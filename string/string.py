# Create a string and perform operations

# Get input string from the user
text = input("Enter a string: ")

# a. Create a string & perform indexing & slicing
print("\n--- a. Indexing and Slicing ---")
print("First character :", text[0])
print("Last character :", text[-1])
print("First five characters:", text[0:5])
print("From index 3 onwards :", text[3:])
print("Every second char :", text[::2])
print("Reversed string :", text[::-1])

# b. Convert to upper case & lower case & swap case
print("\n--- b. Case Conversion ---")
print("Uppercase :", text.upper())
print("Lowercase :", text.lower())
print("Swapcase :", text.swapcase())

# c. Count the occurrence of a character or a substring
print("\n--- c. Count Occurrences ---")
sub = input("Enter a character or substring to count: ")
print("'" + sub + "' occurs", text.count(sub), "time(s)")

# d. Replace a word in the string
print("\n--- d. Replace a Word ---")
old = input("Enter the word to replace: ")
new = input("Enter the new word: ")
print("After replacing :", text.replace(old, new))

# e. Split & join string
print("\n--- e. Split and Join ---")
words = text.split()
print("After split :", words)
print("After join :", "-".join(words))

# f. Check whether the string starts or ends with a given substring
print("\n--- f. Starts With / Ends With ---")
start = input("Enter the substring to check at the start: ")
end = input("Enter the substring to check at the end: ")
print("Starts with '" + start + "' :", text.startswith(start))
print("Ends with '" + end + "' :", text.endswith(end))  