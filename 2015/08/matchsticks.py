r""" Advent of Code 2015 Day 8: Matchsticks

I solved this puzzle completely by using vim's search and replace.

Step 1: Find the total number of non-whitespace characters in the input
textfile.

The number of lines and characters are displayed when first loading the file in vim.
After editing and swapping modes, it will disappear, but a save command `:w` will get it
back.

Step 2: Search and replace according to the rules listed. Caveat: Be careful to replace
\\ first if you don't do it all in one sweep!

`:%s/\\\\\|\\"\|\\x[a-f0-9][a-f0-9]/A/g`

Subtract 2 times the line count for the string literals count.

Explanation:
    :%s/<searchpattern>/<replacepattern>/<flags>     search and replace the entire file
    \\\\    search for \\ (have to escape the backslashes)
    \|      word "or" separator 
    \\"     search for \" (again, backslash escaped)
    \|      word "or" separator
    \\x[a-f0-9][a-f0-9]
            search for \x.. where the dots are hexademical numbers, meaning
            that they can only be a-f or 0-9 (again, backslash escaped)
    A       the replacement: any single character of your liking
    g       global flag: replace all occurences

When testing the search-replace-command, I like to tack a `c` flag at the end
as well. This lets me confirm every match so I can judge whether the cases I want
to catch are caught.


Step 3: Reload the raw input file and type the following command:
`:%s/["\\]/\\\0/g`

Add 2 times the line count to the new character count for the new wrapping quotation
marks.

Explanation:
    ["\\]   search for " or \ (backslash has to be escaped)
    \\\0    replace with a backslash \ (escaped, therefore 2 of them) and the
            match \0 which would be either " or \

"""

line_count = 300
byte_count = 6502
string_literals_count = 5760 - 2*line_count 
print(f"Part 1:\t{byte_count - string_literals_count}")

new_byte_count = 7976 + 2*line_count
print(f"Part 2:\t{new_byte_count - byte_count}")
