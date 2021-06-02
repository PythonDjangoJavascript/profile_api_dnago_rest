
import requests


def client():
    credientials = {
        'username': 'sayed',
        'password': '1234'
    }

    response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/",
                             data=credientials)

    print("status code: ", response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()
