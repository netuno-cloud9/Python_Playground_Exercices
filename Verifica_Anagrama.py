str_1 = input("Enter the first string: ")
str_2 = input("Enter the second string: ")

#Remove spaces and change to upper case
str_1 = str_1.replace(" ", "").upper()
str_2 = str_2.replace(" ", "").upper()

#Sort the strings
sorted_str_1 = sorted(str_1)
sorted_str_2 = sorted(str_2)

#Compare the sorted strings
if sorted_str_1 == sorted_str_2:
   print("The strings are anagrams!")
else:
   print("The strings are not anagrams.")
