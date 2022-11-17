from csv import DictReader

from django.conf import settings
from django.core.management import BaseCommand

from reviews.models import Comment

ALREADY_EXISTS_IN_DATA_BASE = """
Данные уже загружены в БД! Если нужно загрузить их снова,
то удалите файл db.sqlite3, опосля запустите команду
'python manage.py migrate' чтобы создать новую пустую БД.
"""


class Command(BaseCommand):
    help = 'Загружает данные из comments.csv'

    def handle(self, *args, **options):

        if Comment.objects.exists():
            print('Данные comments уже существуют!')
            print(ALREADY_EXISTS_IN_DATA_BASE)
            return

        print('Идёт загрузка данных comments')

        for row in DictReader(open(
                f'{settings.BASE_DIR}/static/data/comments.csv',
                encoding='utf-8'
        )):
            comments = Comment(id=row['id'],
                               review_id=row['review_id'],
                               text=row['text'],
                               author_id=row['author'],
                               pub_date=row['pub_date'])
            comments.save()
