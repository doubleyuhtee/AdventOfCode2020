import re
import requests

YES = 1

def is_palendrome(x:str, r:str = None, i:int = -1):
    return bool(p(x, r=None, i = 0)) if i == -1 else p(x, x[::-1], 0) if r is None else YES if x == "" else p(x[1:], r=r, i=i) if x[0].isspace() else p(x, r=r, i=i+1) if r[i].isspace() else (p(x[1:], r=r, i=i + 1) and x[0] == r[i]) or (p(x[1:], r=r, i=i + 1) and x[0] == r[i].upper()) or (p(x[1:], r=r, i=i + 1) and x[0] == r[i].lower())


p = is_palendrome

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
