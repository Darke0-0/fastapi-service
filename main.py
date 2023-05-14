from urllib.parse import urljoin
import json
import uvicorn
import ast
from fastapi import FastAPI
import requests
import argparse
from dtype import METADATA

app = FastAPI()

def query_conversion(query:dict):
    query_list= []
    query_values = list(query.values())
    for i in query_values:

        if isinstance(i,str):
            query_list.append(i)

        elif isinstance(i,list):
            query_list.append(i)

        elif isinstance(i,dict):
            converted = list(i.values())[0]
            query_list.append(converted)
            
    return query_list

def input_formatting(query:dict,pipeline:str):

    query_list = query_conversion(query=query)
    format = dict(METADATA[pipeline])

    inp = []
    for i in range(len(list(format['inputs']))):
        ith_query = query_list[i]
        ith_format = dict(format['inputs'][i])
        ith_format['data'] = ith_query
        ith_format['parameters'] = dict(ith_format['parameters'])
        inp.append(ith_format)

    return {"inputs":inp,"outputs":[],"parameter":{}}

@app.post("/predict")
async def app(query:dict,pipeline:str,endpoint_url:str):
    
    inp = input_formatting(query=query, pipeline=pipeline)
    response = requests.post(endpoint_url,json=inp, headers={"Content-Type": "application/json"})
    result = response.json()

    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a ArcHydro schema')
    parser.add_argument('--hf_pipeline' , required=True,
                        help='pipeline running')
    parser.add_argument('--endpoint_url' , required=True,
                        help='url of endopint')
    parser.add_argument('--query' , required=True,
                        help='input query')
    args = parser.parse_args()

    query = ast.literal_eval(args.query)

    uvicorn.run(app, host="127.0.0.1", port=8000)