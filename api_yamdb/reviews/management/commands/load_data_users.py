from csv import DictReader

from django.conf import settings
from django.core.management import BaseCommand
from users.models import User

ALREADY_EXISTS_IN_DATA_BASE = """
Данные уже загружены в БД! Если нужно загрузить их снова,
то удалите файл db.sqlite3, опосля запустите команду
'python manage.py migrate' чтобы создать новую пустую БД.
"""


class Command(BaseCommand):
    help = 'Загружает данные из users.csv'

    def handle(self, *args, **options):

        if User.objects.exists():
            print('Данные users уже существуют!')
            print(ALREADY_EXISTS_IN_DATA_BASE)
            return

        print('Идёт загрузка данных users')

        for row in DictReader(open(
                f'{settings.BASE_DIR}/static/data/users.csv',
                encoding='utf-8'
        )):
            users = User(id=row['id'],
                         username=row['username'],
                         email=row['email'],
                         role=row['role'],
                         first_name=row['first_name'],
                         last_name=row['last_name'])
            users.save()
