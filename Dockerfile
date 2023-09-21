FROM python:3.10.4

ADD app.py .

RUN pip install dotenv os yfinance telebot

CMD [ "python", "./app.py"]