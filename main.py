from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.environ['TOKEN']

async def go_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.delete()
        text = ' '.join(context.args)
        if not text:
            return
        reply_to = update.message.reply_to_message
        if reply_to and not reply_to.from_user.is_bot:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=text,
                reply_to_message_id=reply_to.message_id
            )
        else:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=text
            )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("go", go_command))

print("Bot is running...")
app.run_polling()
