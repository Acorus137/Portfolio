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
                                html.H5("GF Avg", className="card-title"),
                                html.P(f"{mls_standings['GF'].mean():.1f}", style={"fontSize": "36px", "textAlign": "center"})
                            ]))),
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5('Points Avg', className='card-title'),
                                    html.P(f'{mls_standings['Points'].mean():.1f}', style={"fontSize": "36px", "textAlign": "center"})
                                ]
                                )
                        )
                    ),
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5('PPG Avg', className='card-title'),
                                    html.P(f'{mls_standings['PPG'].mean():.1f}', style={"fontSize": "36px", "textAlign": "center"})
                                ]
                                )
                        )
                    ),
                    dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H5("Wins Max", className="card-title"),
                                html.P(f"{mls_standings['Won'].max():.0f}", style={"fontSize": "36px", "textAlign": "center"})
                            ]))),
                    dbc.Col(
                        dbc.Card(
                        dbc.CardBody(
                            [
                                html.H5("Loss Max", className="card-title"),
                                html.P(f"{mls_standings['Lost'].max():.0f}", style={"fontSize": "36px", "textAlign": "center"})
                            ]))),
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5('Tie Max', className='card-title'),
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
                html.Br(),
                html.Br(),
                html.P("Here we can analyze the correlation between Goal Differential and Points Per game."),
                html.P("Clubs ranking less than three have been grayed-out to help identify outliers."),
                html.P("In 2024 Miami had a Goal Differential of 30, yet managed a PPG of 2.18."),
                html.P('In 2019 LAFC had an impressive Goal Differential of 48, but only earned a PPG of 2.12. While having a high Goal Differential increases the likelihood success, it can not account for multi-goal wins or losses.'),
                html.P('From this scatter plot, we can see that clubs in the top three of their respective divisions have a Goal Differential of zero or more. This indicates that once a team reaches a positive Goal Differential, its predictive weight on final standings decreases.'),
                html.Br(),
                html.Br(),
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
                            html.Br(),
                            html.Br(),
                            html.P("As we have found Goal Differential diminishes in value as it increases. To address this we will engineer a Win Percentage field to increase our predictive capabilities."),
                            html.H4("Win Percentage = (Wins + (Ties × 0.5)) ÷ Games Played"),
                            html.P("In MLS, wins give 3 points, ties 1 point, and losses 0. Ties count as half a win in this formula."),
                            html.H4("Now, lets plot Win Percentage against PPG."),
                            html.P("Here we can see a strong correlation between PPG and a team's Win Percentage. This isn't unexpected, wins and ties will increase PPG, while losses will decrease PPG."),
                            html.P("From this scatter plot we can identify that clubs ranking in the top three of their division should have a Win Percentage of 0.50 or more. Again, clubs ranking less than three have been grayed out for outlier identification."),
                            html.Br(),
                            html.Br(),
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
                            html.Br(),
                            html.P("In the graphs above we are able to determined that Goal Differential and Win Percentage are strongly correlated with a team's ability to earn points."),
                            html.P("In our comparison of Goal Differential and PPG, we can see that a team must have a Goal Differential of 0 or more, to land in the top three of their divison."),
                            html.P("And when reviewing our Win Percentage vs. PPG, we discovered a club should have a Win Percentage of 0.50 or better to rank among the top three of their division."),
                            html.P('In this violin plot, we can confirm our findings above. As we can see, the median Win Percentage for a 3rd Ranked team is 0.544.'),
                            html.P("With these key statistics in mind, let's take a look at your club of choice!"),
                            html.Br(),
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
            html.Br()
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
#Club Selection statistic cards.
        dbc.Row(
                [
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5("GD Avg", className="card-title"),
                                    html.P(id="clubGDAvg", style={"fontSize": "36px", "textAlign": "center"})
                                ]))),                    
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5("Points Avg", className="card-title"),
                                    html.P(id="clubPpgAvg", style={"fontSize": "36px", "textAlign": "center"})
                                ]))),
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5("PPG Avg", className="card-title"),
                                    html.P(id="clubPointsAvg", style={"fontSize": "36px", "textAlign": "center"})
                                ]))),
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5('Wins Max', className='card-title'),
                                    html.P(id="clubWonMax", style={"fontSize": "36px", "textAlign": "center"})
                                ]))),
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5('Loss Max', className='card-title'),
                                    html.P(id="clubLostMax", style={"fontSize": "36px", "textAlign": "center"})
                                ]))),
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5('Tie Max', className='card-title'),
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
    #Graphs plotting the club selections year over year performance.    
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
