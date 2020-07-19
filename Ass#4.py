#This is Assignment  #3


#initialized my global variables

myUniqueList = []
myLeftovers  = []

#this function will take my leftovers
def take_myLeftovers(value):
    global myLeftovers
    myLeftovers.append(value)
    return False

#this function will insert value to list
def insert_list(value):
    global myUniqueList
    if value not in myUniqueList:
        myUniqueList.append(value)
        return True
    else:
        return take_myLeftovers(value)
        

#This is my Main Function

#Inserting values
print(insert_list("Umar"), "<- Inserted")
print(insert_list("Umar") , "<- rejected to insert")
print(insert_list("Talha"), "<- Inserted")
print(insert_list("Talha"), "<- rejected to insert")

#printing out all elements of list
print("MyUniqueList:" , myUniqueList)
print("MyLeftovers:"  , myLeftovers)