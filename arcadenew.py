import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_TITLE = "ARCADE MODULE"
CHARACTER_SCALING = 1
TILE_SCALING = .5
COIN_SCALING = .5


class Game(arcade.Window):
	def __init__(self):
		super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
		self.cactus_list = None
		self.player_list = None
		self.player_sprite = None
		arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
	def setup(self):
		self.player_list = arcade.SpriteList()
		self.cactus_list = arcade.SpriteList()
		image_source = "birdo3.png"
		self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
		self.player_sprite.center_x = 64
		self.player_sprite.center_y = 128
		self.player_list.append(self.player_sprite)
		for x in range(0,1250,64):
			cactus = arcade.Sprite("cactus.png", TILE_SCALING)
			cactus.center_x = x
			cactus.center_y = 32
			self.cactus_list.append(cactus)
		coordinate_list = [[512, 96], [256, 96], [768, 96]]
		for coordinate in coordinate_list:
			cactus = arcade.Sprite("cactus.png", TILE_SCALING)
			cactus.position = coordinate
			self.cactus_list.append(cactus)
	def on_draw(self):
		arcade.start_render()
		self.cactus_list.draw()
		
def main():
	window = Game()
	window.setup()
	arcade.run
	
if __name__ == "__main__":
	main()
