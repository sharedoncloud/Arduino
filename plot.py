import numpy as np
import matplotlib.pyplot as plt

# Robot parameters
L1 = 5  # Length of the first arm
L2 = 7  # Length of the second arm
base_offset = 3  # Offset of the base between arms

# Function to calculate end-effector position for left arm
def calculate_left_end_effector_position(theta1, theta2):
    theta1_rad = np.radians(theta1)
    theta2_rad = np.radians(theta2)
    x = L1 * np.cos(theta1_rad) + L2 * np.cos(theta1_rad + theta2_rad)
    y = L1 * np.sin(theta1_rad) + L2 * np.sin(theta1_rad + theta2_rad)
    return x, y

# Function to calculate end-effector position for right arm
def calculate_right_end_effector_position(theta1, theta2):
    theta1_rad = np.radians(theta1)
    theta2_rad = np.radians(theta2)
    x = L1 * np.cos(theta1_rad) - L2 * np.cos(theta1_rad + theta2_rad)
    y = L1 * np.sin(theta1_rad) - L2 * np.sin(theta1_rad + theta2_rad)
    return x, y

# Example joint angles
theta1 = 45  # Example value for theta1 in degrees
theta2 = 30  # Example value for theta2 in degrees

# Calculate end-effector positions for left and right arms
left_x_end, left_y_end = calculate_left_end_effector_position(theta1, theta2)
right_x_end, right_y_end = calculate_right_end_effector_position(theta1, theta2)


x1, y1 = -base_offset, 0  
x2, y2 = -base_offset, L1  

plt.plot([x1,x2], [y1,y2], 'r-')  

x1, y1 = -base_offset, L1
x2, y2 = -base_offset, L1 + L2  

plt.plot([x1,x2], [y1,y2], 'b-')  

x1, y1 = base_offset, 0
x2, y2 = base_offset, L1  

plt.plot([x1,x2], [y1,y2], 'r-')  
x1, y1 = base_offset, L1
x2, y2 = base_offset, L1 + L2  

plt.plot([x1,x2], [y1,y2], 'g-')  


plt.xlabel('X')
plt.ylabel('Y')
plt.title('Draw a Line')
plt.grid(True)
plt.show()

x_start, y_start = 0, 0
angle_degrees = 45  # Angle relative to the x-axis

# Define the length of the line
line_length = 1.5

# Convert angle from degrees to radians
angle_radians = np.radians(angle_degrees)

# Calculate the end point (x_end, y_end) using trigonometry
x_end = x_start + line_length * np.cos(angle_radians)
y_end = y_start + line_length * np.sin(angle_radians)
