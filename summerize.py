"""
- takes a list of numbers as input [1,2,3,4,5]
- processes the list and returns a dictionary of key and value pairs for the following:
    - sum: total sum of numbers
    - count: total count of numbers
    - average: average of numbers
    - max: maximum number in the list
    - min: minimum number in the list

    take the input from the terminal
"""
# analyze this function for a single responsibility perspective - keep functions short, -> one purpose for the function
def summerize_data(numbers):
    """refrence comments above"""
    # if numbers is empty
    if not numbers:
        return {"error" : "No data provide"}
    # refrence units - total, count, smallest, largest
    total = 0
    count = 0
    smallest = float('inf') # special string 'inf' and '-inf' - used to specify the larget, infinity
    largest = float('-inf')

    #loop list
    for num in numbers:
        #get total (additional assignment operator)
        total += num
        count += 1
        #smallest number
        if num < smallest:
            smallest = num
        # largest number
        if num > largest:
            largest = num
    # average
    average = total / count
    # dict
    op_dict = {"count" : count, "sum" : total, "min" : smallest, "max" : largest, "average" : round(average,2)}
    return op_dict

# inuilt variables __name__ and __main__
if __name__ == "__main__":
    # take input from terminal
    user_input = input("Enter a list of numbers separated by commas: ")
    # split and convert to float
    # Try (try executing) and except (error handling) to manage invalid inputs : error handling
    try:
        # take users input as a list
        # split inbuilt string method to split by commas
        # strip() method to remove any extra spaces and illegal characters 
        numbers = [float(x.strip()) for x in user_input.split(",") if x.strip()]  # list comprehension to convert input strings to floats
        print(numbers)
        result = summerize_data(numbers)
        print(result)

    except ValueError:
        print("Please enter only numeric values")

    