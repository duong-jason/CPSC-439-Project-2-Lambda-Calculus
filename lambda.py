#!/usr/bin/env python3
# CPSC 439-01 (Spring 2022) Project 2: Lambda Calculus

# Group Members: 
# Bradley Diep
# John Dinh 
# Jason Duong
# Omid Nikjoo

import sys

def state_q0(input_string):
    new_string = input_string[1:] # remove first character of string
    # print(new_string) # prints list without the first element

    init_state = (lambda x: state_q1(new_string) if (x == 0) else state_q5(new_string)) # (new_string[0])
    # print(init_state) 
    print(init_state(input_string[0]))


# # leads to Figure 6.4
def state_q1(input_string):
    if not len(input_string):
        sys.exit('1') # 1 shows that it's an accepted string
        # return 1 
    else:
        new_string = input_string[1:]
        s1 = (lambda x: state_q3(new_string) if (x == 0) else state_q4(new_string))
        print(s1(input_string[0]))


def state_q2(input_string):
    if not len(input_string):
        # return 0 
        sys.exit('0') # 0 shows that it's a rejected string
    else:
        new_string = input_string[1:]
        s2 = (lambda x: state_q1(new_string) if (x == 0) else state_q4(new_string))
        print(s2(input_string[0]))


def state_q3(input_string):
    if not len(input_string):
        # return 0 
        sys.exit('0') # 0 shows that it's a rejected string
    else:
        new_string = input_string[1:]
        s3 = (lambda x: state_q1(new_string) if (x == 0) else state_q2(new_string))
        print(s3(input_string[0]))


def state_q4(input_string):
    if not len(input_string):
        # return 0 
        sys.exit('0') # 0 shows that it's a rejected string
    else:
        new_string = input_string[1:]
        s4 = (lambda x: state_q4(new_string) if (x == 0) else state_q4(new_string))
        print(s4(input_string[0]))


# # leads to Figure 6.3
def state_q5(input_string):
    if not len(input_string):
        # return 0 
        sys.exit('0') # 0 shows that it's a rejected string
    else:
        new_string = input_string[1:]
        s5 = (lambda x: state_q5(new_string) if (x == 0) else state_q6(new_string))
        print(s5(input_string[0]))


def state_q6(input_string):
    if not len(input_string):
        # return 1 
        sys.exit('1') # 1 shows that it's an accepted string
    else:
        new_string = input_string[1:]
        s6 = (lambda x: state_q6(new_string) if (x == 0) else state_q5(new_string))
        print(s6(input_string[0]))


def main():
    value = input("please say which number you want to test out (100, 1010, 1, 10110, 10000011)\n")
    value += ".txt"
    data = open("testfiles/" + value, "r")
    input_string = data.read()

    if ("0" in input_string or "1" in input_string):
        input_string = [int(a) for a in input_string]
        state_q0(input_string)
    else:
        print("This isn't a binary string.")

if __name__ == '__main__':
    main()
