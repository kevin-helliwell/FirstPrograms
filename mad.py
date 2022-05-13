# Asks the user to enter a phrase, and then prints out the following:
# (1) The “mad” version of the phrase in all caps.
# (2) A confused (i.e., mad) version of the phrase where all letter e’s are replaced by x’s.
# (3) The maddest of all: print whether the phrase is printable.

phrase = str(input("Please enter a phrase.\n"))

mad = phrase.upper()
print(mad)

confused = phrase.replace("e", "x")
print(confused)

maddest = phrase.isprintable()
print(maddest)