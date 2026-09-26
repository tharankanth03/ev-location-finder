from fastapi import FastAPI

app = FastAPI(title="EV Location Finder API", version="1.0.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
