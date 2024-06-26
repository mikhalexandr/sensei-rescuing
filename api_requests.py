import requests


def registerUser(name, password, level_amount, time):
    url = "https://mikhalexandr.pythonanywhere.com/api/user/add"
    data = {
        "name": name,
        "password": password,
        "level_amount": level_amount,
        "time": time
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("Register success")
    else:
        print("Register error:", response.status_code)


def checkUser(name):
    url = f"https://mikhalexandr.pythonanywhere.com/api/user/check/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        print('Checking success')
        return response.json()
    else:
        print("Checking error:", response.status_code)


def updateUser(name, level_amount, time):
    url = f"https://mikhalexandr.pythonanywhere.com/api/user/upload/{name}"
    data = {
        "level_amount": level_amount,
        "time": time
    }
    response = requests.put(url, json=data)
    if response.status_code == 200:
        print("Update success")
    else:
        print("Update error:", response.status_code)


def getLeaderboard(name):
    url = f"https://mikhalexandr.pythonanywhere.com/api/leaderboard/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        print('Get success')
        leaders = response.json()[0]
        user_place = response.json()[1]
        return leaders, user_place
    else:
        print("Get error:", response.status_code)
