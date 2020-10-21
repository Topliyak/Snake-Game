import pygame


class Square:
    def __init__(self):
        pass


class Snake:
    def __init__(self):
        pass


class Button:
	def __init__(self, size, text, event):
		self.width, self.height = size
		self.text = text
		self.event = event


class Game:
    def __init__(self):
        pygame.init()
        self.width = 500
        self.height = 600
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake")

        self.menu()

    def create_one_player_game(self):
    	return

    def create_two_players_game(self):
    	return

    def menu(self):
    	button_size = (350, 50)
    	buttons = [
    		Button(button_size, '1 player', create_one_player_game), 
    		Button(button_size, '2 players', create_two_players_game), 
    		Button(button_size, 'exit', exit_game), 
    	]

    	while True:
    		isClicked = False

    		for event in pygame.events.get():
    			if event.type == pygame.QUIT:
    				self.exit_game()
    			if event.type == pygame.MOUSEBUTTONDOWN:
    				if event.button == 1:
    					isClicked = True

    		if isClicked:
    			for button in buttons:
    				pass

        return

    def game(self):
        return

    def exit_game(self):
        return


if __name__ == "__main__":
    game = Game()
