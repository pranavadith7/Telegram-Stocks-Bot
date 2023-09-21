# import creds
from dotenv import load_dotenv
import telebot
import yfinance as yf
from telegram import *
from telegram.ext import *
from requests import *
import os


server = app.server

def configure():
  load_dotenv()

configure()

bot = telebot.TeleBot(os.getenv('API_KEY'))

@bot.message_handler(commands=['greet'])
def greet(message):
  bot.reply_to(message, "Hey! How's it going?")

@bot.message_handler(commands=['hello'])
def hello(message):
  bot.send_message(message.chat.id, "Hello!")


@bot.message_handler(commands=['s'])
def get_stocks(message):
  response = ""
  stocks = ['IOC.BO', 'PRICOLLTD.BO', 'TATAMOTORS.BO', 'BPCL.BO', 'VGUARD.BO']
  res = len(max(stocks, key = len))+10
  stock_data = []
  for stock in stocks:
    data = yf.download(tickers=stock, period='1d')
    data = data.reset_index()
    response += f"-----{stock}-----\n"
    stock_data.append([stock])
    columns = ['STOCKS']
    for row in data.iterrows():
      stock_position = len(stock_data) - 1
      price = round(row[1][4], 2)
      format_date = row[1][0].strftime('%d/%m/%y')
      response += f"{format_date}: {price}\n"
      stock_data[stock_position].append(price)
      columns.append(format_date)

  response = "🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺\n"
  response += columns[0]
  response += "="*(res-len(columns[0]))
  response += columns[1]
  response += "\n🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻\n\n"

  for row in stock_data:
    response += str(row[0])
    response += "="*(res-len(row[0]))
    response += str(row[1])
    response += "\n"
    response += "▬"*17
    response += "\n"

  bot.send_message(message.chat.id,response, parse_mode=ParseMode.HTML)


def stock_request(message):
  request = message.text.split()
  if len(request) < 2 or request[0].lower() not in "price":
    return False
  else:
    return True

@bot.message_handler(func=stock_request)
def send_price(message):
  request = message.text.split()[1]
  data = yf.download(tickers=request, period='5m', interval='1m')
  if data.size > 0:
    data = data.reset_index()
    data["format_date"] = data['Datetime'].dt.strftime('%m/%d %I:%M %p')
    data.set_index('format_date', inplace=True)
    print(data.to_string())
    bot.send_message(message.chat.id, data['Close'].to_string(header=False))
  else:
    bot.send_message(message.chat.id, "No data!?")


bot.polling()
