import time

def draw_square(size):
    for i in range(size):
        print(' * ' * size)
    time.sleep(2)
draw_square(10)
