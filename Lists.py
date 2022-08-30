counties = ['Arapahoe', 'Denver', 'Jefferson']
print(counties[-1])
print(counties[2])
counties.insert(2, 'El Paso')
counties.remove('El Paso')
    # to update a list name use the [#position of Name] and enter the 'Name Change'
counties[2] = 'El Paso'
counties[2] = 'Jefferson'
print(counties)
    # Creating a Dictionary
counties_dict = {}
counties_dict['Arapahoe'] = 422829
counties_dict['Denver'] = 463353
counties_dict['Jefferson'] = 432438
print(counties_dict)
    # Getting items from the dict. add .item() this is a Tuple
print (counties_dict.items())
     # Getting keys from the dict. add .keys()
print(counties_dict.keys())
print(counties_dict.values())
    # To get a specific value, use .get() - example .get('Dever')
print(counties_dict.get('Denver'))
    # To get the # of registered voters we want to wrap the Key "Name of County" in brakets
print(counties_dict['Arapahoe'])














