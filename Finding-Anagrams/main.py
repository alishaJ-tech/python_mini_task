# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    if sorted(word) == sorted(anagram):
        return True

print("Enter First String: ", end="")
first_txt = str(input())
print("Enter Second String: ", end="")
secnd_txt = str(input())

texts = find_anagram(first_txt, secnd_txt)
if texts==True:
    print("\nStrings are Anagram")
else:
    print("\nStrings are Not Anagram")

   

