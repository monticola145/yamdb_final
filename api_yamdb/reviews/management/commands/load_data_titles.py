from csv import DictReader
from django.conf import settings
from django.core.management import BaseCommand

from reviews.models import Title


ALREADY_EXISTS_IN_DATA_BASE = """
Данные уже загружены в БД! Если нужно загрузить их снова,
то удалите файл db.sqlite3, опосля запустите команду
'python manage.py migrate' чтобы создать новую пустую БД.
"""


class Command(BaseCommand):
    help = 'Загружает данные из titles.csv'

    def handle(self, *args, **options):

        if Title.objects.exists():
            print('Данные titles уже существуют!')
            print(ALREADY_EXISTS_IN_DATA_BASE)
            return

        print('Идёт загрузка данных titles')

        for row in DictReader(open(
                f'{settings.BASE_DIR}/static/data/titles.csv',
                encoding='utf-8'
        )):
            titles = Title(id=row['id'],
                           name=row['name'],
                           year=row['year'],
                           category=row['category'])
            titles.save()
