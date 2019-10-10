from concurrent.futures import ProcessPoolExecutor
from time import sleep


def process(*args):
    result = args# 입력받은 인자들을 처리한다...
    sleep(1)
    print(result)


def collect_arguments():
    pass


def main():
    with ProcessPoolExecutor(max_workers=4) as exe:
        while True:
            cont, x = collect_arguments()
            if not cont:
                break
            if x:
                exe.submit(process, *x)
            else:
                sleep(0.1)
            exe.shutdown(wait=True)


if __name__ == "__main__":
    main()
