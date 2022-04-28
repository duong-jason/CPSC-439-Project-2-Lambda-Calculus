# How to make dfa with lambda calc:
# take user input and convert each binary number as an element in a list?
# If the number on the string is a 1, then the Turing Machine will simulate the DFA shown in Figure 6.3. 
# If the number on the string is a 0, then the Turing Machine will simulate the DFA shown in Figure 6.4
# based on certain positions a certain lambda function will trigger?
# return 0 if string rejects
# return 1 if string accepts
# different lambda functions are different states and depending on their input, they'll transition into another state

val0 = 0
val1 = 1

input_string = input("Enter your input string: ")
print(input_string)

new_string = [int(a) for a in str(input_string)]
print(new_string)

first = int(new_string[0])

# prints first element in list if it's the only 1 of its kind
# how to get elements of a list with lambda functions though?
init_state = next(filter(lambda x: new_string[x] == 0, new_string), None)
print(init_state)