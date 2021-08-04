from fastapi import FastAPI


app=FastAPI()
#coment
@app.get('/')
def rea_root():
    return {"Welcome":"wenas"}