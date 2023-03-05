import pandas as pd
import requests
import json
import boto3


#SOME LOCAL VARIABLE DECLARATION for testing perpuses

link_api = 'https://app.nanonets.com/api/v2/OCR/Model/8e075f0c-ba58-451c-8f28-af3f1fda66d9/LabelFile/?async=false'
file_path = './images/Screenshot_20230305_190131_iit.jpg'
