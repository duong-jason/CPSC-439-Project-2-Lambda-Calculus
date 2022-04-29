# CPSC 439-01 (Spring 2022) Project 2: Lambda Calculus

# Group Members: 
# Bradley Diep
# John Dinh - 
# Jason Duong
# Omid Nikjoo


def state_q0(input_string):
    new_string = input_string[1:] # remove first character of string
    # print(new_string) # prints list without the first element

    init_state = (lambda x: state_q1(new_string) if (x == 0) else state_q5(new_string)) # (new_string[0])
    # print(init_state) 
    print(init_state(input_string[0]))
    
    
# # leads to Figure 6.4
def state_q1(input_string): 
    if(len(input_string) == 0):
        return 1 # return 1 bc accepted
    else:
        new_string = input_string[1:]
        # print(new_string)
        s1 = (lambda x: state_q3(new_string) if (x == 0) else state_q4(new_string))
        print(s1(input_string[0]))
    
    
def state_q2(input_string):
    if (len(input_string) == 0):
        return 0 # return 0 bc not accepted
    else:
        new_string = input_string[1:]
        # print(new_string)
        s2 = (lambda x: state_q1(new_string) if (x == 0) else state_q4(new_string))
        print(s2(input_string[0]))
    
    
def state_q3(input_string):
    if (len(input_string) == 0):
        return 0 # return 0 bc not accepted
    else:
        new_string = input_string[1:]
        # print(new_string)
        s3 = (lambda x: state_q1(new_string) if (x == 0) else state_q2(new_string))
        print(s3(input_string[0]))
    

def state_q4(input_string):
    if (len(input_string) == 0):
        return 0 # return 0 bc not accepted
    else:
        new_string = input_string[1:]
        # print(new_string)
        s4 = (lambda x: state_q4(new_string) if (x == 0) else state_q4(new_string))
        print(s4(input_string[0]))
    
    
# # leads to Figure 6.3
def state_q5(input_string): 
    if (len(input_string) == 0):
        return 0 # return 0 bc not accepted
    else:
        new_string = input_string[1:] 
        # print(new_string) 
        s5 = (lambda x: state_q5(new_string) if (x == 0) else state_q6(new_string))
        print(s5(input_string[0]))
        
    
def state_q6(input_string): 
    if (len(input_string) == 0):
        return 1 # return 1 bc accepted
    else:
        new_string = input_string[1:] 
        # print(new_string) 
        s6 = (lambda x: state_q6(new_string) if (x == 0) else state_q5(new_string))
        print(s6(input_string[0]))


def main():
    input_string = input("Enter your input string: ")

    input_string = [int(a) for a in str(input_string)]
    # print(input_string)
    state_q0(input_string)


if __name__ == '__main__':
    main()    