# example of saving a grayscale version of a loaded image
from PIL import Image
# load the image
image = Image.open("bus.jpg")
# convert the image to grayscale
gs_image = image.convert(mode="L")
# save in jpeg format
gs_image.save("grayscale.jpg")
# load the image again and show it
image2 = Image.open("grayscale.jpg")
# show the image
image2.show()
