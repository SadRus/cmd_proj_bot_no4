from telegram import KeyboardButton


# main menu
customer_main_menu = [
        [KeyboardButton('🤓 Меню участника')],
        [KeyboardButton('❓ ЧаВо'), KeyboardButton('💸 Донат')],
    ]

speaker_main_menu = [
        [KeyboardButton('🤓 Меню участника'), KeyboardButton('🎤 Меню докладчика')],
        [KeyboardButton('❓ ЧаВо'), KeyboardButton('💸 Донат')],
    ]

admin_main_menu = [
        [KeyboardButton('🤓 Меню участника'), KeyboardButton('🎤 Меню докладчика')],
        [KeyboardButton('❓ ЧаВо'), KeyboardButton('💸 Донат')],
        [KeyboardButton('📢 Массовая рассылка')]
    ]

# speakers menu
speaker_menu = [
        [KeyboardButton('✨ Ответить на вопрос')],
        [KeyboardButton('👈 Назад')],
    ]

# customer menu
customer_menu = [
        [
            KeyboardButton('🕜 Расписание'),
            # KeyboardButton('❔ Задать вопрос')
        ],
        [KeyboardButton('👋 Найти собеседника')],
        [KeyboardButton('👈 Назад')]
    ]

# unregistered customer menu
unregistered_customer_menu = [
        [
            KeyboardButton('🕜 Расписание'),
            # KeyboardButton('❔ Задать вопрос')
        ],
        [KeyboardButton('✅ Зарегистрировать анкету')],
        [KeyboardButton('👈 Назад')]
    ]
