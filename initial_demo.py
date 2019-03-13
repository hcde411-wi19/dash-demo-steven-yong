# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html


# static data
weekday_in_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
counts_in_order = [160613, 154225, 155175, 150819, 146014, 215725, 203483]

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
                # set x to be weekday, and y to be the counts. We use bars to represent our data.
                {'x': weekday_in_order, 'y': count_in_total, 'type': 'bar', 'name': 'Total'},

            ],
            # configure the layout of the visualization --
            # set the title to be "Usage of the BGT North of NE 70th per week day"
            'layout': {
                'title': 'Usage of the BGT North of NE 70th per week day'
            }
        }
    )
])


if __name__ == '__main__':
    # start the Dash app
    app.run_server(debug=True)


