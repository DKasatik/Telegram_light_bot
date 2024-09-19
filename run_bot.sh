#!/bin/bash

# Запитуємо введення токену бота
read -p "Введіть bot token: " bot_token

# Запитуємо введення IP-адреси
read -p "Введіть IP адресу: " ip_address

# Передаємо токен бота та IP-адресу як змінні середовища та збираємо Docker-контейнер
docker build -t ping_bot --build-arg TELEGRAM_BOT_TOKEN=$bot_token --build-arg IP_ADDRESS=$ip_address .

# Запускаємо контейнер та передаємо токен бота та IP-адресу як змінні середовища
docker run -d -e TELEGRAM_BOT_TOKEN=$bot_token -e IP_ADDRESS=$ip_address ping_bot

# Виводимо повідомлення про успішний запуск
echo "Бот запущено у фоновому режимі."
