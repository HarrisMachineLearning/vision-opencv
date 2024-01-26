import cv2
import numpy as np

# Load the image
# image_name = "IMG_1819_b"
image_name = "aberdine"
image_type = ".png"
image_path = f'/workspace/python-flask-api-tutorial/images/{image_name}{image_type}'
image = cv2.imread(image_path)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to the grayscale image
blurred = cv2.GaussianBlur(gray, (9, 9), 0)

edged = cv2.Canny(blurred, 50, 150)
# Apply Hough Circle Transform to detect circles
detected_circles = cv2.HoughCircles(edged, cv2.HOUGH_GRADIENT, dp=1, minDist=400,
                                    param1=50, param2=30, minRadius=0, maxRadius=0)

# Ensure at least some circles were found
if detected_circles is not None:
    # Convert the circle parameters to integers
    detected_circles = np.round(detected_circles[0, :]).astype("int")

    # Loop over the detected circles and draw them on the original image
    for (x, y, r) in detected_circles:
        print(r)
        # if(r > 590 and r < 650):
        if(r > 200):
            # Draw the outer circle in red (BGR format)
            cv2.circle(image, (x, y), r, (0, 0, 255), 3)
            # Draw the center of the circle in green
            cv2.circle(image, (x, y), 2, (0, 255, 0), 3)

# Save the output image with the detected circles
output_path = f'/workspace/python-flask-api-tutorial/images/rendered/{image_name}_circle_detected_output.png'
cv2.imwrite(output_path, image)

output_path

# # Function to calculate circularity
# def calculate_circularity(contour):
#     perimeter = cv2.arcLength(contour, True)
#     area = cv2.contourArea(contour)
#     if perimeter == 0:
#         return 0
#     circularity = 4 * np.pi * (area / (perimeter ** 2))
#     return circularity

# # Find contours in the image
# contours, _ = cv2.findContours(blurred_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # Assuming the largest contour corresponds to the fan frame
# # Sort the contours based on area and grab the largest one
# sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)
# fan_frame_contour = sorted_contours[0]

# # Calculate the circularity of the fan frame
# fan_frame_circularity = calculate_circularity(fan_frame_contour)

# # Convert circularity to percentage for better readability
# circularity_percentage = fan_frame_circularity * 100
# circularity_percentage


# # Since the previous cell didn't return any output, let's try detecting circles in the new image again
# # Also, we will reapply the contour detection to calculate the circularity

# # Apply Gaussian blur to the new image to reduce noise and improve edge detection
# new_blurred = cv2.GaussianBlur(image, (9, 9), 0)

# # Apply edge detection to the new image
# edges = cv2.Canny(new_blurred, 50, 150)

# # Find contours in the edge-detected image
# new_contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # Assuming the largest contour corresponds to the fan frame
# new_contours = sorted(new_contours, key=cv2.contourArea, reverse=True)
# if new_contours:
#     # Calculate the circularity of the largest contour (presumably the fan frame)
#     new_circularity = calculate_circularity(new_contours[0])
# else:
#     new_circularity = 0  # No contours found

# # Convert new circularity to percentage for better readability
# new_circularity_percentage = new_circularity * 100
# print(new_circularity_percentage)
