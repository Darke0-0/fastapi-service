import requests
import argparse

ENDPOINT_URL = "https://code1-intern-kanishq-8000.demo1.truefoundry.com/predict"

if __name__ == "__main__":
    # Taking Inputs
    parser = argparse.ArgumentParser("FastAPI")
    parser.add_argument("--input",required=True)
    args = parser.parse_args()
    input = args.input

    json = {}
    # String Formatting for Inputs
    input_list = input.split(',')
    for i in input_list:
        intab = "{},"
        outtab = ""
        trantab = str.maketrans('','',",{}")
        i = i.translate(trantab)
        i_split = i.split(':', 1)
        json[i_split[0]] = i_split[1]

    # Result
    response = requests.post(ENDPOINT_URL,json = json)
    result = response.json()
    print(result)