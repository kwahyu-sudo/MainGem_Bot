import os
from dotenv import load_dotenv
from groq import Groq
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

client = Groq(api_key=GROQ_API_KEY) 
riwayat = {}

def tanya_groq(user_id, pesan):
    if user_id not in riwayat:
        riwayat[user_id] = []
    riwayat[user_id].append({'role':'user','content':pesan}) 
    resp = client.chat.completions.create(
        model='llama-3.3-70b-versatile', 
        messages=[{'role':'system','content':'Kamu asisten pribadi. Jawab Bahasa Indonesia.'}] + riwayat[user_id])
    jawaban = resp.choices[0].message.content 
    riwayat[user_id].append({'role':'assistant','content':jawaban}) 
    return jawaban

async def start(update, context):
    await update.message.reply_text('Halo! Gue asisten lo. Ketik apa aja!')

async def reset(update, context): 
    riwayat[str(update.effective_user.id)] = []
    await update.message.reply_text('Riwayat dihapus!')

async def balas(update, context):
    uid = str(update.effective_user.id) 
    teks = update.message.text
    await context.bot.send_chat_action( chat_id=update.effective_chat.id, action='typing') 
    try:
        jawaban = tanya_groq(uid, teks)
        await update.message.reply_text(jawaban) 
    except Exception as e:
        await update.message.reply_text(f'Error: {e}')

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build() 
app.add_handler(CommandHandler('start', start)) 
app.add_handler(CommandHandler('reset', reset)) 
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, balas)) 
app.run_polling()
