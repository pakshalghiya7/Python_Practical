# def group_anagrams(lst):
    
#     """
#     Groups the words in the given list into sets of anagrams.

#     Args:

#     lst (list): A list of words.

#     Returns:

#     dict: A dictionary mapping sorted strings of characters to lists of words that are anagrams of each other.

#     """
#     anagrams = {}
#     for word in lst:
#         sorted_word = ''.join(sorted(word))
#         if sorted_word in anagrams:
#             anagrams[sorted_word].append(word)
#         else:
#             anagrams[sorted_word] = [word]
#     return anagrams


# try:
#     strs = eval(input("Enter Inputs In List Seperated by Commas : "))
    
    
#     if len(strs) < 1 or len(strs) > 104:
#         raise ValueError("Number of inputs must be between 1 and 104.")
    
#     for item in strs:

#         if not (0 < len(item) <= 100 and item.islower()):
#             raise ValueError("Each Input must be a lowercase and length of string should between 1 and 100.")


        
#     anagrams = group_anagrams(strs)
#     print(list(anagrams.values()))

# except ValueError as vError:
#     print(f"Invalid input: {vError}")
# except TypeError:
#     print("Please enter valid String Input")
# except Exception:
#     print("An Error occurred. Please try again.")

#############################################################################################################################33333

# def group_anagrams(lst):
#     """
#     This function groups the words in the given list into sets of anagrams.
#
#     Args:
#         lst (list): A list of words.
#
#     Returns:
#         dict: A dictionary mapping sorted strings of characters to lists of words that are anagrams of each other.
#
#     """
#     anagrams = {}
#     for word in lst:
#         if len(word) == 0:
#             continue
#         sorted_word = ''.join(sorted(word))
#         if sorted_word in anagrams:
#             anagrams[sorted_word].append(word)
#         else:
#             anagrams[sorted_word] = [word]
#     return anagrams
#
#
# try:
#     strs = eval(input("Enter inputs: "))  # Prompting user to enter inputs
#     if len(strs) < 1 or len(strs) > 104:
#         raise ValueError("Number of inputs must be between 1 and 104.")  # Raising an error if input length is invalid
#     for item in strs:
#         if not (0 <= len(item) <= 100 and item.islower()):
#             raise ValueError("Each input must be a lowercase string with length between 1 and 100.")  # Raising an error if input string is invalid
#     anagrams = group_anagrams(strs)  # Calling group_anagrams function to group anagrams
#     print(list(anagrams.values()))  # Displaying a list of values in the anagrams dictionary
# except ValueError as valError:
#     print(f"Invalid input: {valError}")  # Displaying an error message if an error occurs with the input
# except TypeError:
#     print("Please enter valid input.")  # Displaying an error message if input is not of the expected type
# except IndexError:
#     print("Please check the inputs again.")  # Displaying an error message if there is an issue with indexing during execution
# except Exception:
#     print("An error occurred. Please try again.")  # Displaying a general error message if an unexpected error occurs.

