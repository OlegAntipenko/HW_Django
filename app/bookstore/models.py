from django.contrib.auth.models import User
from django.db import models

books = [
    {
        'id': 1,
        'title': 'Записки юного врача',
        'description': 'Записки юного врача - с цикла рассказов, вошедших в данный сборник, началась писательская биография М. А. Булгакова. В основу "Записок юного врача" легли автобиографические факты, относящиеся к периоду работы Булгакова земским врачом в одной из сельских больниц Смоленской губернии.',
        'author_id': 1,

    },
    {
        'id': 2,
        'title': 'Белая гвардия',
        'description': '1919-й год. Киев в руках петлюровцев. Страна охвачена ужасами Гражданской войны. Российская история, а с ней и прежние социальные устои, как и система моральных ценностей, в духе которых были воспитаны молодые представители семьи Турбиных, прекратили свое существование. Турбины - потерянное поколение. У них больше нет монарха, империи. Нет прежней родины. Но они пытаются жить, как прежде, и любой ценой сохранить благородство и нравственные ориентиры в безумии наступивших времен. Для лиц старше 16 лет.',
        'author_id': 1,

    },
    {
        'id': 3,
        'title': 'Марсианские хроники',
        'description': '"Марсианские хроники" - цикл новелл, принесших Рэю Бредбери мировую славу, - рассказывает о покорении человеком Красной планеты, где доживает свои последние годы некогда высокоразвитая цивилизация марсиан.',
        'author_id': 2,

    },
    {
        'id': 4,
        'title': 'Вино из одуванчиков',
        'description': 'Войдите в светлый мир двенадцатилетнего мальчика и проживите с ним одно лето, наполненное событиями радостными и печальными, загадочными и тревожными; лето, когда каждый день совершаются удивительные открытия, главное из которых — ты живой, ты дышишь, ты чувствуешь! «Вино из одуванчиков» Рэя Брэдбери — классическое произведение, вошедшее в золотой фонд мировой литературы.',
        'author_id': 2,

    },
    {
        'id': 5,
        'title': 'Скотный Двор',
        'description': '"Все животные равны, но некоторые животные равнее других" - это, наверное, самая знаменитая фраза из классической притчи Джорджа Оруэлла о крушении революционных надежд. Трагический смысл "Скотный двор" проступает сквозь яркий пародийный рисунок. В этой книге Оруэллу удалось выполнить две поставленные перед собой еще в 1936 году задачи: "разоблачить советский миф" и "сделать политическую прозу искусством".',
        'author_id': 3,

    }
]

authors = [
    {
        'id': 1,
        'first_name': 'Михаил',
        'last_name': 'Булгаков',
    },
    {
        'id': 2,
        'first_name': 'Рэй',
        'last_name': 'Брэдбери',
    },
    {
        'id': 3,
        'first_name': 'Джордж',
        'last_name': 'Оруэлл',
    }
]



class Books(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('Authors', on_delete=models.PROTECT)

    @staticmethod
    def create_books():
        for i in books:
            book = Books(title=i['title'], description=i['description'], author_id=i['author_id'])
            book.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


class Authors(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    @staticmethod
    def create_authors():
        for i in authors:
            author = Authors(first_name=i['first_name'], last_name=i['last_name'])
            author.save()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class Comments(models.Model):
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    text = models.TextField(verbose_name="Текст отзыва", max_length=500)
    time_create = models.DateTimeField(auto_now_add=True)
    author_comm = models.ForeignKey(User, on_delete=models.PROTECT)
    book = models.ForeignKey('Books', on_delete=models.PROTECT)

    def __str__(self):
        return self.author_comm
