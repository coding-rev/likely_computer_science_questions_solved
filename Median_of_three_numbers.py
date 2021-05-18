#Function for calculating median
def medianFunction(first_number, second_number, third_number):
    listOfNumbers = []
    listOfNumbers.append(first_number)
    listOfNumbers.append(second_number)
    listOfNumbers.append(third_number)
    listOfNumbers.sort()
    return listOfNumbers[1]

# Getting an instance of the function
medianValue = medianFunction(490,22,48)
print("The median value is : ", medianValue)
