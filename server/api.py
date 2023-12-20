from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

html = """<!DOCTYPE html>
<html>
<body>

<form action="/name">
  <label for="fname">Meno:</label>
  <input type="text" id="fname" name="fname"><br><br>
  <input type="submit" value="Submit">
</form>

</body>
</html>
"""

@app.get("/", tags=["Root"])
async def root():
    return HTMLResponse(content=html, status_code=200)

@app.get("/test")
async def test():
    return {"message": "testing response"}

@app.post("/name")
async def handle_name(name):
    return {"message": f"Hi {name}"}

