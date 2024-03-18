import pygame
# Initialize Pygame
pygame.init()

# Set up the display window
size = (800, 600)  # Adjust the dimensions as needed
title = "My Image Display"  # Custom window title
window = pygame.display.set_mode(size)
pygame.display.set_caption(title)

# Load the image
image_path = "/home/pi/Slideshow/pic1.png"  # Replace with your image file name
image = pygame.image.load(image_path)
image_rect = image.get_rect()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Display the image
    window.blit(image, image_rect)
    pygame.display.update()

# Clean up
pygame.quit()