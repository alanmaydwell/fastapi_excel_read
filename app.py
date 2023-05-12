import logging
from fastapi import FastAPI, UploadFile
from data_layer.spreadsheet import extract_excel_rows, simple_file_type_check
from data_layer.data_manage import add_file, get_file_details, get_payment_details, record_payments

app = FastAPI()


@app.post("/uploadexcelfile/")
async def get_file_data(file: UploadFile):
    log = logging.getLogger("uvicorn")
    log.info(f"Loading {file.filename}")

    file_data = await file.read()
    rows = extract_excel_rows(file_data)
    spreadsheet_id = add_file(file.filename)
    payment_rows_created = record_payments(spreadsheet_id, rows)

    return {"filename": file.filename, "spreadsheet_id": spreadsheet_id, "rows_read": len(rows), "rows_created": payment_rows_created}


@app.post("/uploadexcelfilecheck/")
async def check_file(file: UploadFile):
    # file_data is standard Python bytes object
    file_data = await file.read()
    file_ok = simple_file_type_check(file_data)
    return {"filename": file.filename, "file_sniff_status": file_ok}


@app.get("/getexistingfilenames")
async def get_existing_filenames():
    details = get_file_details()
    return {"message": details}


@app.get("/getexistingpayments")
async def get_existing_payments():
    details = get_payment_details()
    return {"message": details}

