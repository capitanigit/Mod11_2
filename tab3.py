from dash import dcc
from dash import html
import plotly.graph_objects as go

#dodatkowa tabela
def render_tab(df):

    layout = html.Div([html.H1('Kanały Sprzedaży',style={'text-align':'center'}),
                        html.Div([dcc.DatePickerRange(id='stores-range',
                        start_date=df['tran_date'].min(),
                        end_date=df['tran_date'].max(),
                        display_format='YYYY-MM-DD')],style={'width':'100%','text-align':'center'}),
                        html.Div([html.Div([dcc.Graph(id='bar-stores')],style={'width':'50%'}),
                        html.Div([dcc.Graph(id='barh-stores-subcat')],style={'width':'50%'})],style={'display':'flex'})
                        ])

    return layout