from PIL import Image
from math import pi, log, exp
import numpy as np

def average_blur(img, r):
    w, h = img.size
    a = np.array(img.getdata(), dtype=np.uint8).reshape(h, w)
    b = np.zeros((h,w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            s = a[i,j]+a[i-1,j]+a[i-2,j]
            
            # цикл по квадрату ±r?
                    
            b[i,j] = s / (2*r+1)**2
    return Image.fromarray(b)





img = Image.open('darwin.png')
img.load()

print("Image size is", img.size)
print("Image mode is", img.mode)

a = np.array(img, dtype=np.uint8).reshape(img.size[::-1])

blur_np(a,16).show()