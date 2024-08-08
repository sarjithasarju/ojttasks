# Load the necessary libraries
import cv2
import matplotlib.pyplot as plt

# Load an image
image = cv2.imread('rose.jpeg')

# Check if the image was loaded successfully
if image is None:
    print("Could not read the image")
    exit()

# Convert the image from BGR (OpenCV format) to RGB (Matplotlib format)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Resize the image to 125x128 pixels
resized_image = cv2.resize(image_rgb, (125, 128))

# Display the original and resized images
plt.figure(figsize=(10, 5))

# Original Image
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image_rgb)
plt.axis('off')

# Resized Image
plt.subplot(1, 2, 2)
plt.title('Resized Image (125x128)')
plt.imshow(resized_image)
plt.axis('off')

plt.show()

# Save or display the resized image
# cv2.imwrite('resized_image.jpg', resized_image)

# Crop the image to a region (x, y, width, height)
cropped_image = image_rgb[50:130, 50:200]

# Display the original and cropped images
plt.figure(figsize=(10, 5))

# Original Image
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image_rgb)
plt.axis('off')

# Cropped Image
plt.subplot(1, 2, 2)
plt.title('Cropped Image')
plt.imshow(cropped_image)
plt.axis('off')

plt.show()

# Rotate the image by 45 degrees
(h, w) = image_rgb.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_image = cv2.warpAffine(image_rgb, M, (w, h))

# Display the original and rotated images
plt.figure(figsize=(10, 5))

# Original Image
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image_rgb)
plt.axis('off')

# Rotated Image
plt.subplot(1, 2, 2)
plt.title('Rotated Image')
plt.imshow(rotated_image)
plt.axis('off')

plt.show()
