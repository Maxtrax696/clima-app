from flask import Blueprint, render_template, request
import requests

main = Blueprint("main", __name__)

API_KEY = "04c0153705a885996184dd708e9e536a"

@main.route("/", methods=["GET", "POST"])
def index():
    clima_info = None
    error = None

    if request.method == "POST":
        ciudad = request.form.get("ciudad")
        if ciudad:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric"
            respuesta = requests.get(url)

            if respuesta.status_code == 200:
                datos = respuesta.json()
                clima_info = {
                    "ciudad": ciudad,
                    "temperatura": datos['main']['temp'],
                    "descripcion": datos['weather'][0]['description']
                }
            else:
                error = "No se pudo obtener el clima de esa ciudad."
        else:
            error = "Por favor ingrese una ciudad."

    return render_template("index.html", clima=clima_info, error=error)
