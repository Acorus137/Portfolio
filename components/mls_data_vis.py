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
                dbc.Col(
                dcc.Graph(figure={},
                          id='mlsFig'),
                ),
                dbc.Col(
                    dbc.CardBody([
                html.P("This scatter plot shows a link between Goal Differential and Points but ignores differences in games played. "
                       "Most MLS seasons have 30–34 matches, but in 2020 some teams played only 18."),
                html.P('From this chart we can see the variation between goal differential and points earned. In 2024 Miami had a Goal Differential of 30, yet managed to earn 74 points.'),
                html.P('In 2019 LAFC had an impressive Goal Differential of 48, but only earned 72 points. While having a high Goal Differential increases the likelihood of success, it does not dictate the number of matches won nor points earned.'),
                ]),
                ),
            html.Br(),
            ], style={'padding': "0.5rem"}
            ),
        dbc.Row(
            [
                dbc.Col(
                     dbc.CardBody(
                        [
                            html.P("To adjust for variance in games played, we will create a Win Percentage field:"),
                            html.H5("Win Percentage = (Wins + (Ties × 0.5)) ÷ Games Played"),
                            html.P("In MLS, wins give 3 points, ties 1 point, and losses 0. Ties count as half a win in this formula."),
                            html.P("From this scatter plot, we can see Win Percentages graphed against Points earned. Here we can see a strong correlation between points earned and a team's Win Percentage."),
                        ])),
                dbc.Col(
                    dcc.Graph(figure={},
                              id='mlsFig2')
                ),
            ], style={'padding': "0.5rem"}
            ),
        dbc.Row(
            [
                dbc.Col(
                dcc.Graph(figure={},
                        id='mlsFig3')
                ),
                dbc.Col([
                    dbc.CardBody(
                        [
                            html.P("In the graphs above we are able to determined that Goal Differential and Win Percentage are strongly correlated with a team's ability to earn points, which determines a team's performance."),
                            html.P("In our comparison of Goal Differential and Points earned, we can see that a team must have a Goal Differential of 0 or more, to land in the top three of their divison."),
                            html.P("And when reviewing our Win Percentage vs. Points earned graph, it's easy to see that if a team wishes to be in the top three of their division they should have a Win Percentage of 0.50 or better."),
                            html.P('In this violin plot, we can confirm our findings above. As we can see, the median Win Percentage for a 3rd Ranked team is 0.544.'),
                            html.P("Keep this in mind when reviewing your team's year of year statistics below!")
                        ]
                )
                ])
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
