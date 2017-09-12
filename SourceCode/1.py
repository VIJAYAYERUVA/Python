import string

alphabet = set(string.ascii_lowercase)
input_string = 'We promptly judged antique ivory buckles for the next prize'
if (set(input_string.lower()) >= alphabet):
    print(set(input_string.lower()))
    print(alphabet)
    print(input_string)
    print("The above string contain all letters of the alphabet")
else:
    print(input_string)
    print("The above string not contain all letters of the alphabet")

input_string = 'string not contains every letter of the alphabet'
if (set(input_string.lower()) >= alphabet):
    print(input_string)
    print("The above string contain all letters of the alphabet")
else:
    print(input_string)
    print("The above string not contain all letters of the alphabet")
