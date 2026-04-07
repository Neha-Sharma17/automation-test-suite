from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Test Automation API Running"}

@app.post("/run-tests")
def run_tests():
    result = subprocess.run(
        ["pytest", "-v"],
        capture_output =True,
        text = True
    )
    
    return {
        "output": result.stdout,
        "errors": result.stderr 
    }