import json
import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def ask_algebra():
    number1 = random.choice(numbers)
    number2 = random.choice(numbers)
    choice = random.randint(1, 3)
    if choice == 1:
        return (f"What is {number1} + {number2}?: ", number1 + number2)
    elif choice == 2:
        return (f"What is {number1} - {number2}?: ", number1 - number2)
    elif choice == 3:
        return (f"What is {number1} * {number2}?: ", number1 * number2)

def ask_financial_literacy():
    choice = random.randint(1, 3)
    if choice == 1:
        total = random.randint(0, 500)
        percent = random.randint(0,50)
        correct = round(total * percent / 100, 2)
        return (f"If something costs ${total} and taxes are {percent}%, how much is the tax?: ",correct)
    elif choice == 2:
        save = random.randint(1, 1000)
        months = random.randint(1, 12)
        correct = int(save / months)
        return (f"If you save ${save} over {months} months, how much do you save per month?: ", correct)
    elif choice == 3:
        percent = random.randint(1, 50)
        num = random.randint(1, 300)
        correct = round(num * percent / 100, 2)
        return (f"What is {percent}% of {num}?: ", correct)

def ask_calculus():
    number1 = random.choice(numbers)
    number2 = random.choice(numbers)
    choice = random.randint(1, 3)
    if choice == 1:
        slope = random.randint(1, 10)
        correct = slope
        return (f"What is the slope of y = {slope}x + {number2}?: ", correct)
    elif choice == 2:
        correct = number1 * 2
        return (f"What is the derivative of x^2 multiplied by {number1}?: ", correct)
    elif choice == 3:
        correct = number1 * number2
        return (f"What is the limit of {number1}x as x approaches {number2}?: ", correct)

question_functions = {
    'Algebra 101': ask_algebra,
    'Financial Literacy 111': ask_financial_literacy,
    'Calculus': ask_calculus
}

def run_assessment(current_class):
    check = input("Have you taken this class assessment before? ").strip().lower()
    if check == 'yes':
        try:
            with open(f'/tmp/gradebook_{current_class}.json', 'r') as file:
                gradebook = json.load(file)
                print()
                print(f"Your previous score was: {gradebook['score']}, you {gradebook['grade']}, and you must {gradebook['next_step']}.")
                print()
        except FileNotFoundError:
            print("No previous grade found. Let's start fresh!")
            print()
        runback = input("Do you want to retake the assessment? (yes/no) ").strip().lower()
        if runback == 'no':
            print()
            print("Okay, you can come back later!")
            print()
            return
        else:
            print()
            print("Great! Let's retake the assessment.")
            print()
    elif check == 'no':
        print()
        print("Okay then! Let's get started!")
        print()
    else:
        print("Please enter a valid response (yes or no).")


    ready = input(f"Welcome to {current_class}! Want to test your skills? ").strip().lower()
    if ready == 'no':
        print()
        print("Alright, I'll be waiting!")
        print()
    elif ready not in ['yes', 'no']:
        print()
        print("Please enter a valid response (yes or no).")
        print()

    ask_question = question_functions[current_class]
    counter = 0

    for i in range(10):
        question, correct_answer = ask_question()
        try:
            answer = round(float(input(question)), 2)
        except ValueError:
            print("Please enter a valid number.")
            continue
        if answer == correct_answer:
            print("Correct!")
            counter += 1
        else:
            print("Wrong!")

    print()
    print(f"You got {counter} correct answers out of 10 ({counter/10*100:.0f}%).")

    if counter >= 7:
        grade_status = 'Passed'
        next_step = 'move on to the next class'
    else:
        grade_status = 'Failed'
        next_step = 'retake the assessment'

    print(f"Your status on this class is {grade_status}. Here is your next move: {next_step}.")

    with open(f'/tmp/gradebook_{current_class}.json', 'w') as file:
        json.dump({'score': counter, 'grade': grade_status, 'next_step': next_step}, file)
    print("Progress saved!")
    return True

dtl = '*'
print(dtl * 30)
print("Welcome to Math Class!".center(30))
print(dtl * 30)

while True:
    classes = list(question_functions.keys())
    print()
    print("Here are our available classes in order: " + ", ".join(classes))
    print()
    current_class = input("What class are you being assessed on? ").title().strip()
    print()

    if not current_class or current_class.isdigit():
        print("Please enter a valid class name.")
        continue
    if current_class in classes:
        complete = run_assessment(current_class)
        if complete:
            break
    else:
        print("Invalid class name. Please choose from the available classes.")