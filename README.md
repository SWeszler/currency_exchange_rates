# Currency Exchange Rates API

## Description
This application consists of an RSS scraper and REST API.
1. RSS scraper reads the exchange rates from the European Central Bank and writes them to the database. 
RSS link: https://www.ecb.europa.eu/home/html/rss.en.html  
Fetching the RSS feed is done by the scheduled task. It is scheduled to run every day at midnight.  
For scheduling tasks we can use Cron job, Celery with Redis or Google Cloud Scheduler.  

2. REST API returns the current exchange rate as well as historical data saved in the database.  
It provides the following endpoints:  
  
	GET /api/v1/rates/{currency}/ - returns the latest exchange rate for the given currency  
	GET /api/v1/rates/{currency}/{date} - returns the exchange rate for the given currency and date.  


## Installation
1. Using Docker Compose  
Navigate to the main folder of the project and type in your terminal:
```
	docker-compose up
```
	Attaching docker containers to the terminal for running additional commands, for example:  
```
	docker exec -it currency_exchange_rates_api_web_1 bash
	python manage.py migrate
```

2. Using Virtual Environment  
This method will require you to install Python and Redis on your machine.
```
	pip install virtualenv
	python -m venv env
	source env/bin/activate
	pip install -r requirements.txt
```

## Running the Application
1. REST API
```
	python manage.py runserver <host>:<port>
```
2. Manual Scraping
```
	python manage.py shell < scraper/shell_execute.py
```
3. Asynchronous Task Triggered by Webhook
```
	celery -A exchange_rates worker --loglevel=info
```
```
	curl http://localhost:8000/scraper/run/
```


## Testing

```
python manage.py test
```