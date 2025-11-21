# Laboratorio: Aplicaciones Flask en AWS Lambda

## 🎯 Objetivo
Desarrollar dos aplicaciones Flask listas para despliegue en AWS Lambda:
1. **Tipo de cambio** (USD, EUR, PEN) usando API pública.
2. **Catálogo de vehículos** con datos simulados.

---

## 🖥️ Aplicaciones

### App 1: Tipo de cambio
- Endpoint: `/`
- Muestra un diseño HTML responsivo con los tipos de cambio actuales.
- Usa [ExchangeRate-API](https://www.exchangerate-api.com/) como fuente.
- Incluye valores por defecto en caso de fallo de la API.

### App 2: Catálogo de vehículos
- Endpoint: `/`
- Diseño moderno con lista de vehículos (marca, modelo, año, precio).
- Datos simulados (no requiere base de datos externa).

- Listo para despliegue con Zappa: Ambas aplicaciones (app1 y app2) están completamente configuradas y listas para desplegarse en AWS Lambda mediante Zappa. Incluyen los archivos zappa_settings.json con configuración adecuada para la región us-east-1, manejo de roles desactivado (manage_roles: false) y nombre de rol predefinido para entornos con permisos IAM limitados


---

## 📦 Requisitos
- Python 3.9+
- `pip install -r requirements.txt`

## ▶️ Ejecución local
```bash
# App 1
cd app1
$env:FLASK_APP = "app.py" flask run

# App 2
cd app2
$env:FLASK_APP = "app.py" flask run


