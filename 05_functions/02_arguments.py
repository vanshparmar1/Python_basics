#arg and *kwarg(key value arguments)

def special_chai(*ingredients,**extras):
    print(f"Ingredients",ingredients)
    print(f"Extras",extras)

special_chai("Cinnamon", "Cardmom", sweetener="Honey", foam="yes")