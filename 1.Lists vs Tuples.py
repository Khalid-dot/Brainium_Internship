#Lists:
#Mutable, have many methods
#append(), extend(), insert(), remove(), pop(), clear(), index(), count(), sort(), reverse(), copy()
print("--------------------------------LISTS--------------------------------")
List=["Khalid","Ali","Usman","Aasim"]
print("Original List: ",List)
List.append(2)#insert element at the end
print("After Appending: ",List)
List.insert(1,"Hashir")#insert element at the desired index
print("After Inserting: ",List)
List.remove(2)#will remove the mentioned element
print("After Removing: ",List)
print("Poping out:",List.pop(4))#will pop out element the the mentioned index
print("Index of Hashir: ",List.index("Hashir"))
print("Count of Usman: ",List.count("Hashir"))
List.reverse()
print("Reversing List: ",List)
copyList=List.copy()#doing so creates a duplicate copy of the original with its own memory block, = will duplicates the list but both will point to the same list in the memory
print("Printing copy List: ",copyList)

#Tuples:
#Immutable, have limited methods
#count(),index()
print("\n\n--------------------------------TUPLES--------------------------------")
tuple=(1,2,3,4,5,"Khalid","Ali","Usman",1,2,3,4,5)
print("Original Tuple: ",tuple)
print("Counting 2: ",tuple.count(2))
print("Index of 5: ",tuple.index(5))#will return fisrt occurance of an element