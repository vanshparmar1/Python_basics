# Working with lists
ingredients = ["water", "milk", "black tea"]
ingredients.append("sugar")
print(f"Ingredients are: {ingredients}")
ingredients.remove("water")

# Finding the maximum and minimum sugar levels in a list
sugar_levels = [1,2, 3, 4, 5]
print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Minimum sugar level: {min(sugar_levels)}")

# Working with raw byte data
raw_spice_data = bytearray (b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Bytes: {raw_spice_data}")
