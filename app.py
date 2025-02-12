# upload/main.py
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import os
import uvicorn

def init_app():
    app = FastAPI(
         title='Test FastAPI',
         description="Fast API Test",
         version="1.0.1")

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

    return app

app = init_app()

if __name__== '__main__':
    uvicorn.run("app:app", host="localhost", port=8888, reload=True)
    
