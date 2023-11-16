# STRING OPERATIONS WITHOUT USING IN-BUILT STRING LIBRARY FUNCTION

# 1. CONCATENATING TWO STRINGS
def concatenate_strings(str1, str2):
    print("\n1. Concatenated strings: " + str1 + " " + str2)


# 2. CALCULATING LENGTH OF THE STRINGS
def calculate_length(string):
    count = 0
    for i in string:
        count += 1
    print(f"    Length of string '{string}': {count}")


# 3. LEFT SHIFT (ROTATION)
def left_rotate_string(input_string, rotations):
    # Ensure the number of rotations is within the length of the string
    rotations %= len(input_string)
    # Perform the left rotation using slicing
    rotated_string = input_string[rotations:] + input_string[:rotations]
    print(f"    Left Shift ({rotations} shifts) for '{input_string}': {rotated_string}")


# 4. RIGHT SHIFT (ROTATION)
def right_rotate_string(input_string, rotations):  
    # Ensure the number of rotations is within the length of the string
    rotations %= len(input_string)
    # Perform the right rotation using slicing
    rotated_string = input_string[-rotations:] + input_string[:-rotations]
    print(f"    Right Shift ({rotations} shifts) for '{input_string}': {rotated_string}")


# 5. EXTRACTING SUBSTRING
def extract_substring(string, start, end):
    substring = ""
    if end < (len(string)+1):
        for i in range((start  - 1), end):
            substring = substring + string[i]
        print(f"    The extracted substring from '{string}' - ({start} to {end}): {substring}")
    else:
        print(f"    ERROR: INDEX OUT OF RANGE FOR '{string}'.")        
    

# 6. CONVERT TO UPPERCASE 
def convert_to_uppercase(string):
    uppercase = ""
    for char in string:
        if 'a' <= char <= 'z':
            uppercase += chr(ord(char) - 32)
        else:
            uppercase += char
    print(f"    Uppercase for '{string}': {uppercase}") 


# 7. CONVERT TO LOWERCASE
def convert_to_lowercase(string):
    lowercase = ""
    for char in string:
        if 'A' <= char <= 'Z':
            lowercase += chr(ord(char) + 32)
        else:
            lowercase += char
    print(f"    Lowercase for '{string}': {lowercase}")


# 8. FINDING INDEX OF SUBSTRING PROVIDED 
def find_substring(string, sub):
    index = -1
    for i in range(len(string) - len(sub) + 1):
        if string[i:i+len(sub)] == sub:
            index = i
            break
    if index != -1:
        print(f"    SUBSTRING '{sub}' FOUND at index (position) {index + 1} in '{string}'.")
    else:
        print(f"    SUBSTRING '{sub}' NOT FOUND in the given string '{string}'.")


# 9. SPLITTING STRING INTO SUBSTRINGS
def split_string(string, delimiter):
    substrings = []
    start = 0
    for i in range(len(string)):
        if string[i] == delimiter:
            substrings.append(string[start:i])
            start = i + 1
    if string[start:] == '':
        pass
    else:
        substrings.append(string[start:])
    print(f"    The substrings for the string '{string}' are: {substrings}")


# 10. REPLACING A SUBSTRING
def replace_substring(string):
    print(f"    Given string is: {string}")
    old_sub = input("    Enter the substring to be replaced: ")
    new_sub = input("    Enter new substring: ")
    result = ""
    i = 0
    while i < len(string):
        if string[i:i+len(old_sub)] == old_sub:
            result += new_sub
            i += len(old_sub)
        else:
            result += string[i]
            i += 1
    print(f"    The Resultant String is: {result}")


# 11. REVERSING THE STRING
def reverse(s):
    print(f"    String given: {s}")
    str = ""
    for i in s:
        str = i + str
    return str


stringA = input("\nEnter String 1: ")
stringB = input("Enter String 2: ")

concatenate_strings(stringA, stringB)

print("\n2. Length of the strings: ")
calculate_length(stringA)
calculate_length(stringB)

print("\n3. Left rotation: ")
left = int(input("    Enter Left Shift Number: "))
left_rotate_string(stringA, left)
left_rotate_string(stringB, left)

print("\n4. Right rotation: ")
right = int(input("    Enter Right Shift Number: "))
right_rotate_string(stringA, right)
right_rotate_string(stringB, right)

print("\n5. Substring extraction: ")
begin = int(input("    Enter Start Number for Substring: "))
end = int(input("    Enter End Number for Substring: "))
extract_substring(stringA, begin, end)
extract_substring(stringB, begin, end)

print("\n6. Converting strings to uppercase: ")
convert_to_uppercase(stringA)
convert_to_uppercase(stringB)

print("\n7. Converting strings to lowercase: ")
convert_to_lowercase(stringA)
convert_to_lowercase(stringB)

print("\n8. Finding index of substring provided: ")
substring = input("    Enter Substring to be Searched: ")
find_substring(stringA, substring)
find_substring(stringB, substring)

print("\n9. Splitting given strings into substrings: ")
delim = input("    Enter your delimiter character: ")
split_string(stringA, delim)
split_string(stringB, delim)

print("\n10. Replacing a substring: ")
replace_substring(stringA)
replace_substring(stringB)

print("\n11. Reversing the string: ")
print("    Reversed string is: ", reverse(stringA))
print("    Reversed string is: ", reverse(stringB))
