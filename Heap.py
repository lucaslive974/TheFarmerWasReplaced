from Utils import error_NYI

def heapify(arr: list[Entities]) -> None:
    error_NYI("::heap::heapify")

def parent(idx: int) -> int:
    return (idx - 1) / 2
    
def left_child(idx: int) -> int:
    return idx * 2 + 1
    
def right_child(idx: int) -> int:
    return idx * 2 + 2