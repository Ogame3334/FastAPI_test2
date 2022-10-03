from fastapi import FastAPI

# FastAPIのオブジェクトを作成
app = FastAPI()

# /に対するGETの処理
@app.get('/')
async def hello():
    return {"text": "hello world!"}