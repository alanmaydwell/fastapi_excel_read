from fastapi import FastAPI, UploadFile
from data_layer.spreadsheet import extract_excel_rows


app = FastAPI()


@app.post("/uploadexcelfile/")
async def get_file_data(file: UploadFile):
    file_data = await file.read()
    rows = extract_excel_rows(file_data)
    return {"filename": file.filename, "spreadsheet_data": rows}
