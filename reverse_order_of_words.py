# Write a program to reverse the order of words in a sentence using a while loop.
sentence = input("Enter a sentence: ")
words = sentence.split()
reversed_sentence = " ".join(reversed(words))
print("Reversed sentence:", reversed_sentence)
