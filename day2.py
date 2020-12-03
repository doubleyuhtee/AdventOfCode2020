import re
import requests

if __name__ == "__main__":
    headers = {"Cookie": "session=" + str(open("sessioncookie").readline())}
    resp = requests.get("https://adventofcode.com/2020/day/2/input", headers=headers)
    body = resp.content.decode()

    count = 0
    for line in body.splitlines():
        split = re.split('-| |:', line)
        print(line)
        if re.match("(.*" + split[2] + ".*){" + split[0] + "}", split[4]) \
                and not re.match("(.*" + split[2] + ".*){" + split[1] + "}", split[4]):
            count += 1
    print(count)
    # Slow, ugly, doesn't work.  Just for posterity
