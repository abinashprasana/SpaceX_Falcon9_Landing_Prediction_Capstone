import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Replace with your processed CSV path
DATA_PATH = 'data/spacex_launches.csv'

df = pd.read_csv(DATA_PATH)

app = Dash(__name__)

app.layout = html.Div([
    html.H2('SpaceX Launch Explorer'),
    html.Div([
        html.Label('Launch Site'),
        dcc.Dropdown(
            options=[{'label': s, 'value': s} for s in sorted(df['Launch Site'].unique())] + [{'label': 'All Sites', 'value': 'ALL'}],
            value='ALL',
            id='site-dd'
        ),
    ], style={'width': '300px'}),
    dcc.Graph(id='success-pie'),
    html.Hr(),
    html.Div([
        html.Label('Payload mass range (kg)'),
        dcc.RangeSlider(
            min=df['Payload Mass (kg)'].min(),
            max=df['Payload Mass (kg)'].max(),
            step=100,
            value=[df['Payload Mass (kg)'].min(), df['Payload Mass (kg)'].max()],
            id='payload-slider'
        )
    ]),
    dcc.Graph(id='scatter-out')
])

@app.callback(
    Output('success-pie', 'figure'),
    Input('site-dd', 'value'))
def update_pie(site):
    if site == 'ALL':
        fig = px.pie(df, names='Launch Site', values='class', title='Success count by Launch Site')
    else:
        dff = df[df['Launch Site'] == site]
        fig = px.pie(dff, names='class', title=f'Success vs Failure at {site}')
    return fig

@app.callback(
    Output('scatter-out','figure'),
    [Input('site-dd','value'),
     Input('payload-slider','value')])
def update_scatter(site, payload_range):
    low, high = payload_range
    dff = df[(df['Payload Mass (kg)'] >= low) & (df['Payload Mass (kg)'] <= high)]
    if site != 'ALL':
        dff = dff[dff['Launch Site'] == site]
    fig = px.scatter(dff, x='Payload Mass (kg)', y='class', color='Booster Version Category',
                     title='Payload vs Outcome by Booster Category', hover_data=['Flight Number', 'Launch Site'])
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
