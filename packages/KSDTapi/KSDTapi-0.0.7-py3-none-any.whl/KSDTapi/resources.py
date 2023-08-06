def getResource():
    url = "http://3.39.12.67:8083/jobs"

    response = requests.get(f"{url}", headers=headers) # , params=params)

    print("[LIST] ", response.text, flush=True)

    return response.text