# Make complex data structures of 
import pprint
# pets dictionary with their (key) at least 2: list of dicts, keys name, age, color

pets = {'dog': [{'name':'chewy','color':'black','age':7}],'cat': [{'name':'lilly','color':'white','age':9}]}

print(pets)
pprint.pprint(pets)

# print out one dogs name age and color, and one cats name, age and color

#dog's name
print(f"The dog name is: {pets['dog'][0]['name']} and color is {pets['dog'][0]['color']} and age {pets['dog'][0]['age']}")
#cat's name 
print(f"The cat name is: {pets['cat'][0]['name']}.")


#pets = {'cats': [{'age': 7, 'colors': ['orange', 'brown'], 'name': 'garfield'}, {'age': 2, 'colors': ['white'], 'name': 'snowball'}], 'dogs': [{'age': 3, 'colors': ['brown'], 'name': 'steve'}, {'age': 12, 'colors': ['black', 'white'], 'name': 'rover'}]}

#pprint.pprint(pets)
# print out one dogs name age and color, and one cats name, age and color

#colours = ' and '.join(pets['dogs'][0]['colors'])
#print(f"My dog {pets['dogs'][0]['name']} is {pets['dogs'][0]['age']} years old and is {colours} in color.")

# A little ugly
#hues = ""
#for color in pets['cats'][0]['colors']:
#    print(color)
#    hues += f" and {color}"
#print(hues)
#print(color)
#print(f"My cat {pets['cats'][0]['name']} is {pets['cats'][0]['age']} years old and is {hues}  in color.")



# Prettier way
#colour = ' and '.join(pets['cats'][0]['colors'])
#print(f"My cat {pets['cats'][0]['name']} is {pets['cats'][0]['age']} years old and is {colour} in color.")
