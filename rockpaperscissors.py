loxname = input('Enter your name: ')
print('Hello,', loxname)
import random

def default_game():
    global despair, loxname
    defoption = ['rock', 'paper', 'scissors']
    while True:
        userlox = input()
        comp = random.choice(defoption)
        if userlox == '!exit':
            print('Bye!')
            break
        elif userlox == '!rating':
            if loxname in despair.keys():
                print('You rating:', despair[loxname])
            else:
                print('Your rating: 0')
        elif userlox == comp:
            print(f'There is a draw ({userlox})')
            despair[loxname] += 50
            continue
        elif (userlox == 'rock' and comp == 'paper') or (userlox == 'scissors' and comp == 'rock') or (
                userlox == 'paper' and comp == 'scissors'):
            print(f'Sorry, but computer chose {comp}')
            continue
        elif userlox in defoption:
            print(f'Well done. Computer chose {comp} and failed')
            despair[loxname] += 100
            continue
        else:
            print('Invalid input')
            continue

def hardcore():
    global options, despair
    while True:
        userlox = input()
        if userlox != '!exit' and userlox != '!rating':
            magiyademenkopa = options[options.index(userlox)+1::] + options[:options.index(userlox)]
            win = magiyademenkopa[:len(magiyademenkopa) // 2]
            lose = magiyademenkopa[len(magiyademenkopa) // 2:]
        comp = random.choice(options)
        if userlox == '!exit':
            print('Bye!')
            break
        elif userlox == '!rating':
            if loxname in despair.keys():
                print('You rating:', despair[loxname])
            else:
                print('Your rating: 0')
        elif userlox == comp:
            print(f'There is a draw ({userlox})')
            despair[loxname] += 50
            continue
        elif comp in win:
            print(f'Sorry, but computer chose {comp}')
            continue
        elif comp in lose:
            print(f'Well done. Computer chose {comp} and failed')
            despair[loxname] += 100
            continue
        else:
            print('Invalid input')
            continue

punk = open('rating.txt', 'r+')
despair = dict(s.strip().split(' ', 1) for s in punk.readlines())
if loxname not in despair.keys():
    despair[loxname] = 0
for key, value in despair.items():
    despair[key] = int(value)

options = [x for x in input().split(',')]
print('Okay, let\'s start')
if options[0] == '':
    default_game()
else:
    hardcore()

punk.close()