import pygame
import environment


def mainGUI(fps, scene):
    pygame.init()
    done = False
    clock = pygame.time.Clock()

    while not done:
        scene.process_input()
        scene.update()
        scene.render()
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()


if __name__ == "__main__":
    mainGUI(60,environment.Environment())
