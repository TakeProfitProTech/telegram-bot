from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# 1. Вставь сюда токен бота от @BotFather
BOT_TOKEN = "7861685554:AAFW8j6xOdTW019R7aA-vzVwByYxtrEbwic"

# 2. Твой chat_id (узнать через @userinfobot или через getUpdates)
ADMIN_ID = 7550325157  

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
  # Получаем параметр (если он был передан в ссылке)
  arg = context.args[0] if context.args else ""

  toAdmin = ""
  toUser = "✅ <i>Здравствуйте! Ваше сообщение получено!</i><br/>";

  if arg == "courses":
    toAdmin = "Хочу пройти обучение"
    toUser += "⌛ <b>Специалист свяжется с Вами в течение 24 часов.</b><br>"
  elif arg == "signals":
    toAdmin = "Хочу присоединиться к сообществу и получать торговые сигналы"
    toUser += "⌛ <b>Специалист свяжется с Вами в течение 24 часов.</b><br>"
  elif arg == "copy":
    toAdmin = "Интересует пассивный доход (копи-трейдинг)"
    toUser += "⌛ <b>Специалист свяжется с Вами в течение 24 часов.</b><br>"
  elif arg == "practice":
    toAdmin = "Интересует практика на бектесте"
    toUser += "⌛ <b>Специалист свяжется с Вами в течение 24 часов.</b><br>"
  else:
    toAdmin = "Общие вопросы"
    toUser += "⌛ <b>Специалист свяжется с Вами в течение 24 часов.</b><br>"
  
  toUser += "<br/><br/><i>Спасибо, что проявили интерес к нашему проекту!</i>"

  # Автоответ пользователю
  await update.message.reply_text(f"{toAdmin}", parse_mode = "HTML")

  # Уведомление администратору
  user = update.effective_user
  username = f"@{user.username}" if user.username else user.full_name
  await context.bot.send_message(
    chat_id=ADMIN_ID,
    text=f"📩 Сообщение от telegram-bot!\n\nОт: {username}\nТема: {toAdmin}"
  )

def main():
  app = Application.builder().token(BOT_TOKEN).build()
  app.add_handler(CommandHandler("start", start))
  app.run_polling()

if __name__ == "__main__":
  main()
