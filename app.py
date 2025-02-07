# upload/main.py
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import os

IMAGEDIR = "images/"

app = FastAPI()

# Ensure the directory exists
if not os.path.exists(IMAGEDIR):
    os.makedirs(IMAGEDIR)

# Root route
@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI root route!"}

@app.post("/upload/")
async def create_upload_file(file: UploadFile):
    file_name = os.path.join(IMAGEDIR, file.filename.replace(" ", "-"))
    contents = await file.read()

    # Save the file
    with open(file_name, 'wb+') as f:
        f.write(contents)

    return {"filename": file.filename}
