

class Item_Values:
    values = {
    'PIPE': {"Scrap": 5, "HQM": 1},
    'PIPES': {"Scrap": 5, "HQM": 1},
    'SHEET METAL': {"Scrap": 8, "HQM": 1, "Metal Fragments": 100},
    'ROAD SIGN': {"Scrap": 5, "HQM": 1},
    'SPRING': {'Scrap': 10, 'HQM': 1},
    'METAL BLADE': {'Scrap': 2, "Metal Fragments": 15},
    'GEARS': {'Scrap': 10, "Metal Fragments": 13},
    'SEMI BODY': {'Scrap': 15, "Metal Fragments": 75, "HQM": 2},
    'SMG BODY': {'Scrap': 15,"HQM": 2},
    'AK BODY': {'Scrap': 25,"HQM": 2},
    'TECH TRASH': {'Scrap': 20,"HQM": 1},
    'CAMERA': {'Tech Trash': 2,"HQM": 2},
    'LAPTOP': {'Tech Trash': 3,"Metal Frags": 50, "HQM": 1},
    'ROPE': {'Cloth': 15},
    'SEWING KIT': {'Cloth': 10, "Rope": 2},
    'TARP': {'Cloth': 50},
    'FUSE': {'Scrap': 20},

    }


class Item_calculator:
    def __init__(self, item, quantity):
        self.item = item.upper()
        self.quantity = quantity
        results = []
        if self.item in Item_Values.values:
           Comps = Item_Values.values[self.item]
           for comp, value in Comps.items():
               Total = int(value) * int(self.quantity)
               results.append(f"{Total} {comp}")
        print(f"For {self.quantity} {self.item}, you get: {', '.join(results)}")
               
           

print("Welcome to the Rust Recycle calculator")


items_I_Have = input("What items do you have? ").split(',')
if input("Do you have any other Items? ") == 'yes':
    items_I_Have += input("What other items do you have? ").split(',')


for item in items_I_Have:
    item = item.strip()
    hm = input(f"How many {item} do you have? ").strip()
    if not hm.isdigit():
        print("Please enter a valid number.")
        continue
            
    if input(f"Do you want to calculate the value of your {item}? (yes/no) ").lower() == 'yes':
        Item_calculator(item, hm)
print("Thank you for using the Rust Recycle calculator")
