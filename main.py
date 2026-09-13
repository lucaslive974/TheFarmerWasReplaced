from Seeds import plant_carrot, plant_bush, plant_grass
from Utils import customize_drone
from Iterator import *

def harvest_if_possible() -> None:
        while not can_harvest():
            do_a_flip()
            continue
        harvest()

def engine_start() -> None:
    clear()  
    customize_drone()   
    it = get_iterator(6, [0, 0])
    while True:
        traverse(plant_bush, reverse_iterator(it))
        traverse(harvest_if_possible, it)

                

# Main Loop
engine_start()