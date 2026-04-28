import subprocess
import os
import json
from main import app
from fastapi.openapi.utils import get_openapi

# Генерация openapi.json v2
openapi_schema = get_openapi(
    title=app.title,
    version=app.version,
    openapi_version="3.0.2",
    description=app.description,
    routes=app.routes,
)

# Сохраняем схему в файл
os.makedirs("generated", exist_ok=True)
with open("generated/openapi.json", "w") as f:
    json.dump(openapi_schema, f, indent=2)

print("openapi.json generated in generated/ folder.")

# Использование openapi-generator-cli для создания Python клиента
try:
    subprocess.run([
        "openapi-generator-cli", "generate",
        "-i", "generated/openapi.json",
        "-g", "python",
        "-o", "generated/"
    ], check=True)
    print("OpenAPI Python client generated in generated/ folder.")
except FileNotFoundError:
    print("openapi-generator-cli not found. Please install it or generate the client manually.")
except subprocess.CalledProcessError as e:
    print(f"Error during client generation: {e}")
