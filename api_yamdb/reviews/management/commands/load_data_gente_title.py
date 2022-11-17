from csv import DictReader

from django.conf import settings
from django.core.management import BaseCommand

from reviews.models import GenreTitle

ALREADY_EXISTS_IN_DATA_BASE = """
Данные уже загружены в БД! Если нужно загрузить их снова,
то удалите файл db.sqlite3, опосля запустите команду
'python manage.py migrate' чтобы создать новую пустую БД.
"""


class Command(BaseCommand):
    help = 'Загружает данные из genre_title.csv'

    def handle(self, *args, **options):

        if GenreTitle.objects.exists():
            print('Данные genre_title уже существуют!')
            print(ALREADY_EXISTS_IN_DATA_BASE)
            return

        print('Идёт загрузка данных genre_title')

        for row in DictReader(open(
                f'{settings.BASE_DIR}/static/data/genre_title.csv',
                encoding='utf-8'
        )):
            genre_title = GenreTitle(id=row['id'],
                                     title_id=row['title_id'],
                                     genre_id=row['genre_id'])
            genre_title.save()
