fruits_data= {
    'apple':130,
    'avocado':50,
    'banana':110,
    'kiwifruit':90,
    'pear':100,
    'sweet cherries':100,
    'tomato':""

}

item = input("Item: ").lower()
x = fruits_data.get(item)

print(x)
