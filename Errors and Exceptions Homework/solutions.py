# Problem 1
try:
    for i in ['a', 'b', 'c']:
        print(i**2)
except:
    # Assume a^2 = aa and so on...
    print('aa')
    print('bb')
    print('cc')

# Problem 2
x = 5
y = 0

try:
    z = x / y
except:
    # Use pass because z wouldn't be defined (keep uninitialized)
    pass
finally:
    print('All Done.')

# Problem 3
def ask():
    while True:
        x = input('Input an integer: ')
        try:
            x_sqrd = int(x) ** 2
        except:
            print('An error occurred! Please try again!')
            continue
        else:
            print('Thank you, your number squared is: {}'.format(x_sqrd))
            break

ask()