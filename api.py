from fastapi import FastAPI


app=FastAPI()

@app.get('/')
def rea_root():
    return {"Welcome":"wenas"}