"""

    ASSIGNMENT #1
    QUESTION 9
    AUTHOR: Bonnie Ives de Castro Nunes
    DATE: September 15th, 2023
    
"""

inputList = [54, 44, 27, 79, 91, 41]

print("----- Informed list -----")
print(inputList)

index4 = inputList[4]

inputList.pop(4)
inputList.insert(1,index4)
inputList.append(index4)

print("\nFinal list after inserting", index4,"into 2nd position and final position.")
print(inputList)
