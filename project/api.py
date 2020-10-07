from fastapi import FastAPI
from pythainlp.tokenize import word_tokenize # ติดตั้งด้วยคำสั่ง pip install pythainlp

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/word_tokenize/{text}")
def read_word(text: str):
    return {"word": word_tokenize(text)}


@app.get("/b2s/{b}")
def b2s(b:str):
    s = int(b[0])
    e = int(b[1:9], 2)
    f = [ int(x) for x in b[9:] ]
    x = 1 + sum( [ int(f[i])*2**(-(i+1)) for i in range(len(f)) ])
    return {"Result": (-1)**s * 2**(e-127) * x }
    #return {"Result": [s, e, f, x] }