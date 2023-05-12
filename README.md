# FastAPI Excel File Read
Read Excel file and return the values within it.

### Requires
Python 3 and pipenv

### Install Requirements
```
pipenv install
```

### Setup SQLite database (will clear existing data if re-run)
```
cd data_layer
python make_db.py
```
Note if `python` not recognised in the 2nd line, try `python3` instead.

### Launch

```
pipenv shell
uvicorn app:app --reload
```

Can now interact with the API using swagger docs:
http://127.0.0.1:8000/docs#/default/get_file_data_uploadexcelfile__post

`Choose file` within the swagger can be used to select an Excel file.