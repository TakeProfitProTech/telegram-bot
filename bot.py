import csv
from telegram import Update,  InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler, filters
from rapidfuzz import fuzz

# 1. Bot's token from @BotFather
# BOT_TOKEN = "7861685554:AAFW8j6xOdTW019R7aA-vzVwByYxtrEbwic"  # release
BOT_TOKEN = "8414266678:AAEe23aYGaMR7deZaPry-Jmq3F-osPTLa5k"  # test 

# 2. Admin's chat_id (узнать через @userinfobot или через getUpdates)
# ADMIN_ID = 7550325157  # release
ADMIN_ID = 7690200390   # test

# Loading questions and answers
QUESTIONS = []
with open("questions.csv", "r", encoding="utf-8") as f:
  reader = csv.DictReader(f, delimiter="\t")  # <- tab-delimiter
  for row in reader:
    # row["questions"] contains varians, comma separated
    variants = [v.strip().lower() for v in row["questions"].split(",")]
    QUESTIONS.append( (variants, row["answers"]) )

# *********************************************************************************************************************
#
def get_self_presentation():
  message = "Меня зовут Андрей. Я\u00A0- лидер проекта и трейдер с более чем 10-летним опытом успешной работы на финансовых рынках.\n\n"
  message += "Я могу <a href='https://ru.take-profit.pro/learn/'>научить</a> тебя зарабатывать на бирже (включая теоретические основвы моей торговой методики и необходимую поддержку в твоей самостоятельной торговле) или помогу получать <a href='https://ru.take-profit.pro/copy-trading/'>пассивный доход</a> посредством копи-трейдинга.\n\n"
  message += "Успешность моей работы и моей торговой методики подтверждается статистикой из независимых источников"
  message += " (см. <a href='https://www.myfxbook.com/members/AndreiSM7/smartmoney/11576977'>здесь</a>)"
  return message
# end of def

# *********************************************************************************************************************
#
def get_our_mission_and_services():
  message = "Наша специализация\u00A0- биржевая торговля.\nНаша цель\u00A0- помочь клиентам зарабатывать на трейдинге.\nНаши услуги:\n🎓профессиональное обучение,\n📈торговые сигналы и сопровождение трейдера\n💰получение пассивного дохода от трейдинга.";
  return message
# end of def

# *************************************************************************************************************************
# Returns a clickable link to the user: https://t.me/username if username is found, tg://user?id=USER_ID if not
def get_clickable_user(user):
  if user.username:
    return f"<a href='https://t.me/{user.username}'>@{user.username}</a>"
  else:
    return f"<a href='tg://user?id={user.id}'>Пользователь {user.id}</a>"
# end of def


# *************************************************************************************************************************
# 
def get_main_menu():
  keyboard = [
    [ 
      InlineKeyboardButton("ℹ️\u00A0\u00A0О нас / Услуги", callback_data="about"),
      InlineKeyboardButton( "🌐 Наш сайт", url="https://ru.take-profit.pro")
    ],
    [
      InlineKeyboardButton("🎓\u00A0\u00A0Обучение", callback_data="courses"),
      InlineKeyboardButton("📈\u00A0\u00A0Торговые сигналы", callback_data="signals")
    ],
    [ InlineKeyboardButton("💰\u00A0\u00A0Пассивный доход (копи-трейдинг)", callback_data="copy") ],
    [
      InlineKeyboardButton("🤖\u00A0\u00A0Спросить бот", callback_data="ask_bot"),
      InlineKeyboardButton("📞\u00A0\u00A0Связаться с нами", callback_data="ask_admin")
    ]
  ]
  return InlineKeyboardMarkup(keyboard)



# ***************************************************************************************************
# 
async def reply_to_about_query( update: Update, context: ContextTypes.DEFAULT_TYPE ):
  with open("images/Andrey_256x256.png", "rb") as img:
    await context.bot.send_photo( chat_id = update.effective_chat.id, photo=img, caption="" )

  message = get_self_presentation()
  await update.callback_query.message.reply_text( message, parse_mode="HTML", reply_markup=get_main_menu(), disable_web_page_preview=True )      
# end of def

