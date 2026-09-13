from Utils  import no_op

           
def get_iterator(size: int = get_world_size(),
origin: list[int] = (0,0), reverse: bool = True) -> dict[str, any]:
  return {
    "reverse": reverse, 
    "size": size,
    "origin": origin
  }

def reverse_iterator(iterator: dict[str, any]) -> it:
    iterator["reverse"] = not iterator["reverse"]
    return iterator

def traverse(fn, iterator: dict[str, any]) -> None:
    size: int = iterator["size"]
    n: int = size * size
    for i in range(n):
        pos : int = i
        if iterator["reverse"]:
            pos = n - 1 - i
        next(pos, iterator)
        fn()

def next(position: int, it: dict[str, any]) -> None:
    size: int = it["size"]
    origin: int = it["origin"]
    
    offset_x = origin[0]
    offset_y = origin[1]
    
    x: int = position % size
    y: int = position // size
    if(y % 2 != 0):
        x = size - 1 - x
        
    move_to(x + offset_x, y + offset_y)
     
def next_row() -> None:
    move(North)
    
def previous_row() -> None:
    move(South)
        
def next_col() -> None:
    move(East)
 
def previous_col() -> None:
    move(West)
        
def reset_to_origin() -> None:
    move_to(0, 0)
 
def move_to(x: int, y: int) -> None:
    dis_x: int = x - get_pos_x()
    dis_y: int = y - get_pos_y()
    
    move_x = no_op
    if dis_x > 0:
        move_x = next_col
    else:
        move_x = previous_col
        
    move_y = no_op
    if dis_y > 0:
        move_y = next_row
    else:
        move_y = previous_row
        
    while(get_pos_x() != x):
        move_x()
        
    while(get_pos_y() != y):
        move_y()
