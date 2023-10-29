# Телеграм бот для работы на ивентах

Телеграм бот, разработанный в рамках командного проекта от [Devman](https://dvmn.org)  
Бот помогает в проведении мероприятий. Для слушателей даёт возможность узнать расписание/задать вопрос спикеру через чат/обменяться визитками с другими посетителями.  
Для спикера даёт возможность просмотреть вопросы и выбрать наиболее интересные из них.

## Запуск

Для запуска бота вам понадобится Python третьей версии.

Скачайте код с GitHub. Установите зависимости:

```sh
pip install -r requirements.txt
```
Запустить бота:
```sh
python main.py
```

### Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступные переменные:
 - `TELEGRAM_BOT_TOKEN`= Токен вашего телеграм бота (можно узнать у [@BotFather](https://t.me/botfather))


## Цели проекта

Код написан в учебных целях — для курса по Python и веб-разработке на сайте [Devman](https://dvmn.org).
