#!/usr/bin/python3
#Pulls from a word list, creates "paragraphs" of random length, occasionally entering a blank line.

#User Inputs:
#   word list file path
#       test file, exit if bad path
#       print word count
#   file name for output
#   number of paragraphs
#   min words per paragraph (prompt user not to use zero, random blank functionality is separate)
#   max words per paragraphs

import random

#User input for the input file:
def q1():
    x = input("Enter word list full file path/name: ")
    return x
input_file = q1()

#Check for correct file path. Exit if no such file
try:
    wordlist = open(input_file, "r")
except IOError:
    print("An error was found. Either path incorrect or file doesn't exist!"
    + '\n' + "Exiting program!")
    exit()

source_count = len(open(input_file).readlines())
print("There are {} words in '{}'".format(source_count,input_file))

#Implement output file check. If exists, overwrite?
#User input for the output file:
def q2():
    x = input("Enter desired output path/name: ")
    return x
output_query = q2()

output = open(output_query, "a+")

#User input for number of paragraphs per article:
def q3():
    x = input("How many paragraphs shall we print? ")
    return x
try:
    art_length = int(q3())
except:
    print("Integers only!")
    exit()

#User input for min words per line:
def q4():
    x = input("Minimum number of words per paragraph? ")
    return x
try:
    min_w = int(q4())
except:
    print("Integers only!")
    exit()


#User input for max words per line:
def q5():
    x = input("Maximum number of words per paragraph? ")
    return x
try:
    max_w = int(q5())
except:
    print("Integers only!")
    exit()

answers = (
    '\n' + "Wordlist File: {}" + '\n' + "Words in list: {}" + '\n' + "Output File: {}" + '\n'
     + "Paragraph count: {}" + '\n' + "Min words/paragraph: {}" + '\n'
     + "Max words/paragraph: {}" + '\n' + '------------------------------------------' + '\n'
)

output.write(answers.format(input_file, source_count, output_query, art_length, min_w, max_w))

#Opens the input file, strips out the entries into a list, closes input file.
textBlock = wordlist.readlines()
master_list = []
for line in textBlock:
    master_list.append(line.strip())
wordlist.close()

#Creates num_list which will be used to pull from the master_list
def para_list():
    w_para = random.randint(min_w, max_w)
    x = []
    while w_para > 0:
        x.append(random.randint(1,source_count))
        w_para -= 1
    return x

def para_mesh():
    num_list = para_list()
    paragraph = []
    for i in num_list:
        paragraph.append(master_list[i])
    paragraph = ' '.join(paragraph).lower()
    print(paragraph + '\n')
    output.write(paragraph + '\n')

while art_length > 0:
    para_mesh()
    art_length -= 1

output.close()
