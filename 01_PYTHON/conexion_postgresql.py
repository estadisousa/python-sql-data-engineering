
import os
import psycopg2
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

conexion = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

try:
    consulta = """
    SELECT nombre, sueldo, departamento
    FROM empleados
    ORDER BY sueldo DESC;
    """

    with conexion.cursor() as cursor:
        cursor.execute(consulta)
        registros = cursor.fetchall()
        columnas = [col[0] for col in cursor.description]

    df = pd.DataFrame(registros, columns=columnas)

    print("CONEXIÓN EXITOSA A POSTGRESQL")
    print(df.to_string(index=False))

    df.to_excel("reporte_empleados.xlsx", index=False)
    print("Reporte Excel generado correctamente.")

finally:
    conexion.close()
