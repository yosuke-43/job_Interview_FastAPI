from fastapi import FastAPI

app = FastAPI()

# ルーティング
@app.get("/")
async def index():
  return {"message": "Success!!!!"}

@app.post("/interviews")
async def interviews(interviews: Interview):
  return {"interviews": interviews}