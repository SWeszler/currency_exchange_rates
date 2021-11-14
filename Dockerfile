FROM python:3.9

WORKDIR /currency_exchange_rates_api
COPY . /currency_exchange_rates_api/

RUN pip install -r requirements.txt