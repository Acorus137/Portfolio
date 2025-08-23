#Imports
from dash import html, Input, Output
from utils.data_loader import load_mls_data
import dash_bootstrap_components as dbc

mls_standings = load_mls_data()

#Webscraping Section
scrapingJumbotron = html.Div([
    dbc.Container([
        html.H1('Web Scraping & Data Cleaning'),
        html.P('Web Scraping using Selenium and Python', className='lead'),
        html.Hr(),
        html.P("This project was started as I share an interest in web scraping, data analysis and the MLS. My favorite club is FC Cincinnati, and I wanted to visualize the club's year of year performance. I could not find the data I needed. So, using Selenium and Python, I scraped the data from the MLS website itself. Before doing so, I verified the MLS website did not have verbiage preventing webscraping or bots."),
        html.P("I’ve written the script in a Jupyter Notebook. In the short clip, you’ll see a Firefox browser window launch and be driven automatically by the script. The script handles an initial cookie or security pop-up, then cycles through all available years of data (2025–1996), scraping the table data from each page. Once collected, the data is loaded into a Pandas DataFrame, and appropriate data types are applied. Some of the team names included prefixes related to yearly achievements (like champions, qualifiers, etc.), which I decided to remove for consistency."),
        html.P(
            html.Div([
                dbc.Nav(
                    [
                    dbc.NavItem(dbc.NavLink("Jupyter Notebook", active=True, href='https://github.com/Acorus137/MLS-Scraper/blob/main/MLS_Standings_WebScraper.ipynb', target='_blank')),
                    dbc.NavItem(dbc.NavLink("MLS Standings URL", href='https://www.mlssoccer.com/standings/#season=MLS-SEA-0001K9&live=true', target='_blank')),
                    ], 
                    pills=True),
    ])
        ),
        dbc.Row([
                dbc.Button(
                    "Show/Hide Video",
                    id="collapse-button",
                    className="mb-3",
                    color="danger",
                    n_clicks=0,
                    style={'size': 12, 'order': 1}
                ),
                dbc.Collapse(
                    dbc.Card(
                        dbc.CardBody(
                            html.Div(
                                html.Iframe(
                                    src="https://www.youtube.com/embed/RKubWYXLv6s",
                                    style={'border': '0'},
                                ),
                                className='ratio ratio-16x9'
                            )
                        )                    ),
                    id="collapse",
                    is_open=True
                )
        ]),

        dbc.Row([
            html.H2('Resulting Data'),
            html.Hr(),
            html.P("To clean the data as much as possible, several columns have been dropped and the appropriate data formats have been applied. Additionally, data from 2025 has been removed as this data is incomplete as of today (5/5/2025). This data will be used later to visualize MLS Statistics."),
            html.P('Data Features descriptions are available below!'),
        ]),

#Accordion that will provide a data dictionary for the features scraped from the MLS Standings Website. The accordion is split, to reduce scrolling.
        dbc.Row([
            dbc.Col(
            dbc.Accordion(
                    [
                        dbc.AccordionItem(
                            "An MLS Soccer Team. Data Type: String", title="Club"
                        ),
                        dbc.AccordionItem(
                            "Rank is a numerical standing within a given conference. The MLS currently has two conferences, East and West. Data Type: Integer", title="Rank"
                        ),
                        dbc.AccordionItem(
                            "The year of competetion the data was recorded. Data Type: Integer", title="Year"
                        ),
                        dbc.AccordionItem(
                            "Quantity of points earned through competition during an MLS Year. Point distribution is as follows: Win = 3, Tie=1, Loss = 0.  Data Type: Integer", title="Points"
                        ),
                        dbc.AccordionItem(
                            "The average points earned per-game in a given year. Data Type: Float", title="PPG"
                        ),
                        dbc.AccordionItem(
                            "Wins earned in a given year. Data Type: Integer", title="Won"
                        ),
                        ],
                        flush=True, start_collapsed=True,
                        ),
                    ),
            dbc.Col(
            dbc.Accordion([
                        dbc.AccordionItem(
                            "Ties earned in a given year. Data Type: Integer", title="Tie"
                        ),
                        dbc.AccordionItem(
                            "Losses gained in a given year. Data Type: Integer", title="Lost"
                        ),
                        dbc.AccordionItem(
                            "Goals Scored For a team during a given year. Data Type: Integer", title="GF"
                        ),
                        dbc.AccordionItem(
                            "Goals Scored Against a team during a given year. Data Type: Integer", title="GA"
                        ),
                        dbc.AccordionItem(
                            "Goal Differential per match (Goals For per match minus Goals Against per match). Data Type: Integer", title="GD"
                        ),
                        dbc.AccordionItem(
                            "Games Played during a given year. Data Type: Integer", title="GP"
                        ),
                    ],
                    flush=True, start_collapsed=True,
                            ),
                    )
        ]
        ),

#This table is used to display the scraped, clean data.
        dbc.Row([
            html.Hr(),
            dbc.Table.from_dataframe(
                mls_standings,
                striped=True,
                bordered=True,
                hover=True,
                color='dark',
                size='md'
            )
        ])
    ])
])