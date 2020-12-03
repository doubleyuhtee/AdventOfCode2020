import requests

if __name__ == "__main__":
    headers = {"Cookie": "session=" + str(open("sessioncookie").readline())}
    resp = requests.get("https://adventofcode.com/2020/day/2/input", headers=headers)
    body = resp.content.decode()
    print(body)
