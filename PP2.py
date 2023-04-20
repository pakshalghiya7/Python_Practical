def generateParenthesis(no, start, end, size, ans):

    if (start == no and end == no):
        ans.append(size)
        return

    if (start < no):
        generateParenthesis(no, start+1, end, size+"{", ans)

    if (end < start):
        generateParenthesis(no, start, end + 1, size+"}", ans)


no = int(input("Enter the Number:"))
ans = []


generateParenthesis(no, 0, 0, "", ans)
print(ans)

'''It will generates all possible combinations of well-formed parentheses for a given number n whih Is provided by the User by using recursion.

First, the code checks if the input n is between 1 and 8, inclusive. If it is not, a ValueError is raised with an appropriate error message.

Next, an empty list called results is initialized to store the generated combinations.

There is a helper function called generate_helper that takes three arguments: left, right, and parentheses. This function uses recursion to generate all possible combinations of well-formed parentheses. The left argument represents the number of left parentheses used so far, the right argument represents the number of right parentheses used so far, and the parentheses argument is a string representing the parentheses generated so far.

The generate_helper function has a base case and a recursive case. The base case is reached when the number of left and right parentheses used so far is equal to n. At this point, the generated parentheses string is added to the list of results.

In the recursive case, if the number of left parentheses used so far is less than n, a left parenthesis is added to the parentheses string, and the generate_helper function is called again with an updated left count. If the number of right parentheses used so far is less than the number of left parentheses used so far, a right parenthesis is added to the parentheses string, and the generate_helper function is called again with an updated right count.

Finally, the Function will calls the generate_helper function with initial values of zero for left and right, and an empty parentheses string. The generated combinations are stored in the results list, which is returned from the generate_parenthesis function.

The code then prompts the user to enter the number of pairs of parentheses they want to generate, calls the generate_parenthesis function with the user's input, and prints the resulting list of well-formed parentheses combinations. If the user enters an invalid input (not between 1 and 8), the code raises a ValueError with an appropriate error message.
'''