from random import randrange


class BettingRPS:

    def __init__(self, n_rounds: int):
        self.n_rounds = n_rounds
        self.rock = '✊'
        self.paper = '✋'
        self.scissors = '✌'
        self.hand_library = [self.rock, self.paper, self.scissors]
        self.game_hands = create_game_hands(self.hand_library, self.n_rounds)
        self.p1_chips = 1
        self.p2_chips = 1
        self.log = []
        self.log.append(f'Game started with {n_rounds} rounds \n')
        self.current_round = 1
        self.hand_played = None
        self.bet_chips = None
        self.bet_result = None

    def new_game(self, n_rounds: int):
        self.n_rounds = n_rounds
        self.game_hands = create_game_hands(self.hand_library, self.n_rounds)
        self.p1_chips = 1
        self.p2_chips = 1
        self.log = []
        self.log.append(f'Game started with {n_rounds} rounds \n')
        self.current_round = 1
        self.hand_played = None
        self.bet_chips = None
        self.bet_result = None

    def play_round(self, played_hand: str, bet_result: str, bet_chips: int):
        if self.current_round < self.n_rounds:
            self.log.append(f'Round {self.current_round}: \n')
            game_hand = self.game_hands[self.current_round - 1]
            if self.current_round % 2 == 0:
                self.log.append(f'P1 Bets {bet_chips} chips that P2 will {bet_result} \n')
                result = win_hand(played_hand, game_hand)
                self.log.append(f'P2 Plays {played_hand} against {game_hand} resulting in a {result}\n')
                if result == bet_result:
                    self.p1_chips += bet_chips
                else:
                    self.p1_chips -= bet_chips
                if result == 'win':
                    self.p2_chips += int(self.current_round / 3) + 1
            else:
                self.log.append(f'P2 Bets {bet_chips} chips that P1 will {bet_result} \n')
                result = win_hand(played_hand, game_hand)
                self.log.append(f'P1 Plays {played_hand} against {game_hand} resulting in a {result}\n')
                if result == bet_result:
                    self.p2_chips += bet_chips
                else:
                    self.p2_chips -= bet_chips
                if result == 'win':
                    self.p1_chips += int(self.current_round / 3) + 1
            self.log.append(f'Chips: P1 = {self.p1_chips}, P2 = {self.p2_chips} \n')
            self.current_round += 1
            self.hand_played = None
            self.bet_chips = None
            self.bet_result = None
        else:
            pass

    def show_log(self):
        return ''.join(self.log)


def create_game_hands(hand_library: list, n_rounds: int):
    game_hands = [hand_library[randrange(len(hand_library))] for ind in range(n_rounds)]
    return game_hands


def win_hand(played_hand: str, game_hand: str):
    if game_hand == played_hand:
        return 'draw'
    elif game_hand == '✊':
        return 'win' if played_hand == '✋' else 'lose'
    elif game_hand == '✋':
        return 'win' if played_hand == '✌' else 'lose'
    elif game_hand == '✌':
        return 'win' if played_hand == '✊' else 'lose'


if __name__ == '__main__':
    game = BettingRPS(11)
    game.play_round('✌', 'win', game.p2_chips)
    game.play_round('✊', 'draw', game.p1_chips)
    game.play_round('✋', 'lose', game.p2_chips)
    game.play_round('✌', 'draw', game.p1_chips)
    print(game.show_log())
