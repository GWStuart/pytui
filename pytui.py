import subprocess
import sys, tty, termios, fcntl
import os


class Program:
    STARTING_COLOUR = (30, 30, 30)

    def __init__(self, use_alternative_screen=True):
        if use_alternative_screen:
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
    
    def fill(self, character, fg=None, bg=None, numbered=False):
        ANSI.clear_screen()
        columns, rows = os.get_terminal_size()
        print("HIHIHI")
        for row in range(rows):
            if numbered:
                line_num = str(row)
                ANSI.print(line_num + character * (columns - len(line_num)), bg=bg, fg=fg)
            else:
                ANSI.print(character * columns, bg=bg, fg=fg)

    def write(self, text, row, column):
        ANSI.move_cursor(row, column)
        ANSI.print(text, bg=self.STARTING_COLOUR, fg=None)

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

    def print(message, bg=None, fg=None):
        if bg:
            r, g, b = bg
            print(f"{ANSI.CSI}48;2;{r};{g};{b}m", end="")
        if fg:
            r, g, b = fg
            print(f"{ANSI.CSI}38;2;{r};{g};{b}m", end="")
        print(message) # , end="")
        ANSI.clear_sgr()

    def clear_sgr():
        print(f"{ANSI.CSI}m", end="")


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

