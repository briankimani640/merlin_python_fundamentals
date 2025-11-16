def parse_input(user_input):
    """convert the comma seperated string to be a list of float numbers"""
    try:
        numbers = [float(x.strip())for x in user_input.split(",") if x.strip()]
        return numbers
    except ValueError:
        #ValueError indicates wrong argument was passed for the function ie
        #user_input = "Joseph" , 7, "Jane"
        print("Enter only numeric values seperated by commas!!")
        return [] # ensuring there is always a return incase of a ValueError
    
def summerize_data(numbers):
    """ compute the count, min, max sum and average"""
    if not numbers:
        return {'error': "No numbers data provided"}
    #python math methods - count, sum max, min avaverage
    total = sum(numbers) # sum: sums up the elements in a list of integers /list of float
    count = len(numbers) # length returns the size of a list ie number of elements in the list
    smallest = min(numbers) # min returns the minimum value in the list
    largest = max(numbers) # max eturns the maximum value in the list
    average = round (total / count, 2) # round returns a float value with a determined accuracy
    return {
        'count' : count,
        'sum' : total,
        'min' : smallest,
        'max' : largest,
        'average' : average,


    }
def display_result(result):
    """ display the summerized dictionary in a readable way"""
    print("Summary of your data: ")
    for key,value in result.items():
        print(f"The {key} is {value}")

# first function, main entry function
def main():
    """ main function : handle input and output printing"""
    user_input = input("Enter numbers seperated by commas:: ")
    #pass user input to the modulus function that handles cleaning of the input
    numbers = parse_input(user_input)
    print(numbers)
    result = summerize_data(numbers)
    print(result) # dicionary
    display_result(result)


if __name__ == '__main__':
    main()


