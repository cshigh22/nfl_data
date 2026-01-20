import os
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

# 1. SETUP: Load the secret password (connection string)
load_dotenv()
connect_str = os.getenv('AZURE_CONNECTION_STRING')
container_name = "raw"  # The folder created in Azure

# 2. VALIDATION: Crash if no key is found (Safety first!)
if not connect_str:
    raise ValueError("ERROR: AZURE_CONNECTION_STRING not found. Did you check your .env file?")

print(f"Connecting to Azure Container: {container_name}...")

# 3. CONNECT: Create the client
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

# 4. UPLOAD: Find all CSVs in data/raw and push them
local_data_path = os.path.join("data", "raw")

for filename in os.listdir(local_data_path):
    if filename.endswith(".csv"):
        local_file_path = os.path.join(local_data_path, filename)
        
        print(f"Uploading {filename}...")
        
        # Create a client for this specific file
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=filename)
        
        # Open and upload the file data
        with open(local_file_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)
            
        print(" -> Uploaded successfully!")

print("All files uploaded to Azure Data Lake.")