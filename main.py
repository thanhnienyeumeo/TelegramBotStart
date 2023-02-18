import logging
from telegram import Update
from telegram.ext import CommandHandler, ApplicationBuilder, ContextTypes, MessageHandler, filters
import os
token = os.environ['TELETOKEN']
print(token)
application = ApplicationBuilder().token(os.environ['TELETOKEN']).build()

def spottedUser(user):
    print('Name:', user.name)
    print('First name:', user.first_name)
    print('Last name', user.last_name)      
    print('Id:', user.id)
    print('----------')

def response(text: str):
    if text in ['hello', 'hi', 'chào']:
        return 'Lô con cặ*'
    if 'Nam' in text:
        return 
    return "Chả hiểu gì sất"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    spottedUser(update.effective_user)
    await context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = 'Welcome to ChatGPTIT.'
    )
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    spottedUser(update.effective_user)
    ans = ' '.join(context.args)
    await context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = ans
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    spottedUser(update.effective_user)
    ans = response(str(update.message.text).lower())

    await context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = ans
    )

#add handle
startHandler = CommandHandler('start', start)
echoHandler = CommandHandler('echo', echo)
messHandler = MessageHandler(filters.TEXT , handle_message)

application.add_handler(startHandler)
application.add_handler(echoHandler)
application.add_handler(messHandler)
print("Bot is ready")
application.run_polling()
