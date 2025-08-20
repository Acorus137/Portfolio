from dash import html
import dash_bootstrap_components as dbc

sidebar = html.Div([
    html.H2("Navigation", className="text-light"),
    html.Hr(),
    dbc.Nav([
        dbc.NavLink("Home", href="/", active="exact", style={"color": "#fff"}),
        dbc.NavLink("Web Scraping & Cleaning", href="/page-1", active="exact", style={"color": "#fff"}),
        dbc.NavLink("MLS Data Visualization", href="/page-2", active="exact", style={"color": "#fff"})
    ], vertical=True, pills=True)
], style={
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#444"
})