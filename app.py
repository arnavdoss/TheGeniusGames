# -*- coding: utf-8 -*-

import dash
import os
import dash_bootstrap_components as dbc

# Initialize dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY], title='MATool', update_title=None,
                suppress_callback_exceptions=True,
                meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}])
# LUMEN, SANDSTONE, YETI, CERULEAN, MATERIA,

server = app.server
server.secret_key = os.environ.get('secret_key', 'secret')



