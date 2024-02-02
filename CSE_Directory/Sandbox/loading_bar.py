from time import sleep
from termcolor import colored
from os import get_terminal_size
from sys import stdout
import signal
import threading

def main():
    display = Terminal_Display()
    display.start()
    sleep(1)
    display.stop()
    sleep(5)
    display.start()
    sleep(100)

class Terminal_Display:
    def __init__(self):
        signal.signal(signal.SIGINT, self.quit)

        # stdout.write('\033[?25l') # delete the terminal cursor highlight
        self.frame = 0

    
    def start(self):
        self.running = True

        self.renderer = threading.Thread(target=self.__render)
        self.renderer.start()
    def __render(self):
        while self.running and threading.main_thread().is_alive():
            self.update(self.frame)
            self.frame += 1
    def stop(self):
        self.running = False
        self.renderer.join()

    def quit(self, signal, frame):
        self.stop()
        stdout.write('\033[?25h') # re-show cursor
        exit(0)





    def update(self, frame: int):
        sleep(1/60) # TODO: wait until next frame with non constant time

        self.clear()
        self.output(frame)
    def clear(self):
        stdout.write("\033[0;0H") # return to start
    def output(self, frame):
        self.display_width, self.display_height = get_terminal_size()
        s = f'({self.display_width},{self.display_height})-{frame}'
        s = s.ljust(self.display_width-len(s),'-')

        for line in range(self.display_height-1):
            stdout.write(s + '\n')


if __name__ == '__main__':
    main()
