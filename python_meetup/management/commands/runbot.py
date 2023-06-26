from django.core.management.base import BaseCommand
from main import updater


class Command(BaseCommand):
    # Используется как описание команды обычно
    help = 'Uses to run a bot'

    def handle(self, *args, **kwargs):
        updater.start_polling()
