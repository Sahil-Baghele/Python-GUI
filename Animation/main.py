import pygame
import random
import math


pygame.init()


width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sophisticated Ball Animation")


COLORS = [
    (255, 0, 0),    
    (0, 255, 0),    
    (0, 0, 255),    
    (255, 255, 0),  
    (255, 0, 255),  
    (0, 255, 255),  
]

# Ball class
class Ball:
    def __init__(self):
        self.radius = random.randint(10, 30)
        self.x = random.randint(self.radius, width - self.radius)
        self.y = random.randint(self.radius, height - self.radius)
        self.dx = random.uniform(-2, 2)
        self.dy = random.uniform(-2, 2)
        self.color = random.choice(COLORS)
        self.phase = random.uniform(0, 2 * math.pi)

    def move(self):
        self.x += self.dx
        self.y += self.dy

       
       
        if self.x - self.radius <= 0 or self.x + self.radius >= width:
            self.dx *= -1
        if self.y - self.radius <= 0 or self.y + self.radius >= height:
            self.dy *= -1

        
        
        self.phase += 0.1
        scale = (math.sin(self.phase) + 2) / 3  # Scale between 0.33 and 1
        current_radius = int(self.radius * scale)


        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), current_radius)



balls = [Ball() for _ in range(20)]


running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill((0, 0, 0))

    
    
    for ball in balls:
        ball.move()


    pygame.display.flip()

   
   
    clock.tick(60)


pygame.quit()

