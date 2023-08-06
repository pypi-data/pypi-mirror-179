"""
Опорная схема базы данных:
На стороне сервера БД содержит следующие таблицы:
 - клиент:
    логин;
    информация.
- история_клиента:
    время входа;
    ip-адрес.
- список_контактов (составляется на основании выборки всех записей с id_владельца):
    id_владельца;
    id_клиента.

"""
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import mapper, sessionmaker
import datetime


class ServerStorage:
    class AllUsers:
        def __init__(self, username, password_hash, ip_address, port, sender_count, recepient_count):
            self.username = username
            self.passwd_hash = password_hash
            self.last_login = datetime.datetime.now()
            self.ip_address = ip_address
            self.port = port
            self.id = None
            self.sender_count = sender_count
            self.recepient_count = recepient_count

    class ClientHistory:
        def __init__(self, user_id, ip_address, port, login_time):
            self.id = None
            self.user_id = user_id
            self.ip_address = ip_address
            self.port = port
            self.login_time = login_time

    class ClientContacts:
        def __init__(self, user_id, contact_name, contact_time, message, send_count, recep_count, is_friend):
            self.user_id = user_id
            self.contact_name = contact_name
            self.contact_time = contact_time
            self.message = message
            self.send_count = send_count
            self.recep_count = recep_count
            self.is_friend = is_friend

    def __init__(self, path):
        self.database_engine = create_engine(
            f'sqlite:///{path}',
            echo=False,
            pool_recycle=7200,
            connect_args={
                'check_same_thread': False})
        self.metadata = MetaData()
        # Создание таблицы пользователей

        users_table = Table('Users', self.metadata,
                            Column('id', Integer, primary_key=True),
                            Column('username', String, unique=True),
                            Column('passwd_hash', String),
                            Column('ip_address', String),
                            Column('port', String),
                            Column('last_login', DateTime),
                            Column('sender_count', Integer),
                            Column('recepient_count', Integer)
                            )
        # Создание таблицы истории активности пользователей
        login_history = Table('login_history', self.metadata,
                              Column('id', Integer, primary_key=True),
                              Column('user_id', ForeignKey('Users.id')),
                              Column('ip_address', String),
                              Column('port', String),
                              Column('login_time', DateTime),
                              )
        # Создание таблицы истории контактов пользователей
        users_contacts = Table('users_contacts', self.metadata,
                               Column('id', Integer, primary_key=True),
                               Column('user_id', ForeignKey('Users.id')),
                               Column('contact_name', String),
                               Column('message', String),
                               Column('contact_time', DateTime),
                               Column('send_count', Integer),
                               Column('recep_count', Integer),
                               Column('is_friend', Boolean)
                               )
        # Создаем таблицы
        self.metadata.create_all(self.database_engine)
        mapper(self.AllUsers, users_table)
        mapper(self.ClientHistory, login_history)
        mapper(self.ClientContacts, users_contacts)
        # Создаем сессию
        session = sessionmaker(bind=self.database_engine)
        self.session = session()

    def user_login(self, username, ip_address, port):
        res = self.session.query(self.AllUsers).filter_by(username=username)
        if res.count():
            user = res.first()
            user.last_login = datetime.datetime.now()
            print(user.ip_address)
            user.ip_address = ip_address
            user.port = port
        else:
            sender_count = 0
            recepient_count = 0
            print(self.get_hash(username))
            user = self.AllUsers(username, self.get_hash(username), ip_address, port, sender_count, recepient_count)
            self.session.add(user)
            self.session.commit()
        date_time = datetime.datetime.now()
        history = self.ClientHistory(user.id, ip_address, port, date_time)
        self.session.add(history)
        self.session.commit()

    def add_user(self, name, passwd_hash):
        """
        Метод регистрации пользователя.
        Принимает имя и хэш пароля, создаёт запись в таблице статистики.
        """
        sender_count = 0
        recepient_count = 0
        user = self.AllUsers(name, passwd_hash, None, None, sender_count, recepient_count)
        self.session.add(user)
        self.session.commit()
        date_time = datetime.datetime.now()
        history = self.ClientHistory(user.id, None, None, date_time)
        self.session.add(history)
        self.session.commit()

    def check_user(self, name):
        """Метод проверяющий существование пользователя."""
        if self.session.query(self.AllUsers).filter_by(username=name).count():
            return True
        else:
            return False

    def get_hash(self, name):
        """Метод получения хэша пароля пользователя."""
        user = self.session.query(self.AllUsers).filter_by(username=name).first()
        return user.passwd_hash

    def contact(self, username, add_contact_name, contact_time, message):
        sender = self.session.query(self.AllUsers).filter_by(username=username).first()

        try:
            recipient = self.session.query(self.AllUsers).filter_by(username=add_contact_name).first()
            sender.sender_count += 1
            recipient.recepient_count += 1
            res = self.session.query(self.AllUsers).filter_by(username=username)
            user = res.first()
            # print(user)
            res = self.session.query(self.ClientContacts).filter_by(user_id=sender.id)
            if res:
                for contact in res:
                    if contact.contact_name == add_contact_name:
                        contact.is_friend = True
                        # print(contact.is_friend)

            is_friend = True
            contacts = self.ClientContacts(user.id, add_contact_name, contact_time, message, sender.sender_count,
                                           recipient.recepient_count, is_friend)
            self.session.add(contacts)
        except AttributeError:
            pass

        self.session.commit()

    def del_contact(self, username, del_contact_name):
        try:
            sender = self.session.query(self.AllUsers).filter_by(username=username).first()
            recipient = self.session.query(self.AllUsers).filter_by(username=del_contact_name).first()
            sender.sender_count += 1
            recipient.recepient_count += 1

            res = self.session.query(self.ClientContacts).filter_by(user_id=sender.id)
            for contact in res:
                if contact.contact_name == del_contact_name:
                    contact.is_friend = False
                    # print(contact.is_friend)
        except AttributeError:
            pass
        self.session.commit()

    def user_list(self, username=None):
        query = self.session.query(
            self.AllUsers.id,
            self.AllUsers.username,
            self.AllUsers.ip_address,
            self.AllUsers.port,
            self.AllUsers.last_login,
            self.AllUsers.sender_count,
            self.AllUsers.recepient_count

        )
        if username:
            query = query.filter(self.AllUsers.username == username)
        return query.all()

    def users_gui(self):
        query = self.session.query(
            self.AllUsers.username,
            self.AllUsers.ip_address,
            self.AllUsers.port,
            self.AllUsers.last_login
        )
        return query.all()

    def stat_gui(self):
        query = self.session.query(
            self.AllUsers.username,
            self.AllUsers.last_login,
            self.AllUsers.sender_count,
            self.AllUsers.recepient_count
        )
        return query.all()

    def history(self, username=None):
        query = self.session.query(
            self.AllUsers.username,
            self.ClientHistory.login_time,
            self.ClientHistory.ip_address,
            self.ClientHistory.port
        ).join(self.AllUsers)
        if username:
            query = query.filter(self.AllUsers.username == username)
        return query.all()

    def contacts_list(self, username):

        query = self.session.query(
            self.AllUsers.username,
            self.ClientContacts.contact_name,
            self.ClientContacts.message,
            self.ClientContacts.contact_time,
            self.ClientContacts.is_friend
        ).join(self.AllUsers)
        if username:
            query = query.filter(self.AllUsers.username == username)
        query_is_friend = query.filter(True == self.ClientContacts.is_friend)
        return query_is_friend.all()

    def to_client_message(self, username):
        query = self.session.query(
            self.AllUsers.username,
            self.ClientContacts.contact_name,
            self.ClientContacts.message,
            self.ClientContacts.contact_time,
            self.ClientContacts.is_friend
        ).join(self.AllUsers)
        if username:
            query = query.filter(self.ClientContacts.contact_name == username)
        return query.all()


