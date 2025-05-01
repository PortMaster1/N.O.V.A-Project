import unicorn

# Run the API
unicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)