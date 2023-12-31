# Generated by Django 4.2.2 on 2023-06-23 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('organizer', 'организатор'), ('speaker', 'докладчик'), ('member', 'слушатель')], max_length=50, verbose_name='Роль')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_id', models.IntegerField(blank=True, null=True, verbose_name='Телеграм ID')),
                ('username', models.CharField(max_length=50, verbose_name='Username')),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='python_meetup.role', verbose_name='роль')),
            ],
        ),
        migrations.CreateModel(
            name='Speech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, verbose_name='Тема')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('time_start', models.DateTimeField(blank=True, verbose_name='Время начала')),
                ('time_end', models.DateTimeField(blank=True, verbose_name='Время окончания')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='speech', to='python_meetup.user', verbose_name='Спикер')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, verbose_name='Вопрос')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='python_meetup.user', verbose_name='слушатель')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('members', models.ManyToManyField(related_name='users', to='python_meetup.user', verbose_name='мероприятие')),
            ],
        ),
        migrations.CreateModel(
            name='Cutaway',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('age', models.SmallIntegerField(verbose_name='Возраст')),
                ('specialization', models.CharField(blank=True, max_length=50, verbose_name='Специализация')),
                ('stack', models.TextField(blank=True, verbose_name='Стек')),
                ('hobby', models.TextField(blank=True, verbose_name='Хобби')),
                ('objective', models.TextField(blank=True, verbose_name='Описание')),
                ('location', models.CharField(blank=True, max_length=50, verbose_name='Город')),
                ('grade', models.CharField(blank=True, max_length=50, verbose_name='Грейд')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cutaway', to='python_meetup.user', verbose_name='Владелец визитки')),
            ],
        ),
    ]
