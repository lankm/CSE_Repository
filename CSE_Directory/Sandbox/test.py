import curses

def main(stdscr):
    # Set up the screen
    curses.curs_set(0)  # Hide the cursor
    stdscr.clear()
    stdscr.refresh()

    # Get screen dimensions
    height, width = stdscr.getmaxyx()

    # Display a welcome message
    welcome_message = "Welcome to the Curses Example!"
    stdscr.addstr(height // 2, (width - len(welcome_message)) // 2, welcome_message, curses.A_BOLD)
    stdscr.refresh()

    # Wait for a key press
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
