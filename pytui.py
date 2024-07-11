import subprocess
import sys, tty, termios, fcntl

import time


class Program:
    def __init__(self):
        subprocess.run(["tput", "smcup"])

    def quit(self):
        subprocess.run(["tput", "rmcup"])

    def wait_key(self, k):
        """ wait untill the given key is pressed """
        time.sleep(1)
        while True:
            key = Utils.getch()
            if key:
                print(key)
            if key == k or key == 3:
                return

class Utils:
    def getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ord(ch)

