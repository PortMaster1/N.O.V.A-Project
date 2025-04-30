import uvicorn

# Run the API
uvicorn.run("server:app", host="127.0.0.1", port=8000)
