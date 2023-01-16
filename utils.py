import time


def log(message):
    print(time.strftime('%Y-%m-%d %H:%M:%S') + " - " + message)


def wait(count):
    print("Waiting..(" + str(count) + "): 0", end="\r")
    for x in range(1, count + 1):
        time.sleep(1)
        print("Waiting..(" + str(count) + "): " + str(x), end="\r")
    log("Time up")
