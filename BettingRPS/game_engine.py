from random import randrange


class BettingRPS:

    def __init__(self, n_rounds, start_chips):
        self.n_rounds = n_rounds
        self.rock = '✊'
        self.paper = '✋'
        self.scissors = '✌'
        self.hand_library = [self.rock, self.paper, self.scissors]
        self.game_hands = create_game_hands(self.hand_library, self.n_rounds)
        self.p1_chips = start_chips
        self.p2_chips = start_chips

    def play_round(self, current_round, played_hand, bet_result, bet_chips):
        game_hand = self.game_hands[current_round - 1]
        if current_round % 2 == 0:
            print(f'P1 Bets {bet_chips} chips that P2 will {bet_result}')
            self.p1_chips = self.p1_chips - bet_chips
            print(f'P2 Plays {played_hand} against {game_hand}')
            result = win_hand(played_hand, game_hand)
            if result == bet_result:
                self.p1_chips = self.p1_chips + (2 * bet_chips)
            if result == 'win':
                self.p2_chips += int(self.n_rounds/current_round)
        else:
            print(f'P2 Bets {bet_chips} chips that P1 will {bet_result}')
            self.p2_chips = self.p2_chips - bet_chips
            print(f'P1 Plays {played_hand} against {game_hand}')
            result = win_hand(played_hand, game_hand)
            if result == bet_result:
                self.p2_chips = self.p2_chips + (2 * bet_chips)
            if result == 'win':
                self.p1_chips += int(self.n_rounds / current_round)


def create_game_hands(hand_library, n_rounds):
    game_hands = [hand_library[randrange(len(hand_library))] for ind in range(n_rounds)]
    return game_hands


def win_hand(played_hand, game_hand):
    if game_hand == played_hand:
        return 'draw'
    elif game_hand == '✊':
        return 'win 'if played_hand == '✋' else 'loss'
    elif game_hand == '✋':
        return 'win 'if played_hand == '✌' else 'loss'
    elif game_hand == '✌':
        return 'win 'if played_hand == '✊' else 'loss'


if __name__ == '__main__':
    game = BettingRPS(11, 1)
    game.play_round(1, '✌', 'win', 1)
    print(f'Player 1 has {game.p1_chips}')
    print(f'Player 2 has {game.p2_chips}')
    game.play_round(2, '✋', 'draw', 1)
    print(f'Player 1 has {game.p1_chips}')
    print(f'Player 2 has {game.p2_chips}')
    