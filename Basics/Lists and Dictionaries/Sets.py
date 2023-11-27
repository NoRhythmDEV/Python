#Set = Collection, unordered and unindexed. No Duplicate Values

utensils = {"fork","spoon","knife","cup"}
dishes = {"bowl","plate","cup"}

#utensils.add("spork") #adds new item to set
#utensils.remove("fork") #removes given item out of set
# utensils.clear() #clears set
#utensils.update(dishes) # will update set with another set and add the items from the set to the other set

#creates new set with 2 sets
#dinner_table = utensils.union(dishes)


#output will be random since its unordered
for x in utensils:
    print(x)

#compare sets what the other has and the one doesnt
print(utensils.difference(dishes))

#compare set what they both have
print(utensils.intersection(dishes))