# -*- coding: utf-8 -*-

import dash
import dash_bootstrap_components as dbc

# Initialize dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY], title='MATool', update_title=None,
                suppress_callback_exceptions=True,
                meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}])

server = app.server


