from PIL import Image
import numpy as np
import vectors

HEIGHT = 520
WIDTH = 520
WHITE = [255,255,255]
BLUE = [3,119,252]
RED = [252,3,86]

px2wsRatio = 7

def px2worldSpace(point):
    point[0] = int(HEIGHT/2) + (point[0])
    point[1] = int(WIDTH/2) - (point[1])
    return point

def instantiateImage():
    img = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
    return img

def DrawPoint(image, point, color):

    point = px2worldSpace(point)
    if abs(point[0]) < HEIGHT and abs(point[1]) < WIDTH:
        image[point[1],point[0]] = color
        return(image)
    else:
        print(f"point: {point} off-screen")
        return(image)
    

def vectorMult(vect, mult):
    result = []
    for i in vect:
        result.append(i*mult)
    return result
    
def DrawLine(image, ends, color):#switch to brensehams lines
    if len(ends) != 2:
        print("Line end count is not 2.")
        return

    interpolated = []

    dx = ends[1][1] - ends[0][1]
    dy = ends[1][0] - ends[0][0]

    if abs(dx) < abs(dy):
        m = dx/dy
        c = -ends[0][0]*m + ends[0][1]

        for x in range(ends[0][0], ends[1][0] + 1, vectors.Normalise(ends[1][0] - ends[0][0])):
            interpolated.append([x,round(m*x + c)])
    else:
        m = dy/dx
        c = -ends[0][1]*m + ends[0][0]

        for y in range(ends[0][1], ends[1][1] + 1, vectors.Normalise(ends[1][1] - ends[0][1])):
            interpolated.append([round(m*y + c),y])

    for point in interpolated:
        DrawPoint(image, point, color)

def DrawTri(image, vertex, color, fill):
    if len(vertex) != 3:
        print("Triangle vertex count is not 3.")
        return
    
    vertex[0] = vectorMult(vertex[0],px2wsRatio)
    vertex[1] = vectorMult(vertex[1],px2wsRatio)
    vertex[2] = vectorMult(vertex[2],px2wsRatio)
    
    if fill == True:
        
        vec1 = vectors.DirVector(vertex[0],vertex[1]).perp()
        vec2 = vectors.DirVector(vertex[1],vertex[2]).perp()
        vec3 = vectors.DirVector(vertex[2],vertex[0]).perp()
        vecs = [vec1,vec2,vec3]

        for y in range(HEIGHT):
            for x in range(WIDTH):

                p = [int(x-WIDTH/2), int(y-HEIGHT/2)]
                contained = True
                for i in range(0,3):
                    vec4 = vectors.DirVector(vertex[i],p)
                    if vectors.DotProd(vecs[i],vec4) <= 0:
                        contained = False
                        break

                if contained:
                    DrawPoint(image, p, color)
    
        DrawLine(image, [vertex[0],vertex[1]], WHITE)
        DrawLine(image, [vertex[1],vertex[2]], WHITE)
        DrawLine(image, [vertex[2],vertex[0]], WHITE)

    else:
        DrawLine(image, [vertex[0],vertex[1]], color)
        DrawLine(image, [vertex[1],vertex[2]], color)
        DrawLine(image, [vertex[2],vertex[0]], color)
    

def SaveBitmap(img, filename):
    HEIGHT = len(img)
    WIDTH = len(img[0])

    image = Image.new("RGB", (WIDTH, HEIGHT))

    for y in range(HEIGHT):
        for x in range(WIDTH):
            image.putpixel((x, y), tuple(img[y][x]))

    image.save(filename)


img = instantiateImage()
DrawTri(img, [[-10,-15],[-8,13],[14,12]], BLUE, True)
SaveBitmap(img, "2DRender.png")
print("Complete.")