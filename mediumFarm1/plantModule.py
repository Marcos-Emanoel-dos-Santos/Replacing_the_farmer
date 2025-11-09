import moveModule
import mazeAlgorithms

def soilProcedure():
	if get_ground_type() == Grounds.Grassland:
		till()



def soilProcedure():
	if get_ground_type() == Grounds.Grassland:
		till()


def water_crop(crop, crop_to_water):
	if crop_to_water == crop or crop_to_water == 'All':
		if get_water() < 0.2:
			while get_water() < 0.7:
				use_item(Items.Water)



def drone_ajudante():
	while True:
		if get_water() < 0.2:
			while get_water() < 0.7:
				use_item(Items.Water)
		moveModule.mv(get_world_size() - 1, get_world_size()-1)
				
def fertilize_crop(crop, crop_to_fertilize):
	if crop_to_fertilize == 'None':
		return
	if crop_to_fertilize == crop or crop_to_fertilize == 'All':
		while not can_harvest() and not Entities.Dead_Pumpkin:
			use_item(Items.Fertilizer)


def verifyPumpkin():
	while get_entity_type() == Entities.Dead_Pumpkin:
		plant(Entities.Pumpkin)


def safePlant(crop, c_t_w, c_t_f):
	if can_harvest():
		harvest()
		
	
	if crop in {'g', Entities.Grass, 'hay'}:
		plant(Entities.Grass)
		
	elif crop in {'b', Entities.Bush, 'bush'}:
		plant(Entities.Bush)
		
	elif crop in {'c', Entities.Carrot, 'carrot'}:
		soilProcedure()
		plant(Entities.Carrot)
		
	elif crop in {'t', Entities.Tree, 'tree'}:
		plant(Entities.Tree)

		
	elif crop in {'p', Entities.Pumpkin, 'pumpkin'}:
		soilProcedure()
		plant(Entities.Pumpkin)
		
	elif crop in {'s', Entities.Sunflower, 'sunflower'}:
		soilProcedure()
		plant(Entities.Sunflower)
		
	elif crop in {'k', Entities.Cactus, 'cactus'}:
		soilProcedure()
		plant(Entities.Cactus)
		
	elif crop in {'T', Entities.Treasure, 'treasure'}:
		plant(Entities.Bush)
		substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
		use_item(Items.Weird_Substance, 16)
		mazeAlgorithms.busca(True)
		
		
	if spawn_drone(drone_ajudante):
		quick_print("Nan")
	fertilize_crop(crop, c_t_f)
		

def water_crop(crop, crop_to_water):
	if crop_to_water == crop or crop_to_water == 'All':
		if get_water() < 0.2:
			while get_water() < 0.7:
				use_item(Items.Water)


def drone_ajudante():
	while True:
		if get_water() < 0.2:
			while get_water() < 0.7:
				use_item(Items.Water)
		moveModule.mv(get_world_size() - 1, get_world_size()-1)
				
def fertilize_crop(crop, crop_to_fertilize):
	if crop_to_fertilize == 'None':
		return
	if crop_to_fertilize == crop or crop_to_fertilize == 'All':
		while not can_harvest() and not Entities.Dead_Pumpkin:
			use_item(Items.Fertilizer)


def verifyPumpkin():
	while get_entity_type() == Entities.Dead_Pumpkin:
		plant(Entities.Pumpkin)


def safePlant(crop, c_t_w, c_t_f):
	if can_harvest():
		harvest()
		
	
	if crop in {'g', Entities.Grass, 'hay'}:
		plant(Entities.Grass)
		
	elif crop in {'b', Entities.Bush, 'bush'}:
		plant(Entities.Bush)
		
	elif crop in {'c', Entities.Carrot, 'carrot'}:
		soilProcedure()
		plant(Entities.Carrot)
		
	elif crop in {'t', Entities.Tree, 'tree'}:
		plant(Entities.Tree)

		
	elif crop in {'p', Entities.Pumpkin, 'pumpkin'}:
		soilProcedure()
		plant(Entities.Pumpkin)
		
	elif crop in {'s', Entities.Sunflower, 'sunflower'}:
		soilProcedure()
		plant(Entities.Sunflower)
		
	elif crop in {'k', Entities.Cactus, 'cactus'}:
		soilProcedure()
		plant(Entities.Cactus)
		
	elif crop in {'T', Entities.Treasure, 'treasure'}:
		plant(Entities.Bush)
		substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
		use_item(Items.Weird_Substance, 16)
		mazeAlgorithms.busca(True)
		
		
	if spawn_drone(drone_ajudante):
		quick_print("Nan")
	fertilize_crop(crop, c_t_f)