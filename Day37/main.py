import requests
from datetime import datetime
USERNAME="shubham23a"
TOKEN="as2again3hv89"
pixela_endpoint="https://pixe.la/v1/users"
GRAPH_ID="graph1"
user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
# response=requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)
graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config={
    "id":GRAPH_ID,
    "name":"Cycling Graph",
    "unit":"km",
    "type":"float",
    "color":"ajisai"
    }
headers={
    "X-USER-TOKEN":TOKEN
}    
# response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

today=datetime.now()

pixeela_creation_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_data={
    "date":today.strftime("%Y%m%d"),
    "quantity":"6.5",
}
# response=requests.post(url=pixeela_creation_endpoint,json=pixel_data,headers=headers)
# print(response.text)

pixela_update_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
pixela_update={
    "quantity":"40"
}
response=requests.put(url=pixela_update_endpoint,json=pixela_update,headers=headers)
print(response.text)