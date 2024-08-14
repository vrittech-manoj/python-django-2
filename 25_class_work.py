#WAP to make a calculator ,and choices is like y/n if , user press "y" then he can add,susbtract,
        #if user input 'n' then terminate calculating process.

#WAP to take 5 input number from user and find sum of all number


while True:
    first_number = int(input("Enter first number#>>>"))
    secocnd_number = int(input("Enter Second number#>>>"))
    operator = input("Enter operator number#>>>")

    if operator == '+':
        print(first_number+secocnd_number)
    elif operator == '-':
        print(first_number-secocnd_number)
    elif operator == '*':
        print(first_number*secocnd_number)
    
    is_play  = input("Do you want to play again ? 'y/n'#>>> ")
    if is_play == 'n':
        break





