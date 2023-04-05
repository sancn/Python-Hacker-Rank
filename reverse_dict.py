#program to reverse the key value i.e key to value and value to key
 
dict1={'name':'ram','age':23,'address':'ktm'}


# dict1 = {value:key for key, value in dict1.items()} # using dictionary comparehensive

dict2={}
for key,value in dict1.items():
    #dict2.update({value:key}) # yasari ni hunxa
    dict2[value] = key

print(dict2)
