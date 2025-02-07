# upload/main.py
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import os


app = FastAPI()

# Root route
@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI root route!"}

@app.post("/upload/")
async def create_upload_file(file: UploadFile):
    file_name = os.getcwd() +"/"+ file.filename.replace(" ", "-")
    contents = await file.read()

    # save the file
    with open(file_name,'wb+') as f:
        f.write(contents)

    return {"filename": file.filename}


