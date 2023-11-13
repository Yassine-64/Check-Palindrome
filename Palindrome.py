word = input("Enter a word: ")
word_list = list(word)
reversed_word = ''.join(word_list[::-1])

if word == reversed_word:
    print("Palindrome")
else:
    print("Not a palindrome")
