# import filter
#
# def main():
#     filename = input("Enter the name image you want to edit:")
#     img = filter.convert_grayscale(filename)
#     filter.pixels(img, "editedImage.jpeg")
#
# if __name__ == "__main__":
#     main()
# Imported PIL Library from PIL import Image
#
# Open an Image
# def open_image(path):
#   newImage = Image.open(path)
#   return newImage
#
# # Save Image
# def save_image(image, path):
#   image.save(path, 'png')
#
# # Create a new image with the given size
# def create_image(i, j):
#   image = Image.new("RGB", (i, j), "white")
#   return image
#
# # Get the pixel from the given image
# def get_pixel(image, i, j):
#     # Inside image bounds?
#     width, height = image.size
#     if i > width or j > height:
#       return None
#
#     # Get Pixel
#     pixel = image.getpixel((i, j))
#     return pixel
#     print(pixel)
#
# # Create a Grayscale version of the image
# def convert_grayscale(image):
#   # Get size
#   width, height = image.size
#
#   # Create new Image and a Pixel Map
#   new = create_image(width, height)
#   pixels = new.load()
#
#   # Transform to grayscale
#   for i in range(width):
#     for j in range(height):
#       # Get Pixel
#       pixel = get_pixel(image, i, j)
#
#       # Get R, G, B values (This are int from 0 to 255)
#       red =   pixel[0]
#       green = pixel[1]
#       blue =  pixel[2]
#
#       # Transform to grayscale
#       gray = (red * 0.299) + (green * 0.587) + (blue * 0.114)
#
#       # Set Pixel in new image
#       pixels[i, j] = (int(gray), int(gray), int(gray))
#
#     # Return new image
#     return new
# ------------------------------------------


from PIL import ImageFilter
im1 = Image.open("Coco.jpg")
im.show()

 sdkl a;ll;kasdlkjf ld ktn ,mc,m o do

      # Transform to grayscale
      gray = (red * 0.299) + (green * 0.587) + (blue * 0.114)

im.size(324 × 242)






#
from PIL import Image
path = "coco.jpeg" # Your image path
img = Image.open(path)
members = [(0,0)] * 9
newimg = Image.new("RGB",(width,height),"white")
for i in range(1,width-1):
