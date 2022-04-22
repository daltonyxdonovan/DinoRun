
#WORKING GRAVITY WOOOOOOOOOOOO

	#collision logic for my dino, and landing checks
	if playerDino.rect.y >= 580:
		onground = True
		v = 6
		m = 4
		playerDino.rect.y = 580

	#actual fucking GRAVITY MOTHERFUCKER
	if onground == True:
		if keys[pygame.K_SPACE]:
			onground = False
	if onground == False:
		F =(1/2)*m*(v**2)
		playerDino.rect.y -= F
		v = v - 1
		if v < 0:
			m =-1
