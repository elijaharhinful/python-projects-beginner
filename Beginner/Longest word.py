# This code takes a sentence and outputs the longest word in the sentence

sentence = input("Enter your sentence here: ")

length = 0
longword = ""

for i in sentence.split(" "):
    newlength = len(i)
    if newlength > length:
        length = newlength
        longword = i
    else:
        pass


print("The longest word is:", longword.upper())
print("It has", len(longword), "letters.")
