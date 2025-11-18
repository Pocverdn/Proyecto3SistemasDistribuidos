import requests
import boto3
import io

CSV_URL = "https://www.datos.gov.co/api/views/gt2j-8ykr/rows.csv?accessType=DOWNLOAD"
BUCKET_NAME = "proyecto3datalake"

S3_KEY = "raw/covid/url/casos_covid.gz" 

s3_client = boto3.client('s3')

print(f"Iniciando descarga (en modo streaming) desde {CSV_URL}...")

try:

    with requests.get(CSV_URL, timeout=3600, stream=True) as response:
        response.raise_for_status()
        
        print(f"Descarga iniciada. Subiendo (en modo streaming) a s3://{BUCKET_NAME}/{S3_KEY}...")

        s3_client.upload_fileobj(
            response.raw,
            BUCKET_NAME,
            S3_KEY
        )
    
    print("Carga completa a S3 exitosa.")

except requests.RequestException as e:
    print(f"Error al descargar el archivo: {e}")
    raise e
except Exception as e:
    print(f"Error al subir a S3: {e}")
    raise e