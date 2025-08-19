import os
import platform
if "microsoft" in platform.uname().release.lower():
    os.environ['SDL_AUDIODRIVER'] = 'dummy'
import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import AsteroidField
import sys
from Shot import Shot
from pathlib import Path
import os

def resource_path(relative_path):
    """Return path to resource, works for dev and for PyInstaller."""
    try:
        base_path = sys._MEIPASS  # when bundled by PyInstaller / auto-py-to-exe
    except AttributeError:
        # fallback to the folder where this script lives (better than cwd)
        base_path = Path(__file__).resolve().parent
    return os.path.join(base_path, relative_path)



pygame.mixer.pre_init(44100, -16, 2, 512)
MUSIC_PATH = resource_path("Punkrocker.ogg")
pygame.init()
pygame.mixer.init()

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF)
    pygame.mixer.music.load((MUSIC_PATH))
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(loops=-1, start=0.0, fade_ms=2800)
    font_score = pygame.font.SysFont("verdana", 45, bold=False)
    font_game_over = pygame.font.SysFont("verdana", 100, bold=True)
    pygame.display.set_caption("Asteroids! by faraz")
    clock = pygame.time.Clock()
    running = True
    dt = 0
    score = 0
    score_color = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    print("Starting Asteroids!")
    print(
f"Screen width: {SCREEN_WIDTH}\n"
f"Screen height: {SCREEN_HEIGHT}"
    )
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        updatable.update(dt)
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        score_text = font_score.render("Score: ", True, "cyan")
        score_value_text = font_score.render(str(score), True, get_score_color(score))  # dynamic color
        score_text_rect = score_text.get_rect()
        score_value_rect = score_value_text.get_rect()
        total_width = score_text_rect.width + score_value_rect.width
        x_center = SCREEN_WIDTH // 2
        y_bottom = SCREEN_HEIGHT - 10
        score_text_rect.topleft = (x_center - total_width // 2, y_bottom - score_text_rect.height)
        score_value_rect.topleft = (score_text_rect.topright[0], y_bottom - score_value_rect.height)
        screen.blit(score_text, score_text_rect)
        screen.blit(score_value_text, score_value_rect)
        pygame.display.flip()
        dt = clock.tick_busy_loop(60)/1000
        for asteroid in asteroids:
            if player.Collision(asteroid):
                player.kill()
                text = font_game_over.render("GAME OVER", True, get_score_color(score))
                rect = text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
                screen.blit(text, rect)
                pygame.display.flip()
                pygame.mixer.music.fadeout(600)
                pygame.mixer.music.stop()
                pygame.time.wait(1000)
                sys.exit(
                    f"Game over!\n"
                    f"Score = {score}"
                )
            for bullet in shots:
                if bullet.Collision(asteroid):
                    score += 1
                    asteroid.split()
                    bullet.kill()

    pygame.quit()
    print(
        f"Game over!\n"
        f"Score = {score}"
    )

def get_score_color(score):
    if 0 <= score <= 10:
        return "cyan"
    if 10 < score <= 30:
        return "yellow"
    if 30 < score <= 50:
        return "red"
    if 50 < score <= 90:
        return "violet"
    if 90 < score:
        return "purple"
    




if __name__ == "__main__":
    main()
