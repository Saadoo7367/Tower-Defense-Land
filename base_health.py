import pygame

class BaseHealth:
    def __init__(self, max_health, screen):
        self.max_health = max_health
        self.current_health = max_health
        self.screen = screen
        self.health_bar_image = pygame.image.load("baseHealthBG.png")

    def draw_health_bar(self):
        self.screen.blit(self.health_bar_image, (0, 0))
        text_surface = pygame.font.Font(None, 36).render(f"{self.current_health}/{self.max_health}", True, (255, 255, 255))
        self.screen.blit(text_surface, (50, 5))

    def take_damage(self, damage):
        self.current_health -= damage
        if self.current_health < 0:
            self.current_health = 0

        self.draw_health_bar()
        return self.current_health