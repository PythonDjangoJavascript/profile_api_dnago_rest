
import requests


def client():

    toekn_h = "Token e9629460697686c3586ee1f2a1f3de589c3bd8cd"
    credientials = {
        'username': 'sayed',
        'password': '1234'
    }

    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/",
    #                          data=credientials)

    headers = {"Authorization": toekn_h}

    response = requests.get("http://127.0.0.1:8000/api/profiles/",
                            headers=headers)

    print("status code: ", response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()
