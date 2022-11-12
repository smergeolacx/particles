import pygame,random
from sys import exit

class ParticlePrinciple:
    def __init__(self):
        self.particle = []

    def add_part(self):
        px, py = pygame.mouse.get_pos()
        radius = 10
        dirx, diry = random.randint(-5,5), random.randint(-5,5)
        particle_circle = [[px,py],radius,[dirx,diry]]
        self.particle.append(particle_circle)


    def emit(self):
        if self.particle:
            self.del_part()
            for part in self.particle:
                part[0][0] += part[2][0]
                part[0][1] += part[2][1]
                part[1] -= 0.5
                pygame.draw.circle(screen,"white",part[0],part[1])

    def del_part(self):
        particle_copy = [p for p in self.particle if p[1] > 0]
        self.particle = particle_copy


width, height = 500, 500
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))

part_event = pygame.USEREVENT + 1
pygame.time.set_timer(part_event, 50)
part1 = ParticlePrinciple()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == part_event:
            part1.add_part()

    screen.fill('black')
    part1.emit()
    clock.tick(60)
    pygame.display.update()