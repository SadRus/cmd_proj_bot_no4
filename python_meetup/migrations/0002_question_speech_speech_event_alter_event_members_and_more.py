# Generated by Django 4.2.2 on 2023-06-23 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('python_meetup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='speech',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='python_meetup.speech', verbose_name='вопросы'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='speech',
            name='event',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='speeches', to='python_meetup.event', verbose_name='Мероприятие'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='users', to='python_meetup.user', verbose_name='мероприятие'),
        ),
        migrations.AlterField(
            model_name='role',
            name='role',
            field=models.CharField(choices=[('organizer', 'organizer'), ('speaker', 'speaker'), ('member', 'member')], max_length=50, verbose_name='Роль'),
        ),
        migrations.AlterField(
            model_name='speech',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='speeches', to='python_meetup.user', verbose_name='Спикер'),
        ),
    ]
