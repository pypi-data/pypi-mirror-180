import requests

def getResource():
    url = "http://3.39.12.67:8083/qcc/resources"

    response = requests.get(f"{url}") # , params=params)

    print("[LIST] ", response.text, flush=True)

    return response.text