from django.db import models

# Посмотреть метаклассы, добавить ордеринг по времени для выступлений, мб еще что то


class Role(models.Model):
    ROLES = [
        ('admin', 'admin'),
        ('speaker', 'speaker'),
        ('customer', 'customer'),
        ('unregistered_customer', 'unregistered_customer'),
    ]
    role = models.CharField('Роль', max_length=50, choices=ROLES)

    def __str__(self):
        return self.role


class User(models.Model):
    tg_id = models.IntegerField('Телеграм ID', null=True, blank=True)
    username = models.CharField('Username', max_length=50)
    role = models.ForeignKey(
        Role,
        on_delete=models.SET_NULL,
        null=True,
        related_name='users',
        verbose_name='роль',
        default='unregistered_customer',
    )

    def __str__(self):
        return self.username


class Event(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание', blank=True)
    users = models.ManyToManyField(
        User,
        related_name='users',
        verbose_name='Участники',
        blank=True,
    )

    def __str__(self):
        return self.title


class Cutaway(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='cutaway',
        verbose_name='Владелец визитки',
    )
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    age = models.SmallIntegerField('Возраст')
    specialization = models.CharField(
        'Специализация',
        max_length=50,
        blank=True,
    )
    stack = models.TextField('Стек', blank=True)
    hobby = models.TextField('Хобби', blank=True)
    objective = models.TextField('Цель знакомства', blank=True)
    location = models.CharField('Город', max_length=50, blank=True)
    grade = models.CharField('Грейд', max_length=50, blank=True)


class Speech(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='speeches',
        verbose_name='Спикер',
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='speeches',
        verbose_name='Мероприятие',
    )
    title = models.CharField('Тема', max_length=50, blank=True)
    description = models.TextField('Описание', blank=True)
    time_start = models.DateTimeField('Время начала', blank=True)
    time_end = models.DateTimeField('Время окончания', blank=True)

    class Meta:
        ordering = ['time_start']

    def __str__(self):
        return self.title


class Question(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='questions',
        verbose_name='кто задал',
    )
    text = models.TextField('Вопрос', blank=True)
    speech = models.ForeignKey(
        Speech,
        on_delete=models.CASCADE,
        related_name='questions',
        verbose_name='доклад',
    )
