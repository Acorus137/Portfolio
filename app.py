from dash import Dash
import dash_bootstrap_components as dbc
from index import layout, register_page_content_callbacks
from callbacks.mls_callbacks import register_mls_callbacks
from callbacks.scraper_callbacks import register_scraper_callbacks

app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY], suppress_callback_exceptions=True)
app.title = "MLS Dashboard"
app.layout = layout
server = app.server

# Register all callbacks
register_page_content_callbacks(app)
register_mls_callbacks(app)
register_scraper_callbacks(app)



if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)  # use_reloader=False avoids duplicate load
