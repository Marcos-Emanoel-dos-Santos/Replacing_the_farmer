def mv(area_length, area_height):
	limit_x = get_pos_x() == area_length
	limit_y = get_pos_y() == area_height
	
	if limit_y and limit_x:
		for _ in range(area_height):
			move(South)
		for _ in range(area_length):
			move(West)
		return
	
	if limit_x:
		move(North)
		for _ in range(area_length):
			move(West)

	move(East)
	
def go_to(x, y):
	while x != get_pos_x():
		if x < get_pos_x():
			move(West)
		elif x > get_pos_x():
			move(East)
			
	while y != get_pos_y():
		if y < get_pos_y():
			move(South)
		elif y > get_pos_y():
			move(North)