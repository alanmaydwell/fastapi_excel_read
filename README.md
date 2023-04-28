# FastAPI Excel File Read
Read Excel file and return the values within it.

### Requires
Python 3 and pipenv

### Install Requirements
```
pipenv install
```

###Launch

```
pipenv shell
uvicorn app:app --reload
```

Can now interact with the API using swagger docs:
http://127.0.0.1:8000/docs#/default/get\_file\_data\_uploadexcelfile__post

`Choose file` within the swagger can be used to select an Excel file.