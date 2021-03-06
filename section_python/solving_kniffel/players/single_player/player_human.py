
# the human agent, played through cmd
# .exe is generated using pyinstaller

import game_copy as game


def PlayerGame(game):
    game = game.Kniffel()
    
    while None in game.block_status.values():
        dice = game.PlayerRoll(game.InitialRoll(), 1)  # move 1
        dice = game.PlayerRoll(dice, 2)                # move 2
        game.PlayerBox(dice)                           # box choice

    score = sum(filter(None, game.block_status.values()))

    print('************')
    print(' Game Over ')
    print(' Score : {} '.format(score))
    print('************')
    print('')
    
    input('restart the .exe to play another game')
    while True:
        pass
    
    
if __name__ == '__main__':
    PlayerGame(game)