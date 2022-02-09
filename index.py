from app import app, server
from BettingRPS.player_view import layout as layout_betting_rps

layout = layout_betting_rps

if __name__ == '__main__':
    app.layout = layout
    app.run_server(debug=False)
