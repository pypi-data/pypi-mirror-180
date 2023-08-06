import requests
import json


class ApiSession:
    session = requests.session()

    @staticmethod
    def get(url):
        try:
            return ApiSession.session.get(url)
        except requests.exceptions.ConnectionError:
            ApiSession.session = requests.session()
            return ApiSession.get(url)


def check_user(username):
    res = {'code': 'NotFound', 'message': ''}
    for i in range(10):
        try:
            res = json.loads(ApiSession.get(
                f'https://api.scratch.mit.edu/users/{username}'
            ).text)
        except requests.exceptions.ConnectionError:
            continue

    if res.get('code'):
        return False
    return True


def get_followers(username):
    followers = []
    offset = 0
    while True:
        check = len(followers)

        try:
            followers += list(part['username'] for part in json.loads(ApiSession.get(
                f'https://api.scratch.mit.edu/users/{username}/followers?limit=40&offset={offset}'
            ).text))
        except requests.exceptions.ConnectionError:
            continue

        offset += 40

        if check == len(followers) or check > 500:
            break
    return followers


def get_following(username):
    following = []
    offset = 0
    while True:
        check = len(following)

        try:
            following += list(part['username'] for part in json.loads(ApiSession.get(
                f'https://api.scratch.mit.edu/users/{username}/following?limit=40&offset={offset}'
            ).text))
        except requests.exceptions.ConnectionError:
            continue

        offset += 40

        if check == len(following) or check > 500:
            break
    return following
