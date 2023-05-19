# FastAPI Service

This fastapi service takes input for the model and internally converts the input to V2 inference protocol and returns the response.

## Run
### Run service on remote server
Change the value of data dictionary

```bash
curl --request POST \
  --url https://code1-intern-kanishq-8000.demo1.truefoundry.com/predict \
  --header 'Content-Type: application/json' \
  --data '{"hf_pipeline":"object-detection","model_deployed_url":"https://test1-intern-kanishq.demo1.truefoundry.com/v2/models/test1/infer","inputs":"https://i.imgur.com/ExdKOOz.png","parameters":"None"}'
```

### Run service locally

Clone the repository
```bash
git clone https://github.com/Darke0-0/trufoundry_assign.git && cd fastapi-service
```

Create a virtual environment and activate it:
```python
python -m venv venv
. venv/scripts/activate
```

Install dependencies by running
```python
python -m pip install -r requirements.txt
```

Run

Change value of input keeping the structure same

```python
python main.py --input '{"hf_pipeline":"object-detection","model_deployed_url":"https://test1-intern-kanishq.demo1.truefoundry.com/v2/models/test1/infer","inputs":"https://i.imgur.com/ExdKOOz.png","parameters":"None"}'
```
