

def start(nice=0, mean=0, name=''):
    name = describe_game(name) # getting the user's name
    nice, mean, name = nice_mean(nice, mean, name)



def describe_game(name):
    '''
    checking to see if this is a new game or not.
    If it is new, get the user's name.
    If it is not a new game, thank the player for
    playing again and continue with the game
    '''
    if name != '':
        print('\nThank you for playing again, {}!'.format(name))
    else:
        stop = True
        while stop:
            if name == '':
                name = input('\nWhat is your name? ').capitalize()
                if name != '':
                    print('\nWelcome, {}!'.format(name))
                    print('\nIn this game, you will be greeted by several different people. \nYou can be nice or mean.')
                    print('At the end of the game your fate will be influenced from your actions.')
                    stop = False
    return name


def nice_mean(nice,mean,name):
    stop = True 
    while stop:
        show_score(nice,mean,name)
        pick = input('\nA stranger approaches you for a conversation. \nWill you be nice or mean? n/m:')
        if pick == 'n':
            print('They smile, wave, and walk away...')
            nice = (nice + 1)
            stop = False
        if pick == 'm':
            print('\nThe stranger glares at you menacingly and abruptly storms off...')
            mean = (mean +1)
            stop = False
    score(nice,mean,name) # passing the 3 variables to the score function.
    

def show_score(nice, mean, name):
    print('\n{}, you currently have ({}, Nice) and ({}, Mean) points.'.format(name, nice, mean))


def score(nice, mean, name):
    # score function is being passed the values stored within the 3 variables
    if nice > 5: # ic condition is valid, call win function passing in the variables so it can use them.
        win(nice,mean, name)

    if mean > 5:
        lose(nice,mean,name)
    else:
        nice_mean(nice,mean,name)


def win(nice, mean, name):
    print('\nNice job!, you win! \nEveryone loves you and you now live in a palace!'.format(name))
    again(nice,mean,name)

def lose(nice,mean,name):
    print('\nToo bad, game over! \n{}, you live in a van by the river, wretched and alone!'.format(name))
    again(nice,mean,name)

def again(nice,mean,name):
    stop = True
    while stop:
        choice = input('\nDo you want to play again? y/m ').lower()
        if choice == 'y':
            stop = False
            reset(nice,mean,name)
        if choice == 'n':
            print('\n See ya!')
            stop = False
            exit()
        else:
            print('\nPlease enter "y" for "YES", "n" for "NO" .... ')


def reset(nice,mean,name):
    nice = 0
    mean = 0
    start(nice,mean,name)
            

    



        







if __name__ == "__main__":
    start()
    
