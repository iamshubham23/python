import requests

# api_key="5920f7fd205d096d358448fe4a8b5ac9?"
api_key="96d5ce32adeb3c134db26bd6676fae5b"
#OWM_Endpoint="https://api.openweathermap.org/data/3.0/onecall"
OWM_Endpoint="http://api.weatherstack.com/current"

weather_params={
    "access_key":api_key,
    "query":"25.7609445,87.46858550000002" 
}
response=requests.get(OWM_Endpoint,params=weather_params)
response.raise_for_status()
data=response.json()
print(data)

