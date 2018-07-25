# from PIL import Image
#
# # Rename this file to be "filters.py"
# # Add commands to import modules here.
#
# # Define your load_img() function here.
# #       Parameters: The name of the file to be opened (string)
# #       Returns: The image object with the opened file.
# def load_img(filename):
#     imgObject = Image.open(filename)
#     return imgObject
#
# # Define your show_img() function here.
# #       Parameters: The image object to display.
# #       Returns: nothing.
# def show_img(imgObject):
#     imgObject.show()
#
#
# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(imgObject, newImageName): #newImageName is the name i want to give my image
    imgObject.save(filename, "jpeg")
    show_img(ImgObject)
# Define your cocoicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
obamicon()

#
from PIL import Image
path = "noise.png" # Your image path
img = Image.open(path)
members = [(0,0)] * 9
newimg = Image.new("RGB",(width,height),"white")
for i in range(1,width-1):
    for j in range(1,height-1):
        members[0] = img.getpixel((i-1,j-1))
        members[1] = img.getpixel((i-1,j))
        members[2] = img.getpixel((i-1,j+1))
        members[3] = img.getpixel((i,j-1))
        members[4] = img.getpixel((i,j))
        members[5] = img.getpixel((i,j+1))
        members[6] = img.getpixel((i+1,j-1))
        members[7] = img.getpixel((i+1,j))
        members[8] = img.getpixel((i+1,j+1))
        members.sort()
        newimg.putpixel((i,j),(members[4]))

from PIL import Image
import math
# path = "Coco.jpeg" # Your image path
# img = Image.open(path)
newimg = Image.new("RGB", (width, height), "white")
for x in range(1, width-1):  # ignore the edge pixels for simplicity (1 to width-1)
    for y in range(1, height-1): # ignore edge pixels for simplicity (1 to height-1)

        # initialise Gx to 0 and Gy to 0 for every pixel
        Gx = 0
        Gy = 0

#         # top left pixel
#         p = img.getpixel((x-1, y-1))
#         r = p[0]
#         g = p[1]
#         b = p[2]
#
#         # intensity ranges from 0 to 765 (255 * 3)
#         intensity = r + g + b
#
#         # accumulate the value into Gx, and Gy
#         Gx += -intensity
#         Gy += -intensity
#
#         # remaining left column
#         p = img.getpixel((x-1, y))
#         r = p[0]
#         g = p[1]
#         b = p[2]
#
#         Gx += -2 * (r + g + b)
#
#         p = img.getpixel((x-1, y+1))
#         r = p[0]
#         g = p[1]
#         b = p[2]
#
#         Gx += -(r + g + b)
#         Gy += (r + g + b)
#
#         # middle pixels
#         p = img.getpixel((x, y-1))
#         r = p[0]
#         g = p[1]
#         b = p[2]
#
#         Gy += -2 * (r + g + b)
#
#         p = img.getpixel((x, y+1))
#         r = p[0]
#         g = p[1]
#         b = p[2]
#
#         Gy += 2 * (r + g + b)
#
#         # right column
#         p = img.getpixel((x+1, y-1))
#         r = p[0]
#         g = p[1]
#         b = p[2]
#
#         Gx += (r + g + b)
#         Gy += -(r + g + b)
#
#         p = img.getpixel((x+1, y))
#         r = p[0]
#         g = p[1]
#         b = p[2]
#
#         Gx += 2 * (r + g + b)
#
#         p = img.getpixel((x+1, y+1))
#         r = p[0]
#         g = p[1]
#         b = p[2]
#
#         Gx += (r + g + b)
#         Gy += (r + g + b)
#
#         # calculate the length of the gradient (Pythagorean theorem)
#         length = math.sqrt((Gx * Gx) + (Gy * Gy))

        # # normalise the length of gradient to the range 0 to 255
        # length = length / 4328 * 255
        #
        # length = int(length)

        # draw the length in the edge image
        #newpixel = img.putpixel((length,length,length))
    #    newimg.putpixel((x,y),(length,length,length))




        # Create a Grayscale version of the image
def convert_grayscale(image):
  # Get size
  width, height = image.size(324, 242)

  # Create new Image and a Pixel Map
  new = create_image(width, height)
  pixels = new.load()

  # Transform to grayscale
  for i in range(width):
    for j in range(height):
      # Get Pixel
      pixel = get_pixel(image, i, j)

      # Get R, G, B values (This are int from 0 to 255)
      red =   pixel[0]
      green = pixel[1]
      blue =  pixel[2]

      # Transform to grayscale
      gray = (red * 0.299) + (green * 0.587) + (blue * 0.114)

      # Set Pixel in new image
      pixels[i, j] = (int(gray), int(gray), int(gray))

    # Return new image
    return new
