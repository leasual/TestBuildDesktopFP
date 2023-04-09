import pathlib

from peewee import *
from playhouse.migrate import migrate, SqliteMigrator

storage_directory = pathlib.Path('./storage')
storage_directory.mkdir(parents=True, exist_ok=True)

app_database_file = storage_directory.joinpath('deconz.db')
if not app_database_file.exists():
    app_database_file.touch()

app_database = SqliteDatabase(app_database_file)


class User(Model):
    id = AutoField()
    name = CharField(default='')
    password = CharField(default='')
    token = CharField(default='')
    ipaddress = CharField(default='')

    class Meta:
        database = app_database
        table_name = 'user'

    @staticmethod
    def saveUser(ipaddress: str, token: str, password: str, name: str = 'delight'):
        users = User.select()
        if len(users) == 0:
            result = User(name=name, token=token, ipaddress=ipaddress, password=password).save()
            print("save user success= {}".format(result))
        else:
            user = users.first()
            if isinstance(user, User):
                user.name = name
                user.password = password
                user.token = token
                user.ipaddress = ipaddress
                result = user.save()
                print("update user success= {}".format(result))

    @staticmethod
    def getUser():
        return User.select().first()

    @staticmethod
    def deleteUser(userId: int):
        User.select().where(User.id == userId).delete()


class Schedule(Model):
    id = AutoField()
    name = CharField(default='')
    groupId = CharField(default='')
    progress = IntegerField(default=0)
    total = IntegerField(default=0)
    onOff = BooleanField(default=False)
    delay = IntegerField(default=1)

    class Meta:
        database = app_database
        table_name = 'schedule'


app_database.create_tables([Schedule, User])
migrator = SqliteMigrator(app_database)

# migrate database schema
print("database version= {0}".format(app_database.user_version))
# if app_database.user_version < 1:
#     migrate(
#         # migrator.drop_column('schedule', 'password'),
#         migrator.add_column('user', 'password', CharField(default=''))
#     )
#     app_database.user_version = 1
