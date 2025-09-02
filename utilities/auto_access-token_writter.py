import requests


def get_access_token():
    url = "https://api.udocs.realtest.uz/api/client/auth/login"

    credentials = {
        "username": "cyber_security",
        "password": "cyber_security_admin"
    }

    headers = {
        "Content-Type": "application/json",
        "X-Task-Id": "api-1",
    }

    post_method = requests.post(url=url, json=credentials, headers=headers)

    token = post_method.json()['data']['token']['access_token']

    token_saver(token=token)


def token_saver(token):
    base_url = "https://api.udocs.realtest.uz/api"

    with open("../.env", "w") as file:
        file.write(f"BASE_URL={base_url} \n"
                   f"TOKEN={token}")


get_access_token()
