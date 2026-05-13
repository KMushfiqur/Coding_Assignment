import sys

def rush(x, y):
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    for row in range(y):
        draw = ""

        for col in range(x):
            # Corners
            if (row == 0 and col == 0) or (row == y - 1 and col == 0)  \
               or (row == 0 and col == x - 1) or (row == y - 1 and col == x - 1):
                draw += "o"

            # Top and bottom borders
            elif row == 0 or row == y - 1:
                draw += "-"

            # Left and right borders
            elif col == 0 or col == x - 1:
                draw += "|"

            # Inside
            else:
                draw += " "

        print(draw)

#Test
##rush(5,3);
##rush(1,1);
##rush(1,3);
