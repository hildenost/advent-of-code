#! /bin/sh

# Advent of Code 2015 Day 8: Matchsticks

# The more suitable shell script solution, compatible on Unix shells (because I
# checked it on shellcheck.net).

# First, storing the original number of characters
original=$(wc -c < input.txt)
# And the number of lines
line_count=$(wc -l < input.txt)

# PART 1
# Find the difference in total number of characters minus the number of
# string literals

string_literals=$(sed 's/\\\\\|\\"\|\\x[a-f0-9][a-f0-9]/A/g' input.txt | wc -c)

# Subtract 2 times the line count to eliminate the line wrapping quotation marks
# for the string literals count.
echo Part 1: $((original - (string_literals - 2*line_count)))

# Explanation:
#    sed 's/<search>/<replace>/<flags>' <file>
#		Basic search and replace in sed. I don't want to alter the
#     	 	input file, so I left the option -i out.
#    <sed_expression> | wc -c
#		Pipes the output from the sed command, which is the altered
#		text of the file, to the wordcount command wc with the -c
#		option to count the number of bytes in the file.
#    \\\\    	search for \\ (have to escape the backslashes)
#    \|      	word "or" separator
#    \\"     	search for \" (again, backslash escaped)
#    \|      	word "or" separator
#    \\x[a-f0-9][a-f0-9]
#            	search for \x.. where the dots are hexademical numbers, meaning
#            	that they can only be a-f or 0-9 (again, backslash escaped)
#    A       	the replacement: any single character of your liking
#    g       	global flag: replace all occurences

# PART 2
# Find the difference between the extra escaped input text and the original text

extra_escape=$(sed 's/["\\]/\\\0/g' input.txt | wc -c)

# Add 2 times the line count to account for the line wrapping quotation marks
# for the extra escaped count.
echo Part 2: $((extra_escape + 2*line_count - original))

# Explanation:
#    ["\\]   	search for " or \ (backslash has to be escaped)
#    \\\0    	replace with a backslash \ (escaped, therefore 2 of them) and the
#            	match \0 which would be either " or \
