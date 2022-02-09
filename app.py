import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, State, callback_context, ALL
from main_app import app
from BettingRPS.player_view import layout as layout_bettingrps

app.layout = dbc.Container([
    layout_bettingrps
], fluid=True)


if __name__ == '__main__':
    app.run_server(debug=False)
