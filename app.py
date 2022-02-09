# -*- coding: utf-8 -*-

import dash
import os
import dash_bootstrap_components as dbc

# Initialize dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

server = app.server
server.secret_key = os.environ.get('secret_key', 'secret')



