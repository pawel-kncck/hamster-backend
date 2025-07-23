from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a "route" or "endpoint"
# @app.get tells FastAPI that this function handles GET requests
# to the URL path "/api/hello"


@app.get("/api/hello")
async def hello_world():
    # FastAPI automatically converts Python dictionaries to JSON format
    return {"message": "Hello from you live FastAPI backend!"}
