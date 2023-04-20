def Anagrams(li ):
    
        dictionary = {}
        for word in li:
            sortedWord = ''.join(sorted(word))
# If word is not in dictionary
            if sortedWord not in dictionary:
                dictionary[sortedWord] = [word]
# If previously it is present that means its anagram
# was previously present
            else:
                dictionary[sortedWord] += [word]
                return [dictionary[i] for i in dictionary]


li = ["a"]
# Call to function to Solve and group Anagrams
print(Anagrams(li))