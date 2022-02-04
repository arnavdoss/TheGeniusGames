from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc

# Initialize app
app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY], title='BettingRPS',  update_title=None,
           meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}])
# CYBORG, DARKLY, SLATE, SOLAR, SUPERHERO, VAPOR, QUARTZ,

# IDs
rock = '✊'
paper = '✋'
scissors = '✌'



# Functions

# def hand_card(index):
#
#     item = dbc.Col([
#         dbc.Card([
#             dbc.CardHeader([html.Header(str(index))]),
#             dbc.CardBody([rock])
#         ])
#     ])


# Layout
app.layout = dbc.Container([
    html.H1(f'{rock}, {paper}, {scissors}')
], fluid=True)

# Callbacks


# Server
if __name__ == '__main__':
    app.run_server(debug=True)
