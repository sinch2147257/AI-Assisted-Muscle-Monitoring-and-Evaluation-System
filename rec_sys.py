import random
print("Starting System")
playing_first = True

rec_list = ["mario right hand","mario left hand","dino left arm","dino right arm"]


def start_mario_r():
    print("starting mario right")
    rand = random.randint(0,3)
    if rand == 0:
        return 0
    elif rand == 1:
        return 1
    else:
        return 2
def start_mario_l():
    print("starting mario left")
    rand = random.randint(0,3)
    if rand == 0:
        return 0
    elif rand == 1:
        return 1
    else:
        return 2
def dino_l():
    print("starting dino left arm")
    rand = random.randint(0,3)
    if rand == 0:
        return 0
    elif rand == 1:
        return 1
    else:
        return 2
def dino_r():
    print("starting dino right arm")
    rand = random.randint(0,3)
    if rand == 0:
        return 0
    else:
        return 1

def start_new_rec(rec_result,g_choice):
    if rec_result==1:
        print("List recommendation for low")
        if g_choice == 0:
            print("R: Right Thump game game")
        if g_choice == 1:
            print("R: Right Thump game")
    else:
        print("List recommendation for high")
        if g_choice == 0:
            print("R: Dino elbow")

if playing_first:
    print("Primary Recommendation")
    game_choice = random.randint(0,3)
    prim_game = rec_list[game_choice]
    print(prim_game)
    result = 0
    if game_choice==0:
        result = start_mario_l()
    elif game_choice==1:
        result = start_mario_r()
    elif game_choice==2:
        result = dino_l()
    elif game_choice==3:
        result = dino_r()
    start_new_rec(result,game_choice)

    

    



