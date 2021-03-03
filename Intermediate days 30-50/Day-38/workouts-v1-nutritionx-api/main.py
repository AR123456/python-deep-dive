# imports
import requests

#vars
APP_ID = "d0"
API_KEY = "4"

GENDER = "female"
WEIGHT_KG = 67
HEIGHT_CM = 154
AGE = 58

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/5/workoutTracking/workouts"

exercise_text = input("What exercises did you do ? \n")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)