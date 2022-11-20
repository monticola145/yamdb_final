from csv import DictReader

from django.conf import settings
from django.core.management import BaseCommand
from reviews.models import Genre

ALREADY_EXISTS_IN_DATA_BASE = """
Данные уже загружены в БД! Если нужно загрузить их снова,
то удалите файл db.sqlite3, опосля запустите команду
'python manage.py migrate' чтобы создать новую пустую БД.
"""


class Command(BaseCommand):
    help = 'Загружает данные из genre.csv'

    def handle(self, *args, **options):

        if Genre.objects.exists():
            print('Данные genre уже существуют!')
            print(ALREADY_EXISTS_IN_DATA_BASE)
            return

        print('Идёт загрузка данных genre')

        for row in DictReader(open(
                f'{settings.BASE_DIR}/static/data/genre.csv',
                encoding='utf-8'
        )):
            genre = Genre(id=row['id'],
                          name=row['name'],
                          slug=row['slug'])
            genre.save()
