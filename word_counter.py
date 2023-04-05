if __name__ == '__main__':
    print('..Loading word counter..\n')  # intro comment

# define word tally function
def word_tally(input_text):
    tally = dict()  # create empty dictionary
    input_text = input_text.lower().split()  # split on whitespace and make lowercase
    for word in input_text: # tally counts of words
        tally[word] = tally.get(word, 0) + 1
    max_count = 0
    most_common = None
    for word, value in tally.items():  # determine most common word by number of counts
        if value > max_count:
            max_count = value
            most_common = word
    return print(f"Most common word is {most_common} with {max_count} occurrences.")


# print description for script
print("Result will not be case-sensitive.")
print("Input can be typed text or a file within the same directory.")
option = input("Type your input choice as 'text' or a 'file': ")  # determine input type
if option.lower() == 'text':
    text = input("Please paste or type text here: ")  # take text input
    word_tally(text)
elif option.lower() == 'file':
    filename = input("Please enter filename here: ")  # take filename input to open
    try:  # attempt to open filename
        handle = open(filename)
        text = ""
        for line in handle:
            text += line.rstrip()
        word_tally(text)
    except FileNotFoundError:  # Error exit if file not opened
        print("Unable to open file, exiting program")
        quit()
else:
    print("Invalid choice, exiting program.")
