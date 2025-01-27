import pygame

# base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sup-classes must override
        pass

    def update(self, dt):
        # sup-classes must override
        pass

    def collision(self, circle):
        distance = self.position.distance_to(circle.position)
        if distance < self.radius + circle.radius:
            return True
        return False

