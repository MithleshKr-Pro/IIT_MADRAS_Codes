no_of_pairs = int(input())

op = 1
for _ in range(no_of_pairs):
    lines = input()
    new_list = lines.split(",")
    if op:
        print(int(new_list[0]) + int(new_list[2]))
        op = 0
    else:
        print(abs(int(new_list[0]) - int(new_list[2]))
        op = 1
        
        
# Pattern Print - N
Given an integer n (where n > 0), print an "N" shaped pattern with n rows. The pattern should have vertical bars (|) on the left and right sides of each row, with a backslash (\) moving diagonally from the top-left to the bottom-right. There should be no spaces to the right of the pattern.

NOTE: This is an I/O type question, you need to write the whole code for taking input and printing the output.

Input Format

    • A single integer n, representing the number of rows in the pattern.

Output Format

    • An "N" shaped pattern with n rows, as described.

Examples

Input:

1
Output:

|\|
Input:

2
Output:

|\ |
| \|
Input:

3
Output:

|\  |
| \ |
|  \|