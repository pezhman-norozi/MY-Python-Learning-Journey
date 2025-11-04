from PIL import Image

img = Image.open("/Users/pezhman/Desktop/Screenshot 2025-06-04 at 1.59.04 PM.png")

for i in range(20):
    for j in range(30):
        img.putpixel((200+i , 200+j) , (0 , 0 , 255) )
        
img.show()