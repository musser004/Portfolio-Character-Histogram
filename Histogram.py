# Application checks how many times a letter appears in a given text file, sorts the list by character frequency,
# then outputs the results to a file and makes a bar chart as well

import matplotlib.pyplot as plt

# Use "test.txt", or any other txt file you have in the working directory
# User is asked for the file they want to use, and it is then opened in "read" mode, text copied to variable, and closed

answer = input('Please enter the file name (excluding the ".txt" file extension): ')
file = open(f"{answer}.txt", mode="r")
histogram = file.read()
file.close()

# Initial alphabet dictionary setup

letter_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"]
letter_dict = {}
for letter in letter_list:
    letter_dict[letter] = 0

# Running through the entirety of the file contents (string), adding +1 for each instance of a given letter. If a
# non-alphabetical character is found, the KeyError is ignored and the for loop continues

for char in histogram.lower():
    try:
        letter_dict[char] += 1
    except KeyError:
        continue

# List is sorted from most instances to least

sorted_letter_list = sorted(letter_dict.items(), key=lambda x: x[1], reverse=True)

# File output prepared with the given letter and the number of instances found

file_output = []
for x in range(len(sorted_letter_list)):
    file_output.append(f"{sorted_letter_list[x][0]} -> {sorted_letter_list[x][1]}\n")

# File output

file1 = open(f"{answer}.hist.txt", mode="w")
file1.writelines(file_output)
file1.close()

# Converting list to dictionary for the bar chart, using dictionary comprehension

sorted_letter_dict = {x[0]: x[1] for x in sorted_letter_list}

# Matplotlib bar chart to show number of instances per letter

plt.figure(figsize=(8, 4), dpi=200)
plt.bar(sorted_letter_dict.keys(),
             sorted_letter_dict.values())
plt.xlabel('Letter')
plt.ylabel('Number of Instances in File')
plt.title('Letter Bar Chart')
plt.show()
