from fastapi import FastAPI
from input_formatting import Input_Formatting
import requests

app = FastAPI()

@app.post("/predict")
def predict(input: dict):

    model_deployed_url = input['model_deployed_url']

    input = Input_Formatting(query=input)
    v2_input = input.v2_input()

    response = requests.post(model_deployed_url ,json=v2_input, headers={"Content-Type": "application/json"})
    
    result = response.json()
    return {"prediction": result}