# ***************************************************************************************************
# 
async def reply_to_courses_query( update: Update, context: ContextTypes.DEFAULT_TYPE ):
  message = '''
    Обучение состоит из следующих этапов:\n
    1) <b>Теория.</b> Вы получите необходимые теоретические знания: будете понимать структуру, научитесь классифицировать движения, происходящие на нем, ознакомитесь с моей торговой системой.\n
    Курс под названием «Торговая система Smart Money» предоставляется <b>бесплатно</b>. Чтобы зарегистрироваться\u00A0- перейдите <a href="https://ru.take-profit.pro/courses/smartmoney/">на наш сайт</a>.\n
    2) <b>Практика на бектесте</b> (по желанию). Закрепляем теорию на исторических данных: учимся собирать рабочий алгоритм, определяем среднее количество сделок, время входов, настраиваем риск-менеджмент, учимся контролю эмоций и дисциплине.\n
    3) <b>Торговля на реальном счете</b>. После прохождения теоретического курса (и, опционально, практики) вы присоединитесь к нашему сообществу трейдеров: будете получать аналитику по рынку и торговые сигналы и торговать в контакте с нами.
  '''
  await update.callback_query.message.reply_text( message, parse_mode="HTML", reply_markup=get_main_menu(), disable_web_page_preview=True )      
# end of def

# ***************************************************************************************************
# 
async def reply_to_signals_query( update: Update, context: ContextTypes.DEFAULT_TYPE ):
  message = '''
    Мы предлагаем Вам присоединитесь к нашему сообществу трейдеров, где Вы будете получать нашу аналитику по рынку и наши торговые сигналы и сможете торговать в контакте с нами.\n
    📞Если Вы заинтересовались\u00A0- свяжитесь с нами".
  '''
  await update.callback_query.message.reply_text( message, parse_mode="HTML", reply_markup=get_main_menu(), disable_web_page_preview=True )      
# end of def

# ***************************************************************************************************
# 
async def reply_to_copy_query( update: Update, context: ContextTypes.DEFAULT_TYPE ):
  message = '''
    Хотите зарабатывать на трейдинге, но не готовы самостоятельно сидеть за графиками? Eсть решение\u00A0— автоматическое копирование наших сделок на Вашем счете (копи-трейдинг).\n
    Как это работает?
    1. Вы открываете личный брокерский счёт у одного из рекомендованных мною брокеров (или по Вашему выбору).
    2. Пополняете счет на сумму от 200 USD.
    3. Подключаетесь к нам через платформу копирования.\n
    С этого момента все наши сделки автоматически дублируются на Вашем счёте (в пропорции к депозиту), 
    а Ваши деньги всегда будут Вашим контролем — можете пополнять и выводить средства в любое время.\n
    📞Если Вы заинтересовались\u00A0- свяжитесь с нами".
  '''
  await update.callback_query.message.reply_text( message, parse_mode="HTML", reply_markup=get_main_menu(), disable_web_page_preview=True )      
# end of def

# ***************************************************************************************************
# 
async def reply_to_ask_admin_query( update: Update, context: ContextTypes.DEFAULT_TYPE ):
  clickable_user = get_clickable_user( update.effective_user )
  toAdmin = f"📨 Запрос от пользователя\n" \
    f"👤 {clickable_user}\n\n" \
    f"Пользователь хочет связаться со специалистом."

  await context.bot.send_message(
    chat_id=ADMIN_ID,
    text = toAdmin,
    parse_mode = "HTML",
    #disable_web_page_preview = True
  )

  await update.callback_query.message.reply_text("🤖✅\u00A0\u00A0Ваш запрос отправлен. Специалист свяжется с вами в течение 24-х часов.")
# end of def


# *************************************************************************************************
# Menu button handler
#
async def main_menu_button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
  query = update.callback_query
  await query.answer()

  if query.data == "about":
    await reply_to_about_query( update, context )
  elif query.data == "courses":
    await reply_to_courses_query( update, context )
  elif query.data == "signals":
    await reply_to_signals_query( update, context )
  elif query.data == "copy":
    await reply_to_copy_query( update, context )
  elif query.data == "ask_bot":
    await query.message.reply_text("🤖\u00A0\u00A0 Напишие, пожалуйста, ваш вопрос, и я постараюсь ответить:")
  elif query.data == "ask_admin":
    await reply_to_ask_admin_query( update, context )
