import pygame
import serial
import time

# Serial port settings
SERIAL_PORT = 'COM3'  # Change this to your serial port
BAUD_RATE = 9600

# Initialize Pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Servo Control")

# Connect to Arduino
try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    print("Connected to Arduino")
except serial.SerialException:
    print("Failed to connect to Arduino")
    exit()

# Function to map mouse position to servo angles
def map_mouse_to_angles(mouse_pos):
    horizontal_angle = int(pygame.mouse.get_pos()[0] / SCREEN_WIDTH * 180)
    vertical_angle = int(pygame.mouse.get_pos()[1] / SCREEN_HEIGHT * 180)
    return horizontal_angle, vertical_angle

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Read mouse position and map it to servo angles
    horizontal_angle, vertical_angle = map_mouse_to_angles(pygame.mouse.get_pos())

    # Send servo angles to Arduino
    ser.write(f"{horizontal_angle},{vertical_angle}\n".encode())

    # Wait for a short time to prevent overwhelming Arduino
    time.sleep(0.05)

    # Clear screen
    screen.fill((255, 255, 255))

    # Draw a circle representing the mouse position
    pygame.draw.circle(screen, (255, 0, 0), pygame.mouse.get_pos(), 5)

    # Update the display
    pygame.display.flip()

# Close serial connection and quit Pygame
ser.close()
pygame.quit()
