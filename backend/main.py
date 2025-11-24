import fastapi
app = fastapi.FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

def main():
    print("Hello from backend!")
    return "backend is running"


if __name__ == "__main__":
    # Run the FastAPI app
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
