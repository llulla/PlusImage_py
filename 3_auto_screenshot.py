import time
from PIL import ImageGrab

time.sleep(5)

for i in range(1,31):
    img = ImageGrab.grab()
    img.save("image{}.png".format(i))
    time.sleep(10)