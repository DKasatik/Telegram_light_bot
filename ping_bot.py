import os
import telebot
import subprocess
import time

# Замініть 'YOUR_TELEGRAM_BOT_TOKEN' на свій токен бота
bot_token = os.getenv('TELEGRAM_BOT_TOKEN')

# Отримуємо IP адресу зі змінної середовища IP_ADDRESS
ip_address = os.getenv('IP_ADDRESS')

# Отримуємо chat_id зі скрипта get_chat_id.py
chat_id = None
try:
    import asyncio
    from telegram import Bot

    async def get_chat_id():
        bot = Bot(bot_token)
        updates = await bot.get_updates()

        for update in updates:
            chat_id = update.message.chat.id
            return chat_id

    if __name__ == '__main__':
        chat_id = asyncio.run(get_chat_id())
except Exception as e:
    print(f"Error getting chat_id: {e}")

# Перевіряємо, чи було отримано значення для chat_id
if chat_id is None:
    print("Error: Failed to get chat_id.")
    exit(1)

# Створюємо бота за допомогою токену
bot = telebot.TeleBot(bot_token)

# Змінна для зберігання попереднього статусу пінгу
previous_status = None

# Функція для надсилання повідомлення
def send_message(message):
    bot.send_message(chat_id, message)

# Функція для пінгу IP і надсилання повідомлення при зміні статусу
def ping_and_send():
    global previous_status
    while True:
        # Пінгуємо IP через оболонку
        result = subprocess.run('ping -c 1 ' + ip_address, shell=True, stdout=subprocess.PIPE)

        # Перевіряємо результат пінгу
        if result.returncode == 0:
            current_status = "🟢🟢🟢 LIGHT 🟢🟢🟢"
        else:
            current_status = "🔴🔴🔴 DARK 🔴🔴🔴"

        # Перевіряємо, чи відбулася зміна статусу
        if current_status != previous_status:
            send_message(current_status)
            previous_status = current_status

        # Чекаємо 30 секунд перед наступним пінгом
        time.sleep(30)

# Запускаємо функцію для пінгу і надсилання повідомлень
ping_and_send()
