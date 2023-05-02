from fastapi import FastAPI, UploadFile
from data_layer.spreadsheet import extract_excel_rows, simple_file_type_check


app = FastAPI()


@app.post("/uploadexcelfile/")
async def get_file_data(file: UploadFile):
    file_data = await file.read()
    rows = extract_excel_rows(file_data)
    return {"filename": file.filename, "spreadsheet_data": rows}


@app.post("/uploadexcelfilecheck/")
async def check_file(file: UploadFile):
    # file_data is standard Python bytes object
    file_data = await file.read()
    file_ok = simple_file_type_check(file_data)
    return {"filename": file.filename, "file_sniff_status": file_ok}
