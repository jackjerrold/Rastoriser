from PIL import Image
import cv2
import numpy as np
import time

SPEED = 1
FRAME_COUNT = 255
FPS = 24
HEIGHT = 1028
WIDTH = 1028

video = cv2.VideoWriter(
    "output.mp4",
    cv2.VideoWriter_fourcc(*"mp4v"),
    FPS,
    (WIDTH, HEIGHT)
)

def CreateFrame(offset):

    img = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            r = int((x / (WIDTH - 1))*255) + offset
            g = int((y / (HEIGHT - 1))*255) + offset

            img[y, x] = [0, g % 256, r % 256]

    return(img)

start = time.time()
for i in range(0,FRAME_COUNT):
    img = CreateFrame(i*SPEED)
    video.write(img)
    print(f"wrote frame {i}")
video.release()
print(f"elapsed {time.time() - start}s")