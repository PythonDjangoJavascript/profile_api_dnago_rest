
import requests


def client():

    # toekn_h = "Token e9629460697686c3586ee1f2a1f3de589c3bd8cd"
    reg_data = {
        'username': 'resttest',
        'email': 'test@rest.com',
        'password1': 'testpassword1234',
        'password2': 'testpassword1234'
    }

    response = requests.post("http://127.0.0.1:8000/api/rest-auth/registration/",
                             data=reg_data)

    # headers = {"Authorization": toekn_h}

    # response = requests.get("http://127.0.0.1:8000/api/profiles/",
    #                         headers=headers)

    print("status code: ", response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()
