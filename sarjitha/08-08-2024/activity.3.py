# Import necessary libraries
import cv2
import matplotlib.pyplot as plt
import imageio.v2 as imageio

# Load an image
image = cv2.imread('louts.jpg')

# Check if the image was loaded successfully
if image is None:
    print("Could not load image. Please check the file path.")
    exit()

# Convert the image from BGR (OpenCV format) to RGB (Matplotlib format)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Apply Gaussian blur to denoise
denoised_image = cv2.GaussianBlur(image_rgb, (11, 11), 0)

# Display the original and denoised images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image_rgb)
plt.axis('off')  # Hide axes

plt.subplot(1, 2, 2)
plt.title('Denoised Image')
plt.imshow(denoised_image)
plt.axis('off')

plt.show()

# Convert to grayscale
gray_image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)

# Apply histogram equalization
equalized_image = cv2.equalizeHist(gray_image)

# Display the grayscale and equalized images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Gray Image')
plt.imshow(gray_image, cmap="gray")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Equalized Image')
plt.imshow(equalized_image, cmap="gray")
plt.axis('off')

plt.show()
