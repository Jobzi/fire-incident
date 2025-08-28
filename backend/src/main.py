from fastapi import FastAPI

# Crear la aplicación
app = FastAPI()

# Ruta principal
@app.get("/")
def read_root():
    return {"message": "Hello World"}
