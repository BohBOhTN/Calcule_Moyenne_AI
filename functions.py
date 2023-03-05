import pandas as pd
import requests
import json
import boto3


#SOME LOCAL VARIABLE DECLARATION for testing perpuses

link_api = 'https://app.nanonets.com/api/v2/OCR/Model/8e075f0c-ba58-451c-8f28-af3f1fda66d9/LabelFile/?async=false'
file_path = './images/Screenshot_20230305_190131_iit.jpg'
Module_list = []
Evaluation_list = []
Note_list = []
##CALLING THE API FUNCTION


def get_response_from_api(link,path):
    url = link
    data = {'file': open(path, 'rb')}
    response = requests.post(url, auth=requests.auth.HTTPBasicAuth('51d0a0da-ba9d-11ed-a27e-22a1d9fde453', ''), files=data)
    return response


