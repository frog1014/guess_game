
# start the game
import random
print('Welcome to the guess name')
attempt = 1

def run_game(guess_num, corr_num):
    global attempt
    if guess_num == corr_num:

        print(f'************\nGood job!! you got the right number: {corr_num}\n attempt: {attempt}\n*********')
        return True
    else:
        attempt += 1
        print("try again! \n")
        return False

def min_max(min_num,max_num):
    if max_num < min_num:
        print("your max num less than min, do again.. ")
        return True
    else:
        corr_num = random.randint(min_num, max_num)
        return corr_num


# game on



if __name__ == '__main__':

    while True:
        new_game = input("start a new game? y/n  ")
        if new_game.lower() not in ('y', 'yes', 'n', 'not'):
            print("insert the y or n only")
            continue
        elif new_game.lower() in ('n', 'no'):
            print('\nsee you next time')
            break
        else:




            # input min max number
            while True:
                try:
                    min_num = int(input("insert the min number "))
                except:
                    print("insert the number only")
                    continue
                try:
                    max_num = int(input("insert the max number "))
                except:
                    print("insert the number only")
                    continue

                corr_num = min_max(min_num,max_num)





            # guess the number and check



                while True:

                    try:
                        guess_num = int(input("guess the number "))
                    except:
                        print("insert number only")
                        continue

                    if (run_game(guess_num, corr_num)):
                        break
                    else:
                        continue

                break




