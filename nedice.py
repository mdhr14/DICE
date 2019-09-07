import random
players = ['player_one', 'madhur']
scores = {'player_one': 0, 'madhur': 0}
print('Well, hello there')
random.shuffle(players)

while True:
    for i in players:
        turn_score = 0  
        while turn_score <= 15:
            roll = random.randint(1,6)
            if roll == 1:
                turn_score = 0
                scores[i] += 0
                print('\n{} rolled a {}. Your chance is over'.format(i, roll))
                break
            else:
                turn_score += roll
                print('\n{} rolled a {}.'.format(i, roll))
        scores[i] += turn_score
        print('Turn score: {}'.format(turn_score))
        print('{} score: {} {} score: {}'.format(players[0], scores[players[0]], players[1], scores[players[1]]))
        if scores[i] > 50:
            break
    if scores[i] > 50:
        break

winner = [i for i in scores if scores[i] == max(scores.values())]
print('{} is the winner!'.format(*winner))
input()