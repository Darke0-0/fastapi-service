from urllib.parse import urljoin

import requests
import argparse
from dtype import METADATA

# Replace this with the value of your endpoint 
# ENDPOINT_URL = "https://test1-intern-kanishq.demo1.truefoundry.com/v2/models/test1/infer"

# inp = {"inputs":[
#                 {"name":"array_inputs",
#                  "datatype":"BYTES",
#                  "shape":[-1],
#                  "parameters":{"content_type":"str"},
#                  "data":["Hi, I recently bought a device from your company but it is not working as advertised and I would like to get reimbursed!"]},
#                 {"name":"candidate_labels",
#                  "datatype":"BYTES",
#                  "shape":[-1],
#                  "parameters":{"content_type":"str"},
#                  "data": ["refund", "legal", "faq"]}
#                   ],
#         "outputs":[],
#         "parameters":{}
# }

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

def get_request(query:dict,pipeline:str,endpoint_url:str):
        inp = input_formatting(query=query, pipeline=pipeline)
        response = requests.post(endpoint_url,json=inp, headers={"Content-Type": "application/json"})

        result = response.json()

        return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a ArcHydro schema')
    parser.add_argument('--hf_pipeline', metavar='str', required=True,
                        help='pipeline running')
    parser.add_argument('--endpoint_url', metavar='str', required=True,
                        help='url of endopint')
    parser.add_argument('--query', metavar='str', required=True,
                        help='input query')
    args = parser.parse_args()

    response = get_request(query=args.query, pipeline=args.hf_pipeline, endpoint_url=args.endpoint_url)
    print(response)