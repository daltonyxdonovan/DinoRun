import pygame, sys
GREEN = (0,255,0)

def load_image(name):
    image = pygame.image.load(name)
    return image

class Dino(pygame.sprite.Sprite):
	def __init__(self, color, width, height, speed, velocity, onGround):
		super().__init__()
		self.color = color
		self.speed = speed
		self.height = height
		self.width = width
		self.velocity = velocity
		self.onGround = onGround
		self.images = []
		self.images.append(load_image('dino.png'))
		self.images.append(load_image('dino2.png'))
		self.index = 0
		self.image = self.images[self.index]
		self.rect = pygame.Rect(5, 5, 130, 130)
		
	def update(self):
		count=0
		count += 1
		if count >= 20:
			self.index += 1
			count = 0
		if self.index > 1:
			self.index = 0
			
		self.image = self.images[self.index]
		
		def moveForward(self, pixels):
			self.rect.y -= pixels
	
		def moveBackward(self, pixels):
			self.rect.y += pixels

		
def main():
	pygame.init()
	screen = pygame.display.set_mode((800, 800))
	my_sprite = TestSprite()
	my_group = pygame.sprite.Group(my_sprite)
	
	while True:
		event = pygame.event.poll()
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit(0)

		my_group.update()
		my_group.draw(screen)
		pygame.display.flip()

		

	if __name__ == '__main__':
		main()
