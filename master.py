from textgenrnn import textgenrnn
textgen = textgenrnn()

def choice1():
    random_text = textgen.generate(1)
    return random_text
    

def choice2():
    random_text = textgen.generate_samples()
    return random_text

def f(choice):
    choices = {
        1: choice1,
        2: choice2
    }
    return choices.get(choice, "Bad option")

print("Choose an option")
print("1. Print random text")
print("2. Generate samples")
choice = int(input())
if(choice == 1):
    choice1()
else:
    choice2()