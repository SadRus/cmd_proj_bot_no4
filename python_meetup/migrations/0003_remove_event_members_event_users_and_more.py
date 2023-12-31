# Generated by Django 4.2.2 on 2023-06-23 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('python_meetup', '0002_question_speech_speech_event_alter_event_members_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='members',
        ),
        migrations.AddField(
            model_name='event',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='users', to='python_meetup.user', verbose_name='Участники'),
        ),
        migrations.AlterField(
            model_name='cutaway',
            name='objective',
            field=models.TextField(blank=True, verbose_name='Цель знакомства'),
        ),
        migrations.AlterField(
            model_name='question',
            name='speech',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='python_meetup.speech', verbose_name='доклад'),
        ),
    ]
