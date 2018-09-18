def displayResult(wage):
    print("The employee's gross wage is: $" + wage)

def enterHours(hours):
    print("Please enter the total number of hours worked.")
    hours = float(input())
    
    return hours

def enterRate(hours):
    print("Enter the employee's hourly payrate.")
    rate = float(input())
    wage = hours * rate
    
    return rate

# Main

# A program that calculates your gross wage using a functions - flowgorithm
hours = enterHours()
rate = enterRate(hours)
displayResult (wage)
