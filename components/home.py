from dash import html
import dash_bootstrap_components as dbc

homeJumbotron = html.Div(
    dbc.Container(
        [
        html.H1('Kevin Crowe', className='display-1'),
        html.P(
            'Data Science & Visualization Portfolio', 
            className='lead'
        ),
        dbc.Row([
        html.Hr(),
#Star statement
        dbc.Col([
        html.P("With over 14 years of experience in service, production and quality management, I am a data-driven leader who specializes in using analytics and automation to drive operational efficiency and performance improvement. I hold a Bachelor of Science in Data Analytics from Southern New Hampshire University and bring a well-rounded toolkit that includes Python, R, VBA, SQL, Power BI, and advanced statistical analysis."),
        html.P("In my most recent role, I led initiatives including GAP and competitive analysis, process automation, and the development and tracking of key performance indicators (KPIs). I also designed and implemented interactive Power BI dashboards to support data-driven decision-making and utilized predictive analytics with Python and R to model historical consumption trends and forecast future consumption."),
        html.P("I’m passionate about turning data into actionable insights, and I thrive in projects focused on predictive modeling, process improvement, and operational analytics. Whether you're looking to optimize workflows, uncover growth opportunities, or build custom dashboards and forecasts, I’m ready to help bring your data to life."),
#Contact Details
        html.Hr(),
        html.P('Contact me', className='lead'),        
        dbc.Nav(
            [
        dbc.NavItem(dbc.NavLink("Linkedin", href='https://www.linkedin.com/in/kevin-crowe-8b9b1382/', target='_blank')),
        dbc.NavItem(dbc.NavLink("Email", active=True, href='mailto:kevincrowe137@gmail.com', target='_blank')),
        dbc.NavItem(dbc.NavLink("Upwork", href='https://www.upwork.com/freelancers/~01cec87490ca847f2e', target='_blank')),
        ], pills=True
        ),
        ]),
#Photo of my Family & a short description
        dbc.Col([
        dbc.CardImg(src="/assets/PXL_20241109_194035961.jpg", top=True),
        dbc.CardBody(
            [
                html.H4("My Family", className="card-title"),
                html.P(
                    "This photo is of my family and I at an FC Cincinnati pre-game event in the West End of Cincinnati.",
                    className="card-text",
                ),
            ]
        ),
    ],
    style={"width": "18rem"},
)
    ],
    )
], fluid=True,
className="p-3 bg-body-primary"
)
)