
while True:
    game_score=input("enter game score").lower().strip()
    
    if game_score== "stop":
        print("GAME ENDED!!")
        break
    else:
        game_score=int(game_score)
        if game_score>100:
            print("wow thats a new hugh score")
        else:
            print("good try keep going")    


    