if __name__ == '__main__':
    test_db = ServerStorage()
    # print("Версия SQLAlchemy:", sqlalchemy.__version__)
    # test_db.user_login('client_1', '127.0.0.1', 7777)
    # test_db.user_login('client_2', '127.0.0.1', 8888)
    # test_db.user_login('client_3', '127.0.0.1', 7878)
    # test_db.user_login('client_4', '127.0.0.1', 7888)
    # test_db.user_login('client_5', '127.0.0.1', 7888)
    # print('============== test AllUsers ==============')
    # pprint(test_db.user_list())
    # #
    # test_db.contact('client_2', 'client_1', datetime.datetime.now(), 'test_2_1')
    # test_db.contact('client_2', 'client_3', datetime.datetime.now(), 'test_2_3')
    # test_db.contact('client_3', 'client_1', datetime.datetime.now(), 'test_3_1')
    # test_db.contact('client_3', 'client_2', datetime.datetime.now(), 'test_3_2')
    #
    # print('============== test ClientsContacts ==============')
    # test_db.contacts_list('client_2')
    # test_db.contacts_list(None)
    # pprint(test_db.contacts_list('client_2'))
    #
    # print('============== test ClientsHistory ==============')
    # pprint(test_db.history())
    # pprint(test_db.history('client_3'))
