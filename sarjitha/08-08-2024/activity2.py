import cv2
import matplotlib.pyplot as plt
from PIL import Image
import imageio

# Load an image using OpenCV
image_path = "rose.jpg"
image_cv2 = cv2.imread(image_path)

# Convert the image from BGR to RGB
image_cv2_rgb = cv2.cvtColor(image_cv2, cv2.COLOR_BGR2RGB)

# Display the image loaded with OpenCV
plt.imshow(image_cv2_rgb)
plt.title('Image loaded with OpenCV')
plt.axis('off')  # Hide axes
plt.show()

# Load an image using PIL
image_pil = Image.open(image_path)

# Display the image loaded with PIL
plt.imshow(image_pil)
plt.title('Image loaded with PIL')
plt.axis('off')
plt.show()

# Load an image using imageio
image_imageio = imageio.imread(image_path)

# Display the image loaded with imageio
plt.imshow(image_imageio)
plt.title('Image loaded with imageio')
plt.axis('off')
plt.show()

# PNG image path
image_path_png = "sun.png"
image_path_jpg = ".jpg"

# OpenCV: Load and display a PNG image
image_cv2_png = cv2.imread(image_path_png)
image_cv2_png_rgb = cv2.cvtColor(image_cv2_png, cv2.COLOR_BGR2RGB)
plt.imshow(image_cv2_png_rgb)
plt.title('PNG loaded with OpenCV')
plt.axis('off')
plt.show()

# PIL: Load and display the same PNG image
image_pil_png = Image.open(image_path_png)
plt.imshow(image_pil_png)
plt.title('PNG loaded with PIL')
plt.axis('off')
plt.show()

# imageio: Load and display the same PNG image
image_imageio_png = imageio.imread(image_path_png)
plt.imshow(image_imageio_png)
plt.title('PNG loaded with imageio')
plt.axis('off')
plt.show()
