import subprocess
import sys, tty, termios, fcntl
import os


class Program:
    def __init__(self):
        subprocess.run(["tput", "smcup"])
        # ANSI.hide_cursor()
        ANSI.clear_screen()

    def quit(self):
        print("\033[0m")
        # ANSI.clear_screen()
        ANSI.show_cursor()
        subprocess.run(["tput", "rmcup"])

    def wait_key(self, k):
        """ wait untill the given key is pressed """
        while True:
            key = Utils.getch()
            if key == k or key == 3:
                return
    
    def fill(self, character):
        ANSI.clear_screen()
        columns, rows = os.get_terminal_size()
        for row in range(rows):
            print(character * columns)

class ANSI:
    ESC = "\033"
    CSI = f"{ESC}["

    def clear_screen():
        print(f"{ANSI.CSI}2J{ANSI.CSI}H")

    def move_cursor(row, column):
        print(f"{ANSI.CSI}{row};{column}H", end="")

    def scroll_up(n):
        print(f"{ANSI.CSI}{n}T")

    def hide_cursor():
        print(f"{ANSI.CSI}?25l", end="")

    def show_cursor():
        print(f"{ANSI.CSI}?25h", end="")


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

