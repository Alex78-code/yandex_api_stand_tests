import configuration
import requests
import data


def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH, params={"count":20})

response = get_logs()
print(response.status_code)
print(response.headers)

def get_user_tabel():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)
response = get_user_tabel()
print(response.status_code)

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставляем полный url
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки

response = post_new_user(data.user_body);
print(response.status_code)
print(response.json())

def post_products_kits(products_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         json=products_ids,
                         headers=data.headers)


response = post_products_kits(data.product_ids)
print(response.status_code)
print(response.json())

