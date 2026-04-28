# Демонстрация использования сгенерированного OpenAPI-клиента
# Запускается, когда клиент уже сгенерирован в папке generated/

import sys
sys.path.insert(0, 'generated')

try:
    from generated.openapi_client import Client
    from generated.openapi_client.api.items import get_items_api_v1_items_get, create_item_api_v1_items_post
    print("Client imported successfully. Ready for API calls.")
except ImportError:
    print("OpenAPI client not generated yet. Run generate_v2_openapi.py first or install generated package.")

if __name__ == "__main__":
    print("Demo finished. Make sure to generate the OpenAPI client first.")
