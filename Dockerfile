# Використовуємо образ Ubuntu з Python
FROM ubuntu:20.04

# Оновлюємо пакети та встановлюємо Python і утиліту ping
RUN apt-get update && \
    apt-get install -y python3 python3-pip iputils-ping

# Встановлюємо бібліотеку для телеграм-бота
RUN pip3 install pyTelegramBotAPI

# Копіюємо код бота в образ
COPY ping_bot.py /app/ping_bot.py

# Встановлюємо робочу директорію
WORKDIR /app

# Виконуємо скрипт бота при запуску контейнера
CMD ["python3", "ping_bot.py"]
