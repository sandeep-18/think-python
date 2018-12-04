# Sandeep Sadarangani 4/12/18
# Print input until 'done' command is signalled
# Use the - break - keyword

def repeater():
    while True:
        line = input("> ")
        if line == 'done':
            print("Program Done!")
            break
        print(line)
        

print("Enter anything!")
repeater()
        