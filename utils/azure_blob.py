# from azure.storage.blob import BlobServiceClient
# import pickle
     
# class LoadModel:
    
#     LOCAL_MODEL_PATH_PROP: str = "LOCAL_MODEL_PATH"
#     BLOB_CONNECTION_STRING_PROP: str = "BLOB_CONNECTION_STRING"
#     BLOB_CONTAINER_NAME_PROP: str = "BLOB_CONTAINER_NAME"
#     BLOB_MODEL_NAME_PROP: str = "BLOB_MODEL_NAME"
#     BLOB_MODEL_VERSION_PROP: str = "BLOB_MODEL_VERSION"
#     LOAD_FROM_BLOB_PROP: str = "LOAD_FROM_BLOB"
    
#     def __init__(self,):
#         import os
        
#         self.LOCAL_MODEL_PATH: str = os.getenv(self.LOCAL_MODEL_PATH_PROP, "")
#         if self.LOCAL_MODEL_PATH == "":
#             raise ValueError(f"Environment variable '{self.LOCAL_MODEL_PATH_PROP}' is not defined")
            
#         self.BLOB_CONNECTION_STRING: str = os.getenv(self.BLOB_CONNECTION_STRING_PROP, "")
#         self.BLOB_CONTAINER_NAME: str = os.getenv(self.BLOB_CONTAINER_NAME_PROP, "")
#         self.BLOB_MODEL_NAME: str = os.getenv(self.BLOB_MODEL_NAME_PROP, "")
#         self.BLOB_MODEL_VERSION: str = os.getenv(self.BLOB_MODEL_VERSION_PROP, "")
        
#         self.LOAD_FROM_BLOB: bool = os.getenv(self.LOAD_FROM_BLOB, False)
        
#         self.set_model(self.load_model(self))

#     def load_model(self) -> function:
#         """ Load model from local file storage"""
        
#         if self.LOAD_FROM_BLOB:
#             self.write_model_from_blob_to_local()
            
#         return self.load_local_model()

#     def load_local_model(self):
#         """ Load model from local file storage """
#         with open(self.LOCAL_MODEL_PATH, 'rb') as file:
#             model = pickle.load(file)
#             return model
        
#     def write_model_from_blob_to_local(self):
#         """ Load the blob model """
        
#         if self.BLOB_CONNECTION_STRING == "" or self.BLOB_CONTAINER_NAME == "" or self.BLOB_MODEL_NAME == "" and :
#             raise ValueError(f"In case LOAD_FROM_BLOB = True, '{self.BLOB_CONNCTION_STRING_PROP}', '{self.BLOB_CONTAINER_NAME_PROP}', '{self.BLOB_MODEL_NAME_PROP}' must be defined properly")
        
#         blob_service_client = BlobServiceClient.from_connection_string(self.BLOB_CONNECTION_STRING)
    
#         with open(self.LOCAL_MODEL_PATH, "wb") as file:
#             blob_client = blob_service_client.get_blob_client(container=self.BLOB_CONTAINER_NAME, blob=self.BLOB_MODEL_NAME)
#             blob_data = blob_client.download_blob()
#             file.write(blob_data.readall())
            
#     def get_model(self):
#         return self.model
    
#     def set_model(self, model):
#         self.model = model