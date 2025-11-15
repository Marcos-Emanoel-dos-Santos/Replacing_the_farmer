# mazeAlgorithms

Creates an algorithm to find the chest in a maze.
WARNING: may not be so efficient.


## setFarm()
### SETS/RESETS THE FARM GRID FOR THE MAZE


## neighbors()
### CHECKS ALL AVAILABLE DIRECTIONS FOR MOVEMENT.

## mark_visited(x, y)
### MARKS THE POSITION AS VISITED.
The drone won't go to a already visited position.


## mark_dead_end(x, y)
### MARKS THE POSITION AS A DEAD END.
The drone won't go to a dead end.


## search(reset)
### MOVES THROUGH THE MAZE SEARCHING FOR THE TREASURE.

Receives as parameters:
True

### Example:
``` python
while True:
	moveModule.go_to(get_world_size()//2, get_world_size()//2)
	plant(Entities.Bush)
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)
	mazeAlgorithms.search(True)
```
Moves the drone to the center of the farm, creates a maze and search through it.
You may want other drones' help, so the code below may be of greater utility:

``` python
import moveModule
import mazeAlgorithms

clear()

# A python function can receive other functions as parameters,
# but if it receives a function with parameters,
# it will execute the function
# and return its result, which is not a function.
# This function injects parameters into
# another function so the code works.
def encaps(bool):
	def tsk():
		mazeAlgorithms.search(bool)
	return tsk

def main():
	while True:
		moveModule.go_to(get_world_size()//2, get_world_size()//2)
		plant(Entities.Bush)
		substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
		use_item(Items.Weird_Substance, substance)
		while num_drones() < max_drones():
			spawn_drone(encaps(True))
		mazeAlgorithms.search(True)
			
if __name__ == "__main__":
	main()
```