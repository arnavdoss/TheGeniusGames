from dash import Dash, html, dcc, Input, Output, State, callback_context, ALL, no_update
import dash_bootstrap_components as dbc
import jsonpickle
from BettingRPS.game_engine import BettingRPS
from app import app
import os

# Initialize app
# app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY], title='BettingRPS', update_title=None,
#            meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}])
# CYBORG, DARKLY, SLATE, SOLAR, SUPERHERO, VAPOR, QUARTZ,

# IDs
rock = '✊'
paper = '✋'
scissors = '✌'
ok = '👌'
thumbs_up = '👍'
thumbs_down = '👎'
draw = '👊'
up = '☝'
down = '👇'
id_game_hands_wrapper = 'id_game_hands_wrapper'
id_game_hands = 'id_game_hands'
id_next_round = 'id_next_round'
id_p1_chips = 'id_p1_chips'
id_p2_chips = 'id_p2_chips'
id_game_log = 'id_game_log'
id_new_game = 'id_new_game'
id_show_log = 'id_show_log'
id_modal_log = 'id_modal_log'
id_p1_inputs = 'id_p1_inputs'
id_p2_inputs = 'id_p2_inputs'
id_play_rock = 'id_play_rock'
id_play_paper = 'id_play_paper'
id_play_scissors = 'id_play_scissors'
id_play_confirm = 'id_play_confirm'
id_bet_inc = 'id_bet_inc'
id_bet_val = 'id_bet_val'
id_bet_dec = 'id_bet_dec'
id_bet_confirm = 'id_bet_confirm'
id_bet_input = 'id_bet_input'
id_play_input = 'id_play_input'
id_bet_win = 'id_bet_win'
id_bet_draw = 'id_bet_draw'
id_bet_lose = 'id_bet_lose'
id_bet_result_confirm = 'id_bet_result_confirm'
id_bet_result_input = 'id_bet_result_input'
id_game_store = 'id_game_store'
id_p1_collapse = 'id_p1_collapse'
id_p2_collapse = 'id_p2_collapse'
id_player_collapse = 'id_player_collapse'
id_p1_button = 'id_p1_button'
id_p2_button = 'id_p2_button'
id_sync_timer = 'id_sync_timer'
sync_file_path = 'betting_rps.txt'


def game_hand_display(game):
    game_hand = game.game_hands
    curr_r = game.current_round
    current_hand = dbc.ButtonGroup([
        dbc.Button([html.H1(f'Round {curr_r}')], outline=False, color='primary', disabled=False),
        dbc.Button([html.H1(game_hand[curr_r - 1])], outline=False, color='primary', disabled=False),
    ], style={'width': '100%'})
    print(game.game_hands)
    return html.Div(current_hand)


play_hand_inputs = dbc.Row([
    dbc.ButtonGroup([
        dbc.Button(rock, id=id_play_rock, style={'fontSize': '10vh'}, outline=True, color='secondary'),
        dbc.Button(paper, id=id_play_paper, style={'fontSize': '10vh'}, outline=True, color='secondary'),
        dbc.Button(scissors, id=id_play_scissors, style={'fontSize': '10vh'}, outline=True, color='secondary'),
        dbc.Button(ok, id=id_play_confirm, style={'fontSize': '10vh'}, outline=True, color='success'),
    ], vertical=True, style={'height': '90%'})
], align='center', justify='center', style={'height': '70vh'})

bet_inputs = dbc.Row([
    dbc.ButtonGroup([
        dbc.Button(up, id=id_bet_inc, style={'fontSize': '10vh'}, outline=True, color='secondary'),
        dbc.Button(0, id=id_bet_val, style={'fontSize': '10vh'}, outline=True, color='secondary'),
        dbc.Button(down, id=id_bet_dec, style={'fontSize': '10vh'}, outline=True, color='secondary'),
        dbc.Button(ok, id=id_bet_confirm, style={'fontSize': '10vh'}, outline=True, color='success'),
    ], vertical=True, style={'height': '90%'})
], align='center', justify='center', style={'height': '70vh'})

bet_hand_inputs = dbc.Row([
    dbc.ButtonGroup([
        dbc.Button(thumbs_up, id=id_bet_win, style={'fontSize': '10vh'}, outline=True, color='secondary'),
        dbc.Button(draw, id=id_bet_draw, style={'fontSize': '10vh'}, outline=True, color='secondary'),
        dbc.Button(thumbs_down, id=id_bet_lose, style={'fontSize': '10vh'}, outline=True, color='secondary'),
        dbc.Button(ok, id=id_bet_result_confirm, style={'fontSize': '10vh'}, outline=True, color='success'),
    ], vertical=True, style={'height': '90%'})
], align='center', justify='center', style={'height': '70vh'})

# Layout
layout = dbc.Container([
    dbc.Row([
        dbc.ButtonGroup([
            dbc.Button('Next Round', id=id_next_round),
            dbc.Button('New Game', id=id_new_game),
            dbc.Button('Show Log', id=id_show_log),
        ]),
        dbc.Modal([
            dbc.ModalBody([], id=id_game_log, style={'white-space': 'pre-wrap'})
        ], id=id_modal_log)
    ]),
    html.Br(),
    dbc.Row([
        html.Div([], id=id_game_hands_wrapper),
    ]),
    dcc.Interval(interval=500, id=id_sync_timer),
    dcc.Store(id=id_game_store, data=jsonpickle.encode(BettingRPS(11))),
    dcc.Store(id=id_bet_input, data=0),
    dcc.Store(id=id_play_input, data=None),
    dcc.Store(id=id_bet_result_input, data=None),
    html.Br(),
    dbc.Row([
        dbc.Collapse([
            dbc.ButtonGroup([
                dbc.Button('1', id=id_p1_button, outline=True, color='primary'),
                dbc.Button('2', id=id_p2_button, outline=True, color='primary')
            ])
        ], id=id_player_collapse, is_open=True)
    ]),
    dbc.Row([
        dbc.Collapse([
            dbc.Col([
                html.H1(0, id=id_p1_chips, style={'fontSize': '10vh'})
            ], width=12, align='center'),
            dbc.Col([
                html.Div(dbc.Row([dbc.Col(bet_inputs, width=6), dbc.Col(bet_hand_inputs, width=6)]), id=id_p1_inputs)
            ], width=12),
        ], id=id_p1_collapse, is_open=False),
    ]),
    dbc.Row([
        dbc.Collapse([
            dbc.Col([
                html.H1(0, id=id_p2_chips, style={'fontSize': '10vh'})
            ], width=12, align='center'),
            dbc.Col([
                html.Div(play_hand_inputs, id=id_p2_inputs)
            ], width=12)
        ], id=id_p2_collapse, is_open=False),
    ]),
], fluid=True)


# Callbacks
@app.callback(
    [Output(id_player_collapse, 'is_open'), Output(id_p1_collapse, 'is_open'), Output(id_p2_collapse, 'is_open')],
    [Input(id_p1_button, 'n_clicks'), Input(id_p2_button, 'n_clicks')], prevent_initial_call=True
)
def choose_player(n1, n2):
    call_id = callback_context.triggered[0]['prop_id'].split('.')[0]
    if call_id == id_p1_button:
        return [False, True, False]
    elif call_id == id_p2_button:
        return [False, False, True]
    else:
        return [no_update, no_update, no_update]


@app.callback(
    [Output(id_game_hands_wrapper, 'children'), Output(id_p1_chips, 'children'), Output(id_p2_chips, 'children'),
     Output(id_p1_inputs, 'children'), Output(id_p2_inputs, 'children')],
    [Input(id_new_game, 'n_clicks'), Input(id_game_store, 'data')],
)
def play_round(n, game):
    game = jsonpickle.decode(game)
    call_id = callback_context.triggered[0]['prop_id'].split('.')[0]
    p1_state = no_update
    p2_state = no_update
    if call_id == id_new_game or call_id == '':
        game = BettingRPS(11)
        with open(sync_file_path, 'w') as outfile:
            outfile.write(jsonpickle.encode(game))
        p2_state = dbc.Row([dbc.Col(bet_inputs, width=6), dbc.Col(bet_hand_inputs, width=6)])
        p1_state = play_hand_inputs
    elif game.current_round <= game.n_rounds:
        if game.hand_played is not None and game.bet_chips is not None and game.bet_result is not None:
            game.play_round(game.hand_played, game.bet_result, game.bet_chips)
            with open(sync_file_path, 'w') as outfile:
                outfile.write(jsonpickle.encode(game))
            if game.current_round % 2 == 0:
                p1_state = dbc.Row([dbc.Col(bet_inputs, width=6), dbc.Col(bet_hand_inputs, width=6)])
                p2_state = play_hand_inputs
            else:
                p2_state = dbc.Row([dbc.Col(bet_inputs, width=6), dbc.Col(bet_hand_inputs, width=6)])
                p1_state = play_hand_inputs
    return [game_hand_display(game), game.p1_chips, game.p2_chips, p1_state, p2_state]


@app.callback(Output(id_game_store, 'data'), Input(id_sync_timer, 'n_intervals'))
def sync_game(n):
    with open(sync_file_path, 'r') as infile:
        game_json = infile.read()
    return game_json


@app.callback([Output(id_modal_log, 'is_open'), Output(id_game_log, 'children')], Input(id_show_log, 'n_clicks'),
              State(id_game_store, 'data'))
def show_log(n, game):
    game = jsonpickle.decode(game)
    return [True, game.log]


@app.callback(
    [Output(id_play_rock, 'active'), Output(id_play_paper, 'active'), Output(id_play_scissors, 'active'),
     Output(id_play_confirm, 'active'), Output(id_play_confirm, 'disabled'), Output(id_play_input, 'data')],
    [Input(id_play_rock, 'n_clicks'), Input(id_play_paper, 'n_clicks'), Input(id_play_scissors, 'n_clicks'),
     Input(id_play_confirm, 'n_clicks'), Input(id_next_round, 'n_clicks'), Input(id_new_game, 'n_clicks')],
    [State(id_play_input, 'data'), State(id_game_store, 'data')], prevent_initial_call=True
)
def active_play_hand_buttons(n1, n2, n3, n4, n5, n6, play_input, game_data):
    game = jsonpickle.decode(game_data)
    call_id = callback_context.triggered[0]['prop_id'].split('.')[0]
    if call_id == id_play_confirm:
        game.hand_played = play_input
        with open(sync_file_path, 'w') as outfile:
            outfile.write(jsonpickle.encode(game))
        return [False, False, False, True, False, play_input]
    elif call_id == id_play_rock:
        return [True, False, False, False, False, rock]
    elif call_id == id_play_paper:
        return [False, True, False, False, False, paper]
    elif call_id == id_play_scissors:
        return [False, False, True, False, False, scissors]
    else:
        return [False, False, False, False, True, None]


@app.callback(
    [Output(id_bet_win, 'active'), Output(id_bet_draw, 'active'), Output(id_bet_lose, 'active'),
     Output(id_bet_result_confirm, 'active'), Output(id_bet_result_confirm, 'disabled'),
     Output(id_bet_result_input, 'data')],
    [Input(id_bet_win, 'n_clicks'), Input(id_bet_draw, 'n_clicks'), Input(id_bet_lose, 'n_clicks'),
     Input(id_bet_result_confirm, 'n_clicks'), Input(id_next_round, 'n_clicks'), Input(id_new_game, 'n_clicks')],
    [State(id_bet_result_input, 'data'), State(id_game_store, 'data')], prevent_initial_call=True
)
def active_play_hand_buttons(n1, n2, n3, n4, n5, n6, play_input, game_data):
    game = jsonpickle.decode(game_data)
    call_id = callback_context.triggered[0]['prop_id'].split('.')[0]
    if call_id == id_bet_result_confirm:
        game.bet_result = play_input
        with open(sync_file_path, 'w') as outfile:
            outfile.write(jsonpickle.encode(game))
        return [False, False, False, True, False, play_input]
    elif call_id == id_bet_win:
        return [True, False, False, False, False, 'win']
    elif call_id == id_bet_draw:
        return [False, True, False, False, False, 'draw']
    elif call_id == id_bet_lose:
        return [False, False, True, False, False, 'lose']
    else:
        return [False, False, False, False, True, None]


@app.callback(
    [Output(id_bet_val, 'children'), Output(id_bet_input, 'data'), Output(id_bet_confirm, 'active')],
    [Input(id_bet_inc, 'n_clicks'), Input(id_bet_dec, 'n_clicks'), Input(id_bet_confirm, 'n_clicks'),
     Input(id_new_game, 'n_clicks')],
    [State(id_bet_val, 'children'), State(id_game_store, 'data')],
    prevent_initial_call=True
)
def place_bet(n1, n2, n3, n4, bet, game):
    game = jsonpickle.decode(game)
    call_id = callback_context.triggered[0]['prop_id'].split('.')[0]
    if call_id in [id_play_confirm, id_new_game]:
        return [0, 0, False]
    else:
        if game.current_round % 2 == 0:
            chips_available = game.p1_chips
        else:
            chips_available = game.p2_chips
        if call_id == id_bet_inc:
            if bet + 1 <= chips_available:
                bet += 1
            return [bet, 0, False]
        elif call_id == id_bet_dec:
            if bet > 0:
                bet -= 1
            return [bet, 0, False]
        elif call_id == id_bet_confirm:
            game.bet_chips = bet
            with open(sync_file_path, 'w') as outfile:
                outfile.write(jsonpickle.encode(game))
            return [0, bet, True]
        else:
            return [0, 0, False]


# Server
if __name__ == '__main__':
    app.layout = layout
    app.run_server(debug=True)
