# Импорт необходимых модулей и данных для запроса
import requests
import configuration
import data


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


def get_new_user_token():
    response = post_new_user(data.user_body)
    auth_token = response.json()["authToken"]
    return auth_token
   

def post_new_client_kit(kit_body, authToken):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers={"Content-Type": "applocation/json",
                                  "Autorization": "Berer" + authToken})