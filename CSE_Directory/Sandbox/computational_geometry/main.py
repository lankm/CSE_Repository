import pygame
import sys

def main():
    pygame.init()

    # Set up display
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Simulation Example")

    # Simulation variables
    simulation_objects = [{'x': 50, 'y': 50, 'radius': 20, 'color': (255, 0, 0)}]

    # Main simulation loop
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update simulation logic here

        # Draw simulation objects
        screen.fill((255, 255, 255))  # White background
        for obj in simulation_objects:
            pygame.draw.circle(screen, obj['color'], (obj['x'], obj['y']), obj['radius'])
            obj['x'] += 1

        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)


if __name__ == '__main__':
    main()