import os
import pickle

# Get the file path of the model from environment variables
file_path = os.getenv("LOCAL_MODEL_PATH")

# Check if the model file exists
if not os.path.isfile(file_path):
    raise FileNotFoundError(f"Model file '{file_path}' does not exist.")

# Load the model and pre-computed features from the file
with open(file_path, "rb") as file:
    model, pre_computed_features = pickle.load(file)
    