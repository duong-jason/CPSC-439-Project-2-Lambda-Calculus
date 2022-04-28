# How to make dfa with lambda calc:
# take user input and convert each binary number as an element in a list?
# If the number on the string is a 1, then the Turing Machine will simulate the DFA shown in Figure 6.3. 
# If the number on the string is a 0, then the Turing Machine will simulate the DFA shown in Figure 6.4
# based on certain positions a certain lambda function will trigger?
# return 0 if string rejects
# return 1 if string accepts
# different lambda functions are different states and depending on their input, they'll transition into another state

# input_string = input("Enter your input string: ")
# print(input_string)

# new_string = [int(a) for a in str(input_string)]
# print(new_string)

def lambda_calc(new_string):
    init_state = (lambda x: "go to 6.3" if (x == 1) else "got to 6.4") # (new_string[0])
    # print(init_state) 
    print(init_state(new_string[0]))
    # match new_string[0]:
    #     case 0:
    #         return "yes"
    #     case 1:
    #         return "no"
    #     case default:
    #         return "uhh"


def main():
    input_string = input("Enter your input string: ")
    print(input_string)

    new_string = [int(a) for a in str(input_string)]
    print(new_string)
    lambda_calc(new_string)


if __name__ == '__main__':
    main()    