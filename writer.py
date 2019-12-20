#!/usr/bin/python3
#Pulls from a word list, creates "sentences" of random length, occasionally entering a blank line.

#User Inputs:
#   word list file path
#       test file, exit if bad path
#       print word count
#   file name for output
#   number of lines
#   min words per line (prompt user not to use zero, random blank functionality is separate)
#   max words per line
#   randomly include lines of zero words? Y/n? (implement as an option later, start as default)
#   frequency of random blank lines, max number for random generator

import random


min_w = 5
max_w = 10

a1 = "Wordlist File: {}"
a2 = "Output File: {}"
a3 = "Line count: {}"
a4 = "Min words/line: {}"
a5 = "Max words/line: {}"

#User input for the wordlist file:
def q1():
    x = input("Enter word list full file path/name: ")
    return x
list_file = q1()

#print(a1.format(list_file))

#Check for correct file path. Exit if no such file
try:
    wordlist = open(list_file, "r")
except IOError:
    print("An error was found. Either path incorrect or file doesn't exist!" + '\n' + "Exiting program!")
    exit()

#Implement output file check. If exists, overwrite?
#User input for the output file:
def q2():
    x = input("Enter desired output path/name: ")
    return x
output_query = q2()

#print(a2.format(output))

output = open(output_query, "a+")

#User input for number of lines per article:
def q3():
    x = input("How many lines shall we print? ")
    return x
try:
    art_length = int(q3())
except:
    print("Integers only!")
    exit()

source_count = len(open(list_file).readlines())
print("There are {} words in '{}'".format(source_count,list_file))
output.write("There are {} words in '{}'".format(source_count,list_file) + '\n')

#write in a way to skip the blank line generator for the first line
while art_length > 0:
    blank_gen = random.randint(1,15)
    if blank_gen == 1:
        print("")
        output.write('\n')
        art_length -= 1
    else:
        w_line = random.randint(min_w, max_w)
        new_line = []
        while w_line > 0:
            new_line.append(random.randint(1,source_count))
            w_line -= 1
        print(new_line)
        output.write(' '.join(str(x) for x in new_line) + '\n')
        art_length -= 1

#turning number list into words
#def list_into_line([numbers]):

wordlist.close()
output.close()
output.close()
