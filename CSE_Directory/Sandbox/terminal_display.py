from sys import stdout, exit
from os import get_terminal_size
import numpy
import threading
import time
import signal

def main():
    signal.signal(signal.SIGINT, quit)

    Display.set_fps(120)
    Display.start()
    time.sleep(10)
def quit(signal, frame):
    exit()

class Display:
    _render_thread = None
    _running = False

    _frame_count = 0
    _fps = 60
    _screen = None
    _changed = True
    
    def start():
        if Display._render_thread == None:
            Display._render_thread = threading.Thread(target=Display._display)
            Display._render_thread.start()

        Display._running = True
    def stop():
        Display._running = False

    def set_fps(fps):
        Display._fps = fps

    def _display():
        stdout.write('\033[?25l') # hide cursor
        stdout.flush()

        while threading.main_thread().is_alive():
            if Display._running:
                Display._render()
                Display._frame_count += 1

            time.sleep(1/Display._fps)
        
        stdout.write('\033[?25h') # show cursor
        stdout.flush()
    def _render():
        num_cols, num_rows = get_terminal_size()

        lines = [str(Display._frame_count).ljust(num_cols, '-')]*num_rows
        for i in range(len(lines)-1):
            lines[i] += '\n'
        lines = lines + ['\033[H'] 

        stdout.writelines(lines)
        stdout.flush()
        


if __name__ == '__main__':
    main()
