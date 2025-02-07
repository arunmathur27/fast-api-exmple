# upload/main.py
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import os


IMAGEDIR = "images/"

app = FastAPI()

# Root route
@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI root route!"}
    

@app.post("/upload/")
async def create_upload_file(file: UploadFile):
    file_name = os.getcwd() + "/images/" + file.filename.replace(" ", "-")
    #filename = 'Arunmathur'
    #file.filename = f"{filename}.jpg"
    contents = await file.read()

    # save the file
    with open(file_name,'wb+') as f:
        f.write(contents)

    return {"filename": file.filename}

