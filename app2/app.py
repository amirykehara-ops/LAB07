from flask import Flask, render_template_string

app = Flask(__name__)

VEHICULOS = [
    {"marca": "Toyota", "modelo": "Corolla", "año": 2022, "precio": "25,000"},
    {"marca": "Honda", "modelo": "Civic", "año": 2023, "precio": "27,000"},
    {"marca": "Ford", "modelo": "Mustang", "año": 2021, "precio": "35,000"},
    {"marca": "Tesla", "modelo": "Model 3", "año": 2024, "precio": "45,000"}
]

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Catálogo de Vehículos - Laboratorio</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; background: #f8f9fa; margin: 0; padding: 20px; }
        .container { max-width: 800px; margin: auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        h1 { color: #2c3e50; text-align: center; margin-bottom: 30px; }
        .car { display: flex; justify-content: space-between; padding: 15px 0; border-bottom: 1px solid #eee; }
        .car:last-child { border-bottom: none; }
        .info { flex: 3; }
        .price { flex: 1; text-align: right; font-weight: bold; color: #27ae60; font-size: 1.1em; }
        .marca { font-size: 1.2em; color: #2980b9; }
        .modelo { color: #7f8c8d; }
        .footer { text-align: center; margin-top: 20px; color: #7f8c8d; font-size: 0.9em; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚗 Catálogo de Vehículos</h1>
        {% for v in vehiculos %}
        <div class="car">
            <div class="info">
                <div class="marca">{{ v.marca }}</div>
                <div class="modelo">{{ v.modelo }} • {{ v.año }}</div>
            </div>
            <div class="price">US$ {{ v.precio }}</div>
        </div>
        {% endfor %}
        <div class="footer">
            <p>Laboratorio de Aplicaciones Serverless - UTEC</p>
        </div>
    </div>
</body>
</html>
'''

@app.route('/')
def vehiculos():
    return render_template_string(HTML_TEMPLATE, vehiculos=VEHICULOS)