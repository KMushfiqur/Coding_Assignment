import sys

def rush(x, y):
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    for row in range(y):
        draw = ""

        for col in range(x):
            # Corners
            
            if (col == 0 and row == 0) or (col == x - 1 and row == y - 1):
                if(x == 1 or y == 1):
                    draw+= "B"
                    continue
                draw+= "A"

            elif (col == 0 and row == y-1) or (row == 0 and col == x - 1):
                if(x == 1 or y == 1):
                    draw+= "B"
                    continue
                draw += "C"
                
            # borders
            elif (row == 0 or row == y - 1 or col == 0 or col == x - 1):
                draw += "B"

            # Inside
            else:
                draw += " "

        print(draw)

###Test
##rush(5,3);
##rush(5,1);
##rush(1,3);
##rush(4,4);
##
