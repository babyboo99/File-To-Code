import json
import os

STORAGE_FILE = "storage.json"

def load_storage():
    if not os.path.exists(STORAGE_FILE):
        return {}
    with open(STORAGE_FILE, "r") as f:
        return json.load(f)

def save_storage(data):
    with open(STORAGE_FILE, "w") as f:
        json.dump(data, f)