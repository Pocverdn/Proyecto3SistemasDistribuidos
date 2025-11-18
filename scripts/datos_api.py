import requests
import boto3

API_URL = "https://www.datos.gov.co/resource/gt2j-8ykr.json?$limit=50000"

BUCKET_NAME = "proyecto3datalake"
S3_KEY = "raw/covid/api/covid_api.json"

s3_client = boto3.client('s3')

print(f"Conectando a API: {API_URL} ...")

try:

    with requests.get(API_URL, stream=True) as response:
        response.raise_for_status()
        
        print("Guardando respuesta JSON en S3...")
        
        s3_client.upload_fileobj(
            response.raw, 
            BUCKET_NAME, 
            S3_KEY
        )

    print("¡Ingesta API completada con éxito!")

except Exception as e:
    print(f"Error: {e}")
    raise e