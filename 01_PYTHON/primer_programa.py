import pandas as pd

datos = {
    "Nombre": ["Ana", "Luis", "Carlos", "María"],
    "Sueldo": [2500, 3500, 4200, 3800]
}

df = pd.DataFrame(datos)

print("BASE DE DATOS")
print(df)

print("\nESTADÍSTICAS")
print("Promedio:", df["Sueldo"].mean())
print("Máximo:", df["Sueldo"].max())
print("Mínimo:", df["Sueldo"].min())