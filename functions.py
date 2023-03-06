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


#GET THE BLOCK WE GONNA LOOP THROUGH

def get_the_main_block(response):
    data = response.text
    parse_json = json.loads(data)
    list_predictions = parse_json['result'][0]['prediction']
    return list_predictions

#EXTRACTING DATA FROM THE MAIN BLOCK OF DATA  

def extract_data_to_lists(list_predictions=list,Module=list,Evaluation=list,Note=list):
    for i in list_predictions:
        for j in i['cells']:
            if (j['label']=='Matiere'):
                Module.append(j['text'])
            elif (j['label']=='Type'):
                Evaluation.append(j['text'])
            elif (j['label']=='Note'):
                Note.append(j['text'])


#MAKING A DATAFRAM FROM LISTS

def make_dataframe_with_lists(Module, Evaluation,Note):
    df = pd.DataFrame(list(zip(Module,Evaluation,Note)),columns=["Module","Evaluation","Note"])
    return df


images_uploaded_link = ['Screenshot_20230305_190131_iit.jpg','Screenshot_20230305_190138_iit.jpg','Screenshot_20230305_190144_iit.jpg']
#PROCESS ALL IMAGES
link_api = 'https://app.nanonets.com/api/v2/OCR/Model/8e075f0c-ba58-451c-8f28-af3f1fda66d9/LabelFile/?async=false'
def process_all_images(images_links):
    for links in images_links:
        image_file_path = ('./images/'+links)
        response = get_response_from_api(image_file_path,link_api)
        list_predictions = get_the_main_block(response)
        extract_data_to_lists(list_predictions,Module_list,Evaluation_list,Note_list)
        dataframe = make_dataframe_with_lists(Module_list,Evaluation_list,Note_list)
        print(dataframe)

process_all_images(images_uploaded_link)