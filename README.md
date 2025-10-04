# Telegram Bot (Python + Render)

Этот бот принимает сообщения с сайта (через `?start=...` в ссылке) и пересылает их админу.

## 🚀 Установка

1. Создай бота через [BotFather](https://t.me/BotFather) и получи токен.
2. Форкни или склонируй этот репозиторий.
3. Добавь файл `requirements.txt` с зависимостями.

## ⚙️ Деплой на Render

1. Зайди на [Render](https://render.com) → **New Web Service**.
2. Подключи свой GitHub-репозиторий.
3. Укажи:
   - **Environment**: Python
   - **Build Command**:  
     ```bash
     pip install -r requirements.txt
     ```
   - **Start Command**:  
     ```bash
     python bot.py
     ```
4. В настройках Render добавь переменные окружения:
   - `BOT_TOKEN` = твой токен от BotFather
   - `ADMIN_CHAT_ID` = твой chat_id

## 🔗 Ссылка с сайта

Пример:
```html
<a href="https://t.me/YourBot?start=Forex_Consultation" target="_blank">
  Связаться через Telegram
</a>
