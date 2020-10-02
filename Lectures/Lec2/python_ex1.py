print("Python is fun!")

message = "python is fun"
print(message)

name = "fernando romero galvan"
print(name.title())

first_name = 'Fernando'
last_name = 'Romero Galvan'

full_name = f"{first_name} {last_name}"

print(full_name)

print(f"My name is, {full_name.title()}!")

# Lists
states = ['California', 'Florida', 'Hawaii']
print(states)

print(states[0])

states[0] = 'New York' # Value changed at index 0
print(states) # confirmed

states.insert(0,'Alaska') # Add element
print(states)
popped_states = states.pop(1) # Remote element
print(popped_states)
print(states)

# Loops
for state in states:
    print(state)
    print("All states in list printed")

# Loops + Ifs
for state in states:
    if state == 'Alaska':
        print(state.upper())
    elif state == 'New York':
        print(state.lower())
    else:
        print(state.title())

# Dictionaries
plants = {'color':'blue', 'height': 10}
print(plants['color'])
plants['sepal'] = 3
print(plants)
del plants['color']
print(plants)

def weather():
    answer = input("How's the weather?")
    print(answer)

weather() # Calls for user input and prints what the user responded with.

# reading in file
fasta_file = open("/home/bioinfo/Data/sample1.fasta", "r")
if fasta_file.mode == "r":
    contents = fasta_file.read()
    outF = open("/home/bioinfo/Data/test_out.fasta","w")
    outF.write(contents)

fasta_file.close()
outF.close()
