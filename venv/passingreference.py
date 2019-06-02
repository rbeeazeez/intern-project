# Passing by reference


def cook(ingredients=[], foodstuff=""):
    ingredients.append(foodstuff)


soup = ["water", "rice", "pepper"]
print(hex(id((soup))))
cook(soup, "beans")
print(soup)
print(hex(id((soup))))

num = int(1)
print(hex(id((num))))
num = int(8)
print(hex(id((num))))

def bookshop(stationeries = [], writing = ""):
    stationeries.append(writing)
materials = ["pen", "pencil", "eraser"]
bookshop(materials, "sharpener")
print(materials)


# Passing by value


name = "Ray"
print(hex(id((name))))
name = "Ramond"
print(hex(id((name))))
name = "Ramond" + "tkjpe"
print(hex(id((name))))



def try_to_change_list_contents(the_list):
    print('got', the_list)
    the_list.append('four')
    print('changed to', the_list)

outer_list = ['one', 'two', 'three']

print('before, outer_list =', outer_list)
try_to_change_list_contents(outer_list)
print('after, outer_list =', outer_list)

