import subprocess
import platform
import sys
import time

def ping(host):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', host]
    return subprocess.call(command) == 0


def main():
    while True:
        time.sleep(1)
        host = sys.argv[1] if len(sys.argv) == 2 else f'{ip}'
        result = ping(host)
        if result:
            print(f'{host} is accessible')
        else:
            print(f'{host} is not accessible')


if __name__ == "__main__":
    ip = "1.1.1.1"
    main()
