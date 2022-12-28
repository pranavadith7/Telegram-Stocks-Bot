import pywhatkit as kit
import cv2

kit.text_to_handwriting("Hope you are doing well", save_to="handwriting.png")
img = cv2.imread("handwriting.png")
cv2.imshow("Text to Handwriting", img)
cv2.waitKey(0)
cv2.destroyAllWindows()




# @bot.message_handler(commands=['stocks'])
# def get_stocks(message):
#   response = ""
#   stocks = ['IOC.NS', 'PRICOLLTD.NS', 'TATAMOTORS.BO', 'BPCL.BO', 'VGUARD.BO']
#   stock_data = []
#   for stock in stocks:
#     data = yf.download(tickers=stock, period='2d', interval='1d')
#     data = data.reset_index()
#     response += f"-----{stock}-----\n"
#     stock_data.append([stock])
#     columns = ['Stocks']
#     for index, row in data.iterrows():
#       stock_position = len(stock_data) - 1
#       price = round(row['Close'], 2)
#       format_date = row['Date'].strftime('%m/%d')
#       response += f"{format_date}: {price}\n"
#       stock_data[stock_position].append(price)
#       columns.append(format_date)
#     print()

#   response = f"{columns[0] : <10}{columns[1] : ^10}{columns[2] : >10}\n"
#   for row in stock_data:
#     response += f"{row[0] : <10}{row[1] : ^10}{row[2] : >10}\n"
# #   response += "\nStock Data"
#   print(response)
#   bot.send_message(message.chat.id, response)