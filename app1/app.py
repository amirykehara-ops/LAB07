from flask import Flask, render_template_string
import requests

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tipo de Cambio - Laboratorio</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; background: #f8f9fa; margin: 0; padding: 20px; }
        .container { max-width: 600px; margin: auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        h1 { color: #2c3e50; text-align: center; }
        .rate { display: flex; justify-content: space-between; padding: 12px 0; border-bottom: 1px solid #eee; }
        .label { font-weight: bold; color: #3498db; }
        .value { color: #27ae60; font-size: 1.2em; }
        .footer { text-align: center; margin-top: 20px; color: #7f8c8d; font-size: 0.9em; }
    </style>
</head>
<body>
    <div class="container">
        <h1>💱 Tipo de Cambio Actual</h1>
        <div class="rate">
            <span class="label">Dólar (USD)</span>
            <span class="value">1.00</span>
        </div>
        <div class="rate">
            <span class="label">Euro (EUR)</span>
            <span class="value">{{ eur }}</span>
        </div>
        <div class="rate">
            <span class="label">Sol Peruano (PEN)</span>
            <span class="value">{{ pen }}</span>
        </div>
        <div class="footer">
            <p>Datos proporcionados por <a href="https://www.exchangerate-api.com/" target="_blank">ExchangeRate-API</a></p>
        </div>
    </div>
</body>
</html>
'''

@app.route('/')
def tipo_cambio():
    eur = "1.07"
    pen = "3.78"
    try:
        resp = requests.get('https://api.exchangerate-api.com/v4/latest/USD', timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            eur = round(data['rates'].get('EUR', 1.07), 4)
            pen = round(data['rates'].get('PEN', 3.78), 4)
    except:
        pass  # Usa valores por defecto si falla
    return render_template_string(HTML_TEMPLATE, eur=eur, pen=pen)