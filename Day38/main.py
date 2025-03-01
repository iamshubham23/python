import requests
from datetime import datetime
import os
# NT_APP_ID="baf164bb"
# NT_API_KEY="852f91a69d15b8ae172473a2c5cacd75"

# os.environ["NT_APP_ID"] = "baf164bb"
# os.environ["NT_API_KEY"] = "852f91a69d15b8ae172473a2c5cacd75"
# os.environ["SHEET_ENDPOINT"] = "https://api.sheety.co/1ddbGj_uNBVM55um8XmodBzMiliFZUDY7z6rtgkssd8E/workouts"  
APP_ID=os.environ.get("NT_APP_ID", "baf164bb")
API_KEY=os.environ.get("NT_API_KEY","852f91a69d15b8ae172473a2c5cacd75")
SHEET_ENDPOINT=os.environ.get("SHEET_ENDPOINT","https://api.sheety.co/1ce551fe3e9e2564d4fc53c3b591a61b/workoutTrackings/workouts")
# os.environ["NT_APP_ID"] = "baf164bb"
# os.environ["NT_API_KEY"] = "852f91a69d15b8ae172473a2c5cacd75"
# os.environ["SHEET_ENDPOINT"] = "https://api.sheety.co/1ddbGj_uNBVM55um8XmodBzMiliFZUDY7z6rtgkssd8E/workouts"  # Replace with your Sheety API endpoint

exercise_endpoint="https://trackapi.nutritionix.com/v2/natural/exercise"
# SHEET_ENDPOINT="https://api.sheety.co/1ddbGj_uNBVM55um8XmodBzMiliFZUDY7z6rtgkssd8E/workouts"  
# sheet_endpoint=os.environ["SHEET_ENDPOINT"]
# Production_endpoint ="https://api.syndigo.com"
# UAT_endpoint="https://api.uat.syndigo.com"

GENDER="Male"
WEIGHT=48
HEIGHT=160
AGE=23

exercise_text=input("enter the workout have you done:")
parameters={
    "query":exercise_text,
    "gender":GENDER,
    "age":AGE
}



headers={
    "x-app-id":APP_ID,
    "x-app-key":API_KEY,
}
response=requests.post(exercise_endpoint,json=parameters,headers=headers)
result=response.json()


today_date=datetime.now().strftime("%d/%m/%Y")
now_time=datetime.now().strftime("%X")
bearer_token=os.environ.get('BEARER_TOKEN')
if not bearer_token:
    raise ValueError("Bearer token is not set. Please set the BEARER_TOKEN environment variable.")
bearer_headers={
    "Authorization":f"Bearer {'A8809995391B12'}"
}

for exercise in result["exercises"]:
    sheet_inputs={
        "workout":{
            "date":today_date,
            "time":now_time,
            "exercise":exercise["name"].title(),
            "duration":exercise["duration_min"],
            "calories":exercise["nf_calories"]
        }
    }
    sheet_response=requests.post(SHEET_ENDPOINT,json=sheet_inputs,headers=bearer_headers)
    print(sheet_response.text)
