"""
0.Setup
a.create a list of 13 integers and assign it to a variable
1.List Slicing With Stride
a.create a variable and assign it a list slice comprised of every 4th number from the list you made in step 0.a.
b.print the list slice from step 1.a.
2.List Slicing with Stride and Omitted start and end indices
a.using only stride, assign a list slice composed of every 3rd value from the list you made in step 0.a. to a
variable.
b.print the list slice from step 2.a.
3.Reversing Lists with Stride
a.reverse the list you made in step 0.a. and assign it to a variable
b.print the reversed list you made in step 3.a.
"""
integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

slice4th = integers[4:13:4]
print(slice4th)
slice3rd = integers[::3]
print(slice3rd)
reverse = integers[::-1]
print(reverse)
