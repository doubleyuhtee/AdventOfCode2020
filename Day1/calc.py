import requests


if __name__ == "__main__":
    headers = {"Cookie": "session=" + str(open("../sessioncookie").readline())}
    resp = requests.get("https://adventofcode.com/2020/day/1/input", headers=headers)
    body = resp.content
    values = [int(x) for x in body.decode().splitlines()]
    print(values)
    # f = open("input.txt", "r")
    # values = [int(r) for r in body]
    values.sort()
    for i in range(0,len(values)-2):
        for j in range(i+1, len(values)-1):
            for k in range(j+1, len(values)):
                calced = values[i] + values[j] + values[k]
                if calced < 2020:
                    continue
                elif calced > 2020:
                    break
                else:
                    print(str(values[i]) + " * " + str(values[j]) + " * " + str(values[k]) + " = " + str((values[i]*values[j]*values[k])))
                    exit(0)