# end of main_menu_button_handler


# *************************************************************************************************
# Bot functionality
#
async def user_message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
  text = update.message.text.lower().strip()

  best_score = 0
  best_answer = None

  for variants, answer in QUESTIONS:
    for variant in variants:
      score = fuzz.partial_ratio(text, variant)
      if score > best_score:
        best_score = score
        best_answer = answer

  if best_score > 70:
    await update.message.reply_text( "🤖\u00A0\u00A0" + best_answer, reply_markup=get_main_menu(), parse_mode="HTML" )
  else:
    await update.message.reply_text(
      "🤖🤔\u00A0\u00A0Не уверен, что понял вас. Попробуйте уточнить вопрос или нажмите \"📞\u00A0\u00A0Связаться с нами\".",
      reply_markup=get_main_menu(),
    )

'''
  # Sending to admin
  user = update.effective_user
  await context.bot.send_message(
    chat_id = ADMIN_ID,
    text = f"📨 Новый вопрос от @{user.username or user.id}:\n\n{text}",
  )
'''
# end of message_handler


# ************************************************************************
# "/start" command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
  arg = context.args[0] if context.args else ""

  # No arg - a user pushed "/start" and no parameters are given
  if arg == "":
    toUser = f"🤖\u00A0\u00A0<i>Приветствуем Вас на канале проекта <a href='https://ru.take-profit.pro'>Take-Profit.Pro</a></i>.\n"
    toUser += get_our_mission_and_services()
    # Sending the message to the user 
    await update.message.reply_text( f"{toUser}", parse_mode = "HTML", reply_markup = get_main_menu() )      
    return

  # A user wants to contact us (from the web-site)
  toUser = "🤖\u00A0\u00A0<i>Здравствуйте!</i>\n";
  toAdmin = "Пользователь хочет связаться.\n"

  if arg == "courses":
    toUser += "Вы интересуетесь обучением - отлично!\n"
    toUser += "⌛ <b>Специалист свяжется с Вами в течение 24 часов.</b>\n"
    toAdmin = "Хочу пройти обучение"
  elif arg == "signals":
    toUser += "Вы интересуетесь получением торговых сигналов - отлично!\n"
    toUser += "⌛ <b>Специалист свяжется с Вами в течение 24 часов.</b>\n"
    toAdmin = "Хочу присоединиться к сообществу и получать торговые сигналы"
  elif arg == "copy":
    toUser += "Вы интересуетесь получением пассивного дохода - отлично!\n"
    toUser += "⌛ <b>Специалист свяжется с Вами в течение 24 часов.</b>\n"
    toAdmin = "Интересует пассивный доход (копи-трейдинг)"
  elif arg == "practice":
    toUser += "Вас интересует практика на исторических данных - отлично!\n"
    toUser += "⌛ <b>Специалист свяжется с Вами в течение 24 часов.</b>\n"
    toAdmin = "Интересует практика на бектесте"
  elif arg == "other":
    toUser += "⌛ <b>Специалист свяжется с Вами в течение 24 часов ответит на Ваши вопросы.</b>\n"
    toAdmin = "Общий вопрос"
  else:
    toUser += "⌛ <b>Специалист свяжется с Вами в течение 24 часов.</b>\n"

  toUser += "\n\n<i>Спасибо, что проявили интерес к нашему проекту!</i>"

  # To User
  await update.message.reply_text( f"{toUser}", parse_mode = "HTML", reply_markup = get_main_menu() )      

  # To Admin
  clickable_user = get_clickable_user(update.effective_user)
  await context.bot.send_message( chat_id = ADMIN_ID, text = f"📩 From: {clickable_user}\nSubject:\n{toAdmin}", parse_mode = "HTML" )
# end of def


def main():
  app = Application.builder().token(BOT_TOKEN).build()
  app.add_handler(CommandHandler("start", start))
  app.add_handler(CallbackQueryHandler(main_menu_button_handler))
  app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, user_message_handler))
  app.run_polling()

if __name__ == "__main__":
  main()
