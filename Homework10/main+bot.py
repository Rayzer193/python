from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from calc import calculate2
from interface import *


heap = {
    'count': 0,
    'first': None,
    'second': None,
    'operator': None
}

async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет, {update.effective_user.first_name}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Введите /start, после введите ОТДЕЛЬНЫМИ СООБЩЕНИЯМИ(!!!) первое число, второе число и действие между ними (+, -, *, /)')

async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if heap['count'] != 0:
        if heap['count'] == 1:
            heap['first'] = update.message.text
            heap['count'] += 1
        elif heap['count'] == 2:
            heap['second'] = update.message.text
            heap['count'] +=1
        elif heap['count'] == 3:
            heap['operator'] = update.message.text
            a, b = inp(heap['first'], heap['second'])
            await update.message.reply_text(f"{a} {heap['operator']} {b} = {calculate2(a,b, heap['operator'])}")
            heap['count'] = 0
            heap['first'] = None
            heap['second'] = None
            heap['operator'] = None
           
async def startcalc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    heap ['count'] = 1
    print('бот отработал')

app = ApplicationBuilder().token("6133374676:AAGvs8a04LvJcObUG53pbnvElViFvrjkC2E").build()
app.add_handler(CommandHandler("hello", hello_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("start", startcalc))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calculate))
print('бот запущен')
app.run_polling()