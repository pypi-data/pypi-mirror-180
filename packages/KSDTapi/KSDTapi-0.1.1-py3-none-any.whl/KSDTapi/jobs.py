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

def getList(volumeName, hostPath):
    url = "http://3.39.12.67:8083/qcc/jobs"

    # params = {
    #     "volumeName": volumeName,
    #     "hostPath": hostPath
    # }

    response = requests.get(f"{url}", headers=headers) # , params=params)

    print("[LIST] ", response.text, flush=True)

    return response.text
# params = {
#     "grant_type": "password",
#     "username": "junesu@sdt.inc",
#     "password": "Sdt251327!",
#     "customerCode": "Q5YK-JRE9-M9FC"
# }


# params = {
#     "namespace": "june"
# }

# params = {
#     "notebookName": "test5",
#     "namespace": "sdt"
# }


# data = json.dumps({
#     "notebookName": "test2",
#     "namespace": "sklim",
#     "image": "jupyter/datascience-notebook:latest",
#     "cpu": 100,
#     "mem": 250,
#     "volumeName": "workspace1"
# })

# data = json.dumps({
#     "volumeName": "workspace2",
#     "namespace": "sklim"
# })


# data = json.dumps({
#     "email": "junetest@sdt.inc",
#     "password": "Sdt251327!"
# })

# data = json.dumps({
#   "code": "SITE-B2C",
#   "name": "b2c",
#   "customerCode": "ZWBC-UZGZ-3GMU"
# })

#print(f"URL = {url}/{method}")
#respeonse = requests.get(f"{url}/{method}/", headers=headers, params=params)
# respeonse = requests.get(f"{url}", headers=headers, params=params)
# respeonse = requests.post(f"{url}", headers=headers, data=data)
#respeonse = requests.post(f"{url}", headers=headers, params=params)
#respeonse = requests.get(f"{url}", headers=headers)

# print(respeonse.text, flush=True)

