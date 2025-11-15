oppositeDir = {
North: South,
South: North,
East: West,
West: East
}


def setFarm():
	n = get_world_size()
	farm = []
	for _ in range(n):
		linha = []
		for _ in range(n):
			linha.append('.')
		farm.append(linha)
	return farm

def neighbors():
	dir = []
	if can_move(East):
		dir.append(East)
	if can_move(West):
		dir.append(West)
	if can_move(North):
		dir.append(North)
	if can_move(South):
		dir.append(South)
	return dir


def mark_visited(x, y):
	farm[x][y] = 'V'


def mark_dead_end(x, y):
	farm[x][y] = 'D'
	
	
def search(reset):
	if reset:
		global farm
		farm = setFarm()
	
	if get_entity_type() != Entities.Treasure and get_entity_type() != Entities.Hedge:
		return True
		
	posX, posY = get_pos_x(), get_pos_y()
	
	if get_entity_type() == Entities.Treasure:
		harvest()
		return True
		
	if farm[posX][posY] in ['V','D']:
		return False
	
	mark_visited(posX, posY)

	dirs = neighbors()
	for i in range(len(dirs)-1, 0, -1):
		j = random() * (i+1) // 1
		dirs[i], dirs[j] = dirs[j], dirs[i]
	
	for direcao in dirs:
		move(direcao)
			
		
		if search(False):
			return True
		
		move(oppositeDir[direcao])

	mark_dead_end(posX, posY)

	return False