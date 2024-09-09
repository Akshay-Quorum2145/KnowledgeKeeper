# import urllib.request
# import json
# import os
# import ssl

# def allowSelfSignedHttps(allowed):
#     # bypass the server certificate verification on client side
#     if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
#         ssl._create_default_https_context = ssl._create_unverified_context

# allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# # Request data goes here
# # The example below assumes JSON formatting which may be updated
# # depending on the format your endpoint expects.
# # More information can be found here:
# # https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
# data = {"query":"hi"}

# body = str.encode(json.dumps(data))

# url = 'https://keeperproj-nfspj.eastus.inference.ml.azure.com/score'
# # Replace this with the primary/secondary key, AMLToken, or Microsoft Entra ID token for the endpoint
# api_key = 'NI7iEU0bE68rJQBHfEu7tHVk8e2X1kV9'
# if not api_key:
#     raise Exception("A key should be provided to invoke the endpoint")


# headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

# req = urllib.request.Request(url, body, headers)

# try:
#     response = urllib.request.urlopen(req)

#     result = response.read()
#     print(result)
# except urllib.error.HTTPError as error:
#     print("The request failed with status code: " + str(error.code))

#     # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
#     print(error.info())
#     print(error.read().decode("utf8", 'ignore'))

from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
 
# Define your connection string and container name
connection_string = 'DefaultEndpointsProtocol=https;AccountName=keeperstorages;AccountKey=ck4uu702O6MY0ehMNrM9xjLydfT6Blo3Ep3IIwPspSnJH7d0gZMqbWJMxPAqQ99B7+p36FnK1/9P+ASt/gdh8w==;EndpointSuffix=core.windows.net'
container_name = 'fileupload-keeperindex'
file_path = 'C:\\Users\\akshay.bachkar\\Downloads\\Exception Resolver.txt'
blob_name = 'Exception Resolver.txt'
 
# Create a BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
 
 
# Get a container client
container_client = blob_service_client.get_container_client(container_name)
 
# Create the container if it does not exist
if not container_client.exists():
    container_client.create_container()
 
# Create a blob client
blob_client = container_client.get_blob_client(blob_name)
 
# Upload the file
with open(file_path, 'rb') as data:
    blob_client.upload_blob(data, overwrite=True)
 
print(f'File {file_path} uploaded to blob storage as {blob_name}')