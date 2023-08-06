import requests
import json

def create(uploadType, shot, resourceId, filePath):
    url = "http://3.39.12.67:8083/qcc/job"

    headers = {
        #"Content-Type": "application/x-www-form-urlencoded"
        "Content-Type": "application/json"
    }

    data = json.dumps({
        "uploadType": uploadType,
        "shot": shot,
        "resourceId": resourceId,
        "filePath": filePath
    })

    # params = {
    #     "namespace": f"{nameSpace}"
    # }

    response = requests.post(f"{url}", headers=headers, data=data) 

    print("[CREATE] ",response.text, flush=True)

    return response.text

def getList():
    url = "http://3.39.12.67:8083/qcc/jobs"

    # params = {
    #     "volumeName": volumeName,
    #     "hostPath": hostPath
    # }

    response = requests.get(f"{url}") # , params=params)

    print("[LIST] ", response.text, flush=True)

    return response.text
