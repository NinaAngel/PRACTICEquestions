Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
... #............................................SECTION B STRUCTURED QUESTIONS.............................
... 
... 
... 
... #QUESTION ONE
... name=input("Enter your name: ")
... age=input("Enter your age: ")
... 
... print("hello ", name , "You are ",age, "years old")
... 
... 
... 
... 
... 
... 
... #QUESTION TWO
... 
... numbers= input("Enter a list of numbers ").split(',')
... sum = 0
... 
... for number in numbers:
...     if int(number) % 2 == 0:
...         sum += int(number)
... 
... print("The sum of even numbers in the list is:", sum)
... 
... 
... 
... 
... 
... 
... #QUESTION THREE
... def words_list(strings):
... 
...     words = []
...     for string in strings:
...         if len(string) > 5:
...             words.append(string)
...     return words
... 
... 
... strings = ["apple", "banana", "orange", "watermelon", "grapefruit", "pear", "peach"]
... words = words_list(strings)
... print(words)
... 







#QUESTION FOUR

item = input("Enter a string: ")
reverse_items = item[::-1]
print("The reverse of the string is:", reverse_items)






#QUESTION FIVE
def find_unique_elements(input_list):
    unique_elements = []
    for element in elements:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements

elements = [1, 2, 3, 3, 4, 4, 5, 6, 6]
unique_elements = find_unique_elements(input_list)
