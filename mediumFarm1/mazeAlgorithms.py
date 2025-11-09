inverso = {
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
	if can_move(North):
		dir.append(North)
	if can_move(East):
		dir.append(East)
	if can_move(South):
		dir.append(South)
	if can_move(West):
		dir.append(West)
	return dir


def mark_visited(x, y):
	farm[x][y] = 'V'


def mark_dead_end(x, y):
	farm[x][y] = 'D'
	
	
def busca(reset):
	if reset:
		global farm
		farm = setFarm()
		
	posX, posY = get_pos_x(), get_pos_y()
	
	if get_entity_type() == Entities.Treasure:
		harvest()
		return True
		
	if farm[posX][posY] in ['V','D']:
		return False
	
	mark_visited(posX, posY)

	dirs = neighbors()
	
	for direcao in dirs:
		move(direcao)
			
		
		if busca(False):
			return True
		
		move(inverso[direcao])

	mark_dead_end(posX, posY)

	return False