import uvicorn
import requests
from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

@app.post("/predict")
async def predict(payload: dict):
    # convert input to V2 inference protocol
    # use pipeline_name to select the appropriate conversion logic
    converted_input = ...

    # send converted input to deployed model
    model_url = "https://my-model.com"
    response = requests.post(model_url, json=converted_input)

    # return response to client
    return response.json()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Start the FastAPI server.")
    parser.add_argument("--hf_pipeline", type=str, required=True, help="Name of Hugging Face pipeline to use.")
    parser.add_argument("--model_deployed_url", type=str, required=True, help="URL of deployed model.")
    args = parser.parse_args()

    # create pipeline based on pipeline_name
    pipeline_name = args.hf_pipeline
    pipeline = pipeline(pipeline_name)

    # start server
    uvicorn.run(app, host="0.0.0.0", port=8000)