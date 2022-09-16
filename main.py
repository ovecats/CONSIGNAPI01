from fastapi import FastAPI

app = FastAPI()



@app.get('/home')
def home():
    return {"message": "consigna"}

@app.get('/Año con más carreras')
def Fecha():
    return {"message": "2021, 23 carreras"}

@app.get('/Piloto con mayor cantidad de primeros puestos')
def name():
    return {"message": "hamilton"}

@app.get('/Nombre del circuito más corrido')
def pista():
    return {"message": "nazionale di monza"}

@app.get('/Piloto con mayor cantidad de puntos en total, cuyo constructor sea de nacionalidad sea American o British')
def nacionalidad():
    return {"message": "jenson button 1154"}

@app.get('/otros')
def end():
    return {"message": "2022"}