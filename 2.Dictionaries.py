#Dictionaries:
#contains onordered key-value pairs
#keys(), values(), items(), get(), update(), pop(), popitem(), clear(), copy()
print("\n\n--------------------------------DICTIONARIES--------------------------------")
dict={
    "Name":"Khalid",
    "Age":23,
    "University":"Bahria University",
    "CGPA":3.54
}
print("Original Dictionary: ",dict)
print("Printing Keys: ",dict.keys())#print keys
print("Printing Values: ",dict.values())#print values
print("Printing items: ",dict.items())#print all items
print("Getting Age: ",dict.get("Age"))#print desired value, will return none if doesn't exist
print("Getting CGPA: ",dict["CGPA"])#print desired value, will throw error if nothing exists
dict["Company"]="Brainium"#adds a new value
print("After Adding Company: ",dict)
dict["Company"]="Systems Limited"#updates existing value
print("After Updating Company: ",dict)
print("Poping last key value: ",dict.popitem())#will removed the last key-value pair
print("After Poping: ",dict)
print("Poping University: ",dict.pop("University"))#will removed the last key-value pair
print("After Poping University: ",dict) 