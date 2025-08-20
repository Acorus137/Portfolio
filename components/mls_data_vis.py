#Imports
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
from utils.data_loader import load_mls_data
import plotly.express as px
import plotly.graph_objects as go

mls_standings = load_mls_data()

#Data Vis
visJumbotron = html.Div(
    dbc.Container(
    [
        dbc.Row(
                [
                html.H1('MLS Standings and Statistics Data Visualization'),
                html.P("Now that we've gathered our data, let's visualize MLS Statistics!")
                ]
                ),
#Row of Cards presenting Statistics for all MLS
            dbc.Row(
                [
                    html.H1('MLS Year over Year Statistics'),
                    dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H5("Avg GF", className="card-title"),
                                html.P(f"{mls_standings['GF'].mean():.1f}", style={"fontSize": "36px", "textAlign": "center"})
                            ]))),
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5('Avg Points', className='card-title'),
                                    html.P(f'{mls_standings['Points'].mean():.1f}', style={"fontSize": "36px", "textAlign": "center"})
                                ]
                                )
                        )
                    ),
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5('Avg PPG', className='card-title'),
                                    html.P(f'{mls_standings['PPG'].mean():.1f}', style={"fontSize": "36px", "textAlign": "center"})
                                ]
                                )
                        )
                    ),
                    dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H5("Max Wins", className="card-title"),
                                html.P(f"{mls_standings['Won'].max():.0f}", style={"fontSize": "36px", "textAlign": "center"})
                            ]))),
                    dbc.Col(
                        dbc.Card(
                        dbc.CardBody(
                            [
                                html.H5("Max Losses", className="card-title"),
                                html.P(f"{mls_standings['Lost'].max():.0f}", style={"fontSize": "36px", "textAlign": "center"})
                            ]))),
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5('Max Ties', className='card-title'),
                                    html.P(f'{mls_standings['Tie'].max():.0f}', style={"fontSize": "36px", "textAlign": "center"})
                                ]
                                )
                        )
                    ),
                ]
            ),
        html.Br(),
        dbc.Row(
            [
                dcc.Graph(figure={},
                          id='mlsFig'),
            html.Br()
            ]
        ),
        dbc.Row(
            [
            html.Hr(),
            html.P(
                "The chart shows a link between Goal Differential and Points but ignores differences in games played. "
                "Most MLS seasons have 30–34 matches, but in 2020 some teams played only 18."
            ),
            html.P(
                "To adjust for this, we use Win Percentage:"
            ),
            html.H5("Win Percentage = (Wins + (Ties × 0.5)) ÷ Games Played"),
            html.P(
                "In MLS, wins give 3 points, ties 1 point, and losses 0. Ties count as half a win in this formula."
            ),
            ], style={'padding': "0.5rem"}),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(figure={},
                            id='mlsFig2')
                       )
            ], style={'padding': "0.5rem"}
            ),
        dbc.Row(
            [
                html.P('From the graph above, we can see Win Percentages graphed against Goal Differential. Additonally, the chart is colored according to points earned.'),
                html.P('This highlights difference between goal differential and points earned. In 2024 Miami had a Goal Differential of 30, yet managed to earn 74 points.'),
                html.P('In 2019 LAFC had an impressive Goal Differential of 48, yet only earned 72 points. While having a high Goal Differential increases the likelihood of success, it does not dictate the number of matches won nor points earned.'),
            ], style={'padding': "0.5rem"}
            ),
        dbc.Row(
            [
                dcc.Graph(figure={},
                        id='mlsFig3')
            ], style={'padding': "0.5rem"}
            ), 
#Creating a section of the MLS Data Vis portion of the portfolio that allows viewers to choose their favorite MLS club and see their yearly statistics.
        dbc.Row(
            [
            html.Hr(),
            html.H2("Choose You're Favorite Club!"),
            html.P('Visualizing Yearly Statistics for your favorite MLS Club! My favorite club is Cincinnati, please select your own below!'),
            html.Hr(),
            ]
        ),
        dbc.Row(
            [
#Dropdown to choose an MLS Club.
            dbc.Col([
                dcc.Dropdown(mls_standings['Club'].unique(),
                            value='Cincinnati',
                            id='mlsDropdown',
                            style={'color': 'black'}
                            )
                        ], width=3
                        ),
                html.Br(),
            ]
        ),
        dbc.Row(
                [
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5("Avg GF", className="card-title"),
                                    html.P(id="clubGfAvg", style={"fontSize": "36px", "textAlign": "center"})
                                ]))),                    
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5("Avg Points", className="card-title"),
                                    html.P(id="clubPpgAvg", style={"fontSize": "36px", "textAlign": "center"})
                                ]))),
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5("Avg PPG", className="card-title"),
                                    html.P(id="clubPointsAvg", style={"fontSize": "36px", "textAlign": "center"})
                                ]))),
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5('Max Wins', className='card-title'),
                                    html.P(id="clubWonMax", style={"fontSize": "36px", "textAlign": "center"})
                                ]))),
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5('Max Losses', className='card-title'),
                                    html.P(id="clubLostMax", style={"fontSize": "36px", "textAlign": "center"})
                                ]))),
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5('Max Ties', className='card-title'),
                                    html.P(id="clubTieMax", style={"fontSize": "36px", "textAlign": "center"})
                                ]))),
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5('Avg Rank', className='card-title'),
                                    html.P(id="clubRankAvg", style={"fontSize": "36px", "textAlign": "center"})
                                ]))),
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5('Win%', className='card-title'),
                                    html.P(id="clubWinPercentage", style={"fontSize": "36px", "textAlign": "center"})
                                ]))),                                                                 
                ]
                ),
        
        html.Br(),
        dbc.Row(
            [
            dbc.Col(
                [
                    dcc.Graph(figure={},
                            id='mlsgraph1')
                ]
            ),
            dbc.Col(
                [
                    dcc.Graph(figure={},
                            id='mlsgraph2')
                ]
            ),
            ], style={'padding': "0.5rem"}
            ),
            ]))
