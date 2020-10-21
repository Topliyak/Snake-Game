import pygame


class Square:
    def __init__(self):
        pass


class Snake:
    def __init__(self):
        pass


class Game:
    def __init__(self):
        pygame.init()
        self.width = 500
        self.height = 600
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake")

        self.menu()

    def menu(self):
        return

    def game(self):
        return

    def exit_game(self):
        return


if __name__ == "__main__":
    game = Game()
