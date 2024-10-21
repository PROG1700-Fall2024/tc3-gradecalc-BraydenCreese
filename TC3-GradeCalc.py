# Grade Point Calculator

# Create a console-based program that will take a letter grade, such as B+ or C, and convert it to its 
# corresponding numeric value. It will use two prompts, one for the letter grade and a second for the
# modifier, if any (+ or -), and calculate, then output the proper number grade.

# •	Possible letter grades are A, B, C, D, and F
# •	Possible numeric values are 4, 3, 2, 1, and 0, respective to the letters listed above.
# •	Possible modifiers are a plus (+), a minus (–) or nothing. 
# •	There is no F+ or F–. 
# •	Using the + sign increases the numeric value by 0.3, using the – sign decreases it by 0.3. However, an A+ has 
#       still has a value of only 4.0. 
# •	A valid letter grade can be either uppercase or lowercase.
# •	If an invalid value is entered, display a warning message.


def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    # Gives user a breakdown for the prog
    print("Grade Point Calculator")
    print("\nValid letter grades that can be entered: A, B, C, D,F.")
    print("Valid grade modifiers are +, - or nothing.")
    print("All letter grades except F can include a + or - symbol")
    print("Calculated grade point value cannot exceed 4.0.")


    # gets user input and catches for any invalid inputs. ( Takes all input as uppercase Ex: 'A' )
    while True:
            userLetterGrade = input("\nPlease enter a letter grade: ").upper()
            if userLetterGrade in ['A', 'B', 'C', 'D', 'F']:
                  break
            else:
                  print("Invalid Input! Please enter a valid letter grade.")


    while True:
        gradeModifier = input("Please enter a modifier (+, - or nothing): ")
        if gradeModifier in ['+', '-', '']:
              break
        else:
            print("Invalid Input! Please enter a valid letter grade.")


    # using if statmenats to check the grade and modifier entered by the user
    """
    desided to do this in a simple way this time, we could make a table and make a table and map out the values
    Ex: ( gradePoints = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0} ). Then use this to make a few
    if, else, elif statments that check for the gradeModifier and userLetterGrade, add a check for a A+ cap at
    4.0 and a low cap for no F+ or F-, Then a small check for the -/+ for the 0.3 grade point diff.
    """
    if userLetterGrade == 'A':
        if gradeModifier == '-':
            numValue = 3.7
        else:
            numValue = 4.0

    elif userLetterGrade == 'B':
        if gradeModifier == '+':
            numValue = 3.3
        elif gradeModifier == '-':
            numValue = 2.7
        else:
            numValue = 3.0

    elif userLetterGrade == 'C':
        if gradeModifier == '+':
            numValue = 2.3
        elif gradeModifier == '-':
            numValue = 1.7
        else:
            numValue = 2.0

    elif userLetterGrade == 'D':
        if gradeModifier == '+':
            numValue = 1.3
        elif gradeModifier == '-':
            numValue = 0.7
        else:
            numValue = 1.0
    
    else:
        numValue = 0.0


    # displaying the users output from the inputed values
    print(f"\nThe numeric value for {userLetterGrade}{gradeModifier} is {numValue:.1f}.")


    # YOUR CODE ENDS HERE

main()
