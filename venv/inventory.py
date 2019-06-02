stuffs = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):
    print("Inventory:")
    total_items = 0
    for k, v in inventory.items():
        total_item = total_item + v.get(item,0)
        print("total number of items: " + str(total_items))
display_inventory(stuffs)
