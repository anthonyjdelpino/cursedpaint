import curses
from curses import wrapper

stdscr = curses.initscr()
curses.start_color()

curses.noecho()
curses.cbreak()
curses.mousemask(curses.REPORT_MOUSE_POSITION | curses.ALL_MOUSE_EVENTS)
curses.mouseinterval(1)


def main(stdscr):
    print('\033[?1003h')
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.keypad(True)
    stdscr.clear()
    stdscr.refresh()

    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(7, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    paintColor = 1

    stdscr.addstr(1,0, 'press q or click me to close', curses.color_pair(3))
    #stdscr.addstr(4,0, 'click to start drawing, r click to stop', curses.color_pair(1))
    stdscr.addstr(2,0, 'BLUE', curses.color_pair(1))
    stdscr.addstr(2,10, 'CYAN', curses.color_pair(2))
    stdscr.addstr(2,20, 'GREEN', curses.color_pair(3))
    stdscr.addstr(2,30, 'MAGENTA', curses.color_pair(4))
    stdscr.addstr(2,40, 'RED', curses.color_pair(5))
    stdscr.addstr(2,50, 'WHITE', curses.color_pair(6))
    stdscr.addstr(2,60, 'YELLOW', curses.color_pair(7))
    brushTip = '@'
    stdscr.addstr(3, 0, 'Brushes: # @ - + $ ERASER')
    stdscr.refresh()

    while True:
        event = stdscr.getch()
        if event == ord('q'): break
        if event == curses.KEY_MOUSE:
            _, mouseX, mouseY, _, mouseState = curses.getmouse()
            stdscr.addstr(4,0, '                                  ')
            stdscr.addstr(4, 0, 'Y: {} X: {} S: {}'.format(mouseY, mouseX, mouseState))
            #on mouse click(2), or mouse drag(268435456)
            if (mouseState == 2) or (mouseState == 268435456):
                if mouseY == 1 and mouseX in range(0, 28): break
                if mouseY == 2:
                    if mouseX in range(0, 5): paintColor = 1
                    elif mouseX in range(10, 15): paintColor = 2
                    elif mouseX in range(20, 27): paintColor = 3
                    elif mouseX in range(30, 38): paintColor = 4
                    elif mouseX in range(40, 44): paintColor = 5
                    elif mouseX in range(50, 56): paintColor = 6
                    elif mouseX in range(60, 67): paintColor = 7
                    stdscr.addstr(0, 15, 'COLOR', curses.color_pair(paintColor))
                    continue
                if mouseY == 3:
                    if mouseX == 9: brushTip = '#'
                    elif mouseX == 11: brushTip = '@'
                    elif mouseX == 13: brushTip = '-'
                    elif mouseX == 15: brushTip = '+'
                    elif mouseX == 17: brushTip = '$'
                    elif mouseX in range(19, 26): brushTip = ' '
                    stdscr.addch(0, 25, brushTip)
                    continue
                stdscr.addstr(0,0, '            ')
                stdscr.addstr(0, 0, 'Y: {} X: {}'.format(mouseY, mouseX))
                stdscr.addch(mouseY, mouseX, brushTip, curses.color_pair(paintColor))
                #curses.ungetch('0')
                stdscr.refresh()
    
    print('\033[?1003l')
    curses.echo()
    curses.nocbreak()
    stdscr.keypad(False)
    curses.endwin()

wrapper(main)