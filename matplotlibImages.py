from matplotlib import image
from matplotlib import pyplot

data = image.imread('Capture6.jpg')

print(data.dtype)
print(data.shape)

pyplot.imshow(data)
pyplot.show()