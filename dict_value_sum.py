################################################################################
################################################################################
#Dictionary ko value sum garni

dict1={'one':1,'two':2}
total_sum=0
for value in dict1.values():
    # total_sum=total_sum+value
    total_sum+=value

print(total_sum)

###############################################################################
######################################################################
# sum the value of dictionary if integer value xa vanea

dict1={'one':1,'two':2,'sjkldfj':'jsdhjkfjh','adlkjs':23,'akhsd':'sdf'}
total_sum=0

for key,value in dict1.items():
    if type(value)==int:
        total_sum+=value
print(total_sum)

    
###############################################################################
###############################################################################
# sum the value of dictionary if integer value xa vanea using list comprehension


total_sum=sum([val for val in dict1.values() if type(val)==int])
print(total_sum)

############another way##############

total_sum=sum([val for val in dict1.values() if isinstance(val,int)])
print(total_sum)











# print(sum_count)

# print(dict1['two'])
# # for key,value in dict1.items():
# #     print(value)ct
# print(dict1.__dict__)
