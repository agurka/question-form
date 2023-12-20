from fastapi import FastAPI

app = FastAPI()

html = """<!DOCTYPE html>
<html>
<body>

<h1>My First Heading</h1>

<p>My first paragraph.</p>

</body>
</html>
"""

@app.get("/", tags=["Root"])
async def root():
    return html

@app.get("/test")
async def test():
    return {"message": "testing response"}

