from PIL import Image

def CreateTestImg():
    HEIGHT = 64
    WIDTH = 64

    img = [[[0, 0, 0] for x in range(WIDTH)] for y in range(HEIGHT)]

    for y in range(HEIGHT):
        for x in range(WIDTH):
            r = int((x / (WIDTH - 1))*255)
            g = int((y / (HEIGHT - 1))*255)

            img[y][x] = [r, g, 0]

    return(img)

def SaveBitmap(img, filename):
    HEIGHT = len(img)
    WIDTH = len(img[0])

    image = Image.new("RGB", (WIDTH, HEIGHT))

    for y in range(HEIGHT):
        for x in range(WIDTH):
            image.putpixel((x, y), tuple(img[y][x]))

    image.save(filename)


img = CreateTestImg()
SaveBitmap(img, "output.png")