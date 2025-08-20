from dash import html, dcc, Input, Output
from components.sidebar import sidebar
from components.home import homeJumbotron
from components.scraper import scrapingJumbotron
from components.mls_data_vis import visJumbotron

layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    html.Div(id="page-content", style={"margin-left": "18rem", "padding": "2rem 1rem"})
])

def register_page_content_callbacks(app):
    @app.callback(Output("page-content", "children"), Input("url", "pathname"))
    def display_page(pathname):
        if pathname == "/":
            return homeJumbotron
        elif pathname == "/page-1":
            return scrapingJumbotron
        elif pathname == "/page-2":
            return visJumbotron
        return html.Div([
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised...")
        ])