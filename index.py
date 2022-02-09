from app import app, server
import dash_bootstrap_components as dbc
from BettingRPS.player_view import layout as layout_betting_rps

app.layout = dbc.Container([layout_betting_rps], fluid=True)

if __name__ == '__main__':
    app.run_server(debug=False)
