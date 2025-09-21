from fastapi import FASTAPI

app = FastAPI(title="Ethical AI Judge", version="0.1.0")

@app.get("/health")
def health():
  return {"status": "ok"}
