import logging
from telegram import Update
from telegram.ext import CommandHandler, ApplicationBuilder, ContextTypes
import os
application = ApplicationBuilder().token(os.environ['TELETOKEN'])
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id = Update.effective_chat.id,
        text = 'Welcome to ChatGPTIT.'
    )
