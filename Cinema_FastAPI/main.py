from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import os
import json
from scraper import scrape_cinepolis  # Importar la función de scraping

app = FastAPI()

def load_peliculas():
    # Verificar si el archivo JSON existe
    if os.path.exists("peliculas_guardadas.json"):
        # Cargar los datos del archivo JSON
        with open("peliculas_guardadas.json", "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        raise HTTPException(status_code=404, detail="No se encontraron datos de películas.")

@app.get("/peliculas")
async def get_peliculas():
    try:
        # Ejecutar el scraping para actualizar los datos
        scrape_cinepolis()

        # Cargar los datos actualizados
        peliculas_data = load_peliculas()

        # Estructura de respuesta personalizada
        response = {
            "mensaje": "Cartelera Cinepolis Perisur - Funciones para el día de hoy",
            "peliculas": peliculas_data
        }

        return JSONResponse(content=response)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al realizar el scraping: {e}")
