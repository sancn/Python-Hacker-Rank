# program to update id to userid
mylist=[{'id':2,'name':'ram'},{'id':4,'name':'sita'}]


# mylist[1]['userid']=mylist[1].pop('id')  # only second id lai matra userid banuxa


for i in mylist:
    if 'id' in i:
        i['userid'] = i.pop('id')

print(mylist)




# Create a dictionary inside list and access the key value pair

mylist=[{'id':2,'name':'ram'},{'id':4,'name':'sita'}]
# mydict=mylist[0]
for i in mylist:
    for key, val in i.items():
        print(f"{key}: {val}", end=' ')
    print()
    
