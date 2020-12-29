import curses
from curses import wrapper

stdscr = curses.initscr()
curses.start_color()

curses.noecho()
curses.cbreak()
curses.mousemask(1)
curses.mouseinterval(0)


def main(stdscr):
    stdscr.nodelay(True)
    stdscr.keypad(True)
    stdscr.clear()
    stdscr.refresh()

    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    paintColor = 1

    stdscr.addstr(1,0, 'press q or click me to close', curses.color_pair(2))
    stdscr.addstr(2,0, 'RED', curses.color_pair(1))
    stdscr.addstr(2,10, 'GREEN', curses.color_pair(2))
    stdscr.addstr(2,20, 'BLUE', curses.color_pair(3))
    brushTip = '@'
    stdscr.addstr(3, 0, 'Brushes: # @ - + $')
    stdscr.refresh()

    

    while True:
        event = stdscr.getch()
        if event == ord('q'): break
        if event == curses.KEY_MOUSE:
            _, mouseX, mouseY, _, _ = curses.getmouse()
            if mouseY == 1 and mouseX in range(0, 28): break
            if mouseY == 2:
                if mouseX in range(0, 3): paintColor = 1
                elif mouseX in range(10, 15): paintColor = 2
                elif mouseX in range(20, 24): paintColor = 3
                stdscr.addstr(0, 15, 'COLOR', curses.color_pair(paintColor))
                continue
            if mouseY == 3:
                if mouseX == 9: brushTip = '#'
                elif mouseX == 11: brushTip = '@'
                elif mouseX == 13: brushTip = '-'
                elif mouseX == 15: brushTip = '+'
                elif mouseX == 17: brushTip = '$'
                stdscr.addch(0, 25, brushTip)
                continue
            stdscr.addstr(0,0, '            ')
            stdscr.addstr(0, 0, 'Y: {} X: {}'.format(mouseY, mouseX))
            stdscr.addch(mouseY, mouseX, brushTip, curses.color_pair(paintColor))
            stdscr.refresh()

    curses.echo()
    curses.nocbreak()
    stdscr.keypad(False)
    curses.endwin()

wrapper(main)