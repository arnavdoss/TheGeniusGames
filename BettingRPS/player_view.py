from dash import Dash, html, dcc, Input, Output, State, callback_context, ALL, no_update
import dash_bootstrap_components as dbc
from BettingRPS.game_engine import BettingRPS

# Initialize app
app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY], title='BettingRPS', update_title=None,
           meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}])
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

# Functions
game = BettingRPS(11)


def game_hands_display():
    game_hands = game.game_hands
    n_rounds = game.n_rounds
    round_hand_button = []
    width = f'calc(100vw / {n_rounds * 1.5})'
    for idx in range(n_rounds):
        round_hand_button.append(
            dbc.Button([
                dbc.Row([game_hands[idx]], justify='center', style={'fontSize': width}), dbc.Row(html.H3(idx + 1))
            ], id={'type': id_game_hands, 'index': idx}, outline=False, color='success', disabled=False,
                style={'width': width, 'height': '25vh'}
            )
        )
    return html.Div([dbc.Row([dbc.ButtonGroup(round_hand_button)], align='center', justify='center')])


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
app.layout = dbc.Container([
    html.Div(game_hands_display(), id=id_game_hands_wrapper),
    dcc.Store(id=id_bet_input, data=0),
    dcc.Store(id=id_play_input, data=None),
    dcc.Store(id=id_bet_result_input, data=None),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    html.Div(dbc.Row([dbc.Col(bet_inputs), dbc.Col(bet_hand_inputs)]), id=id_p1_inputs)
                ], width=8),
                dbc.Col([
                    html.H1(game.p1_chips, id=id_p1_chips, style={'fontSize': '10vh'})
                ], width=4, align='center')
            ])
        ], width=4, style={'border-top': '1px solid grey', 'border-right': '1px solid grey',
                           'border-bottom': '1px solid grey', 'border-top-right-radius': '30px',
                           'border-bottom-right-radius': '30px'}),
        dbc.Col([
            dbc.ButtonGroup([
                dbc.Button('Next Round', id=id_next_round),
                dbc.Button('New Game', id=id_new_game),
                dbc.Button('Show Log', id=id_show_log),
            ]),
            dbc.Modal([
                dbc.ModalBody(game.log, id=id_game_log, style={'white-space': 'pre-wrap'})
            ], id=id_modal_log)
        ], width=4, align='center', style={'height': '100%'}),
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    html.H1(game.p2_chips, id=id_p2_chips, style={'fontSize': '10vh'})
                ], width=4, align='center'),
                dbc.Col([
                    html.Div(play_hand_inputs, id=id_p2_inputs)
                ], width=8)
            ])
        ], width=4, style={'border-top': '1px solid grey', 'border-left': '1px solid grey',
                           'border-bottom': '1px solid grey', 'border-top-left-radius': '30px',
                           'border-bottom-left-radius': '30px'}),
    ], style={'height': '70vh'}, justify='center')
], fluid=True)


# Callbacks
@app.callback(
    [Output(id_game_hands_wrapper, 'children'), Output(id_p1_chips, 'children'), Output(id_p2_chips, 'children')],
    [Input(id_play_confirm, 'active'), Input(id_bet_confirm, 'active'), Input(id_bet_result_confirm, 'active'),
     Input(id_new_game, 'n_clicks')],
    [State(id_play_input, 'data'), State(id_bet_input, 'data'), Input(id_bet_result_input, 'data')],
    prevent_initial_call=True
)
def play_round(play_confirm, bet_confirm, bet_result_confirm, n, play_input, bet_input, bet_result_input):
    call_id = callback_context.triggered[0]['prop_id'].split('.')[0]
    if call_id == id_new_game:
        game.new_game(11)
        return [game_hands_display(), game.p1_chips, game.p2_chips]
    elif game.current_round <= game.n_rounds:
        if play_confirm is True and bet_confirm is True and bet_result_confirm is True:
            game.play_round(play_input, bet_result_input, bet_input)
        return [no_update, game.p1_chips, game.p2_chips]


@app.callback([Output(id_modal_log, 'is_open'), Output(id_game_log, 'children')], Input(id_show_log, 'n_clicks'))
def show_log(n):
    return [True, game.log]


@app.callback(
    Output({'type': id_game_hands, 'index': ALL}, 'active'),
    Input(id_next_round, 'n_clicks'),
    State({'type': id_game_hands, 'index': ALL}, 'active')
)
def which_round_active(n, state):
    state = [False for item in state]
    state[game.current_round - 1] = True
    return state


@app.callback(
    [Output(id_play_rock, 'active'), Output(id_play_paper, 'active'), Output(id_play_scissors, 'active'),
     Output(id_play_confirm, 'active'), Output(id_play_confirm, 'disabled'), Output(id_play_input, 'data')],
    [Input(id_play_rock, 'n_clicks'), Input(id_play_paper, 'n_clicks'), Input(id_play_scissors, 'n_clicks'),
     Input(id_play_confirm, 'n_clicks'), Input(id_next_round, 'n_clicks'), Input(id_new_game, 'n_clicks')],
    State(id_play_input, 'data')
)
def active_play_hand_buttons(n1, n2, n3, n4, n5, n6, play_input):
    call_id = callback_context.triggered[0]['prop_id'].split('.')[0]
    if call_id == id_play_confirm:
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
    State(id_bet_result_input, 'data')
)
def active_play_hand_buttons(n1, n2, n3, n4, n5, n6, play_input):
    call_id = callback_context.triggered[0]['prop_id'].split('.')[0]
    if call_id == id_bet_result_confirm:
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
    State(id_bet_val, 'children')
)
def place_bet(n1, n2, n3, n4, bet):
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
            return [0, bet, True]
        else:
            return [0, 0, False]


@app.callback(
    [Output(id_p1_inputs, 'children'), Output(id_p2_inputs, 'children')],
    [Input(id_next_round, 'n_clicks'), Input(id_new_game, 'n_clicks')]
)
def switch_inputs_per_round(n1, n2):
    call_id = callback_context.triggered[0]['prop_id'].split('.')[0]
    if call_id == id_next_round:
        if game.current_round % 2 == 0:
            return [dbc.Row([dbc.Col(bet_inputs), dbc.Col(bet_hand_inputs)]), play_hand_inputs]
        else:
            return [play_hand_inputs, dbc.Row([dbc.Col(bet_inputs), dbc.Col(bet_hand_inputs)])]
    else:
        return [play_hand_inputs, dbc.Row([dbc.Col(bet_inputs), dbc.Col(bet_hand_inputs)])]


# Server
if __name__ == '__main__':
    app.run_server(debug=True)
