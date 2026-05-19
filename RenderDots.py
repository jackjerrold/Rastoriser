from PIL import Image
import numpy as np

HEIGHT = 16
WIDTH = 16

points = [
    [0,0],
    [0,1],
    [0,-1],
    [1,0],
    [-1,0]
    ]

def px2worldSpace(point):
    point[0] = int(HEIGHT/2) + (point[0] * k)
    point[1] = int(WIDTH/2) + (point[1] * -k)
    return point

def DrawPoints(points):

    img = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)

    for i in points:
        i = px2worldSpace(i)
        img[i[1],i[0]] = [255,255,255]

    return(img)

def SaveBitmap(img, filename):
    HEIGHT = len(img)
    WIDTH = len(img[0])

    image = Image.new("RGB", (WIDTH, HEIGHT))

    for y in range(HEIGHT):
        for x in range(WIDTH):
            image.putpixel((x, y), tuple(img[y][x]))

    image.save(filename)

img = DrawPoints(points)
SaveBitmap(img, "RenderdDots.png")
print("Complete.")