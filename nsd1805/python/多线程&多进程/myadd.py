import time

def add():
    result = 0
    for i in range(1, 50000001):
        result += i
    print(result)

if __name__ == '__main__':
    start = time.time()
    add()
    add()
    end = time.time()
    print(end - start)
