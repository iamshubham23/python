import requests
from twilio.rest import Client
STOCK_NAME="TATAMOTORS.BSE"
COMPANY_NAME="Tata Motors Ltd"
stock_api_key="0JF9WHZM2FF7XL3W"
news_api="c8f2657de60f40ecbda6126b26e8eb39"
TWILIO_SID="ACc9586572d02afda4b5a5084d38ee8ac8"
TWILIO_AUTH_TOKEN="770a85638de1b4578c5e4c2085dece84"
STOCK_ENDPOINT="https://www.alphavantage.co/query"
NEWS_ENDPOINT="https://newsapi.org/v2/everything"
stock_params={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":stock_api_key,
}
response=requests.get(STOCK_ENDPOINT,params=stock_params)
data=response.json()["Time Series (Daily)"]
data_list=[value for (key,value) in data.items()] #list comprehension
yesterday_data=data_list[0]
yesterday_closing_price=yesterday_data['4. close']
before_yesterday=data_list[1]
before_yesterday_closing_price=before_yesterday['4. close']
difference=abs(float(yesterday_closing_price)-float(before_yesterday_closing_price))
up_down=None
if difference >1:
    up_down="⬆️"
else:
    up_down="⬇️"    
percentage_diff=round(difference/float(yesterday_closing_price))*100
print(percentage_diff)
if abs(percentage_diff) <=5:
    news_params={
        "apiKey":news_api,
        "q":COMPANY_NAME,
    }
    news_response=requests.get(NEWS_ENDPOINT,params=news_params)
    articles=news_response.json()["articles"]
    three_articles=articles[:3]
    
    formatted_articles=[f"{STOCK_NAME}: {up_down}{percentage_diff}%\nHeadline: {article['title']}.\nBrief: {article ['description']}" for article in three_articles]
    client=Client(TWILIO_SID,TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message=client.messages.create(
            body=article,
            from_="+17245064443",
            to="+916200874817"
        )