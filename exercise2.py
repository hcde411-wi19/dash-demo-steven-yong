# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np
import pandas as pd

# static data
neighborhood = ['Fremont', 'Queen Anne', 'Belltown', 'South Lake Union', 'Capitol Hill', 'Downtown', 'First Hill', 'Pioneer Square', 'Chinatown', 'SODO']
crime_type = ['Total Crime', 'Robbery', 'Aggravated Assault', 'Burglary', 'Larceny-Theft', 'Motor Vehicle Theft']
# TODO: working on this file to add more codes...

# initialize Dash environment
app = dash.Dash(__name__)

# set up an layout
app.layout = html.Div(children=[
    # H1 title on the page
    html.H1(children='Hello Dash for HCDE 411'),

    # a div to put a short description
    html.Div(children='''
        This is a simple Dash application for HCDE 411
    '''),

    # append the visualization to the page
    dcc.Graph(
        id='example-graph',
        figure={
            # configure the data
            'data': [
                go.Heatmap(z=[[93, 171, 83, 129, 189, 293, 84, 40, 91, 75],
                              [1, 5, 3, 7, 6, 23, 1, 2, 7, 4],
                              [1, 11, 4, 9, 11, 28, 10, 11, 8, 4],
                              [26, 45, 22, 19, 47, 24, 47, 36, 51, 43],
                              [61, 97, 53, 90, 115, 209, 47, 36, 51, 43],
                              [4, 12, 0, 3, 7, 5, 6, 0, 5, 6]],
                           colorscale='Rainbow',
                           x=neighborhood,
                           y=crime_type),
            ],

            # configure the layout of the visualization --
            # set the title to be "Usage of the BGT North of NE 70th per week day"
            'layout': {
                'title': 'Crime in Seattle Neighborhoods'
            }
        }
    )
])

if __name__ == '__main__':
    # start the Dash app
    app.run_server(debug=True)