from csv import DictReader
from django.conf import settings
from django.core.management import BaseCommand

from reviews.models import Review


ALREADY_EXISTS_IN_DATA_BASE = """
Данные уже загружены в БД! Если нужно загрузить их снова,
то удалите файл db.sqlite3, опосля запустите команду
'python manage.py migrate' чтобы создать новую пустую БД.
"""


class Command(BaseCommand):
    help = 'Загружает данные из review.csv'

    def handle(self, *args, **options):

        if Review.objects.exists():
            print('Данные review уже существуют!')
            print(ALREADY_EXISTS_IN_DATA_BASE)
            return

        print('Идёт загрузка данных review')

        for row in DictReader(open(
                f'{settings.BASE_DIR}/static/data/review.csv',
                encoding='utf-8'
        )):
            review = Review(id=row['id'],
                            title_id=row['title_id'],
                            text=row['text'],
                            author_id=row['author'],
                            score=row['score'],
                            pub_date=row['pub_date'])
            review.save()
