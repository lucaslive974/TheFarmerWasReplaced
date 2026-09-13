priority_ctx: map[Entities, int] = {
  Entities.Grass: 0,
  Entities.Bush: 1,
  Entities.Carrot: 2
}

seeds: list[Entities] = [ Entities.Grass, Entities.Carrot, Entities.Bush ]

def till_if_needed():
    if(get_ground_type() != Grounds.Soil):
        till()
     
def water_if_needed():
    if(get_water() < 0.50):
        use_item(Items.Water)

def plant_entitie(entitie: Entities):
    till_if_needed()
    plant(entitie)

def plant_carrot() -> None:
    water_if_needed()
    plant_entitie(Entities.Carrot)    

def plant_bush() -> None:
    plant_entitie(Entities.Bush)
    
def plant_grass() -> None:
    plant_entitie(Entities.Grass)
