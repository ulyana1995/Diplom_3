from data.user_data import build_order_payload
from api.order_api import create_order

def create_order_by_api(token, ingredients_list):
    payload = build_order_payload([ingredients_list[0]])
    response = create_order(payload, token)
    return response.json()["order"]["number"]