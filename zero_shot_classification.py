from urllib.parse import urljoin

import requests

# Replace this with the value of your endpoint 
ENDPOINT_URL = "https://test1-intern-kanishq.demo1.truefoundry.com/v2/models/test1/infer"

inp = {"inputs":[
                {"name":"array_inputs",
                 "datatype":"BYTES",
                 "shape":[-1],
                 "parameters":{"content_type":"str"},
                 "data":["Hi, I recently bought a device from your company but it is not working as advertised and I would like to get reimbursed!"]},
                {"name":"candidate_labels",
                 "datatype":"BYTES",
                 "shape":[-1],
                 "parameters":{"content_type":"str"},
                 "data": ["refund", "legal", "faq"]}
                  ],
        "outputs":[],
        "parameters":{}
}

response = requests.post(ENDPOINT_URL,json=inp, headers={"Content-Type": "application/json"})
print(response)

result = response.json()

print(result)

