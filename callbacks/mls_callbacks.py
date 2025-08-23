#Imports
from dash import Input, Output, State, callback
import plotly.express as px
from dash.exceptions import PreventUpdate
from utils.data_loader import load_mls_data
import plotly.graph_objects as go

#mls_callbacks

mls_standings = load_mls_data()
mls_standings['WinPercentage'] = (mls_standings['Won']+(mls_standings['Tie']*0.5))/mls_standings['GP']
mls_standings['sRank'] = mls_standings['Rank'].astype(str)


def register_mls_callbacks(mls_data_vis):
    @callback(
        Output('mlsFig', 'figure'),
        Output('mlsFig2', 'figure'),
        Output('mlsFig3', 'figure'),
        Output('mlsgraph1', 'figure'),        
        Output('mlsgraph2', 'figure'),
        Output('clubGDAvg', 'children'),
        Output('clubPointsAvg', 'children'),
        Output('clubPpgAvg', 'children'),
        Output('clubWonMax','children'),
        Output('clubLostMax', 'children'),
        Output('clubTieMax', 'children'),
        Output('clubRankAvg', 'children'),
        Output('clubWinPercentage', 'children'),
        Input('mlsDropdown', 'value')
    )
    def update_mls_graphs(value):
        if not value:
            raise PreventUpdate
        
        rank_colors = {
            "1": "Blue",
            "2": "Yellow",
            "3": "Purple",
            "4": "darkgray",
            "5": "darkgray",
            "6": "darkgray",
            "7": "darkgray",
            "8": "darkgray",
            "9": "darkgray",
            "10": "darkgray",
            "11": "darkgray",
            "12": "darkgray",
            "13": "darkgray",
            "14": "darkgray",
            "15": "darkgray",
        }
        #Coping database within the function, and performing adjustments/calculations.
        mls_standings_club = mls_standings[mls_standings['Club'] == value].copy()
        mls_standings_club.dropna(inplace=True)
        mls_standings['WinPercentage'] = (mls_standings['Won']+(mls_standings['Tie']*0.5))/mls_standings['GP']
        mls_standings_club= mls_standings_club[['Year', 'GP', 'Rank', 'GF', 'GA', 'GD', 'Points','PPG', 'Won', 'Lost', 'Tie', 'WinPercentage']]
        clubGDAvg = mls_standings_club['GD'].mean()
        clubPpgAvg = mls_standings_club['PPG'].mean()
        clubWonMax = mls_standings_club['Won'].max()
        clubLostMax = mls_standings_club['Lost'].max()
        clubTieMax = mls_standings_club['Tie'].max()
        clubPointsAvg = mls_standings_club['Points'].mean()
        clubWinPercentage = mls_standings_club['WinPercentage'].mean()*100
       
       #Creation and caluculation of variables for Radar Chart
        won = mls_standings_club['Won'].sum()
        lost = mls_standings_club['Lost'].sum()
        tie = mls_standings_club['Tie'].sum()
        gd = mls_standings_club['GD'].sum()
        clubRankAvg = mls_standings_club['Rank'].mean()

        mlsFig = px.scatter(mls_standings,
            x="GD",
            y="PPG",
            title="Points Per Game vs Goal Differential",
            hover_data=["Year", 'Club', 'Rank'],
            template="plotly_dark",
            color="sRank",
            color_discrete_map=rank_colors,
            labels={'sRank': 'Rank'}
            )

        mlsFig2 = px.scatter(mls_standings,
                            x="PPG",
                            y="WinPercentage",
                            title="WinPercentage vs. Points Per Game",
                            hover_data=["Year", 'Club', 'Rank'],
                            template="plotly_dark",
                            color='sRank',
                            color_discrete_map=rank_colors,
                            labels={'sRank': 'Rank'}
            )
        
        mlsFig3 = px.violin(mls_standings,
                            y = 'WinPercentage',
                            x = 'Rank',
                            hover_data=['Club', 'Rank' ,'GD', 'GF', 'GA', 'Won', 'Lost'],
                            labels={'GD': 'Goal Differential', 'GF': 'Goals For', 'GA': 'Goals Against', 'Won': 'Matches Won', 'Lost': 'Matches Lost'},
                            title='Win Percentage by Rank',
                            template='plotly_dark',
                            points='all',
                            color='Rank'
            )
                             
        
        #Radar Chart
        fig1 = go.Figure(data=go.Scatterpolar(
             r=[won,lost,tie,gd],
             theta=['Won', 'Lost', 'Tie', 'GD'],
             fill='toself'
             )
             )
        fig1.update_layout(
         template='plotly_dark',
         title='Club MLS Record Radar Chart',
         polar=dict(
             radialaxis=dict(
             visible=True
             ),
             ),
             showlegend=False
             )

        fig2 = px.line(mls_standings_club, 
                       x='Year', 
                       y='Rank', 
                       title=f"{value}'s Year-over-Year Rankings", 
                       template='plotly_dark',
                       markers=True,
                       hover_data=['WinPercentage', 'GD', 'GF']
                       )
        fig2.update_yaxes(autorange="reversed")
        fig2.update_layout(xaxis=dict(tickmode='linear', dtick=1))

        return (mlsFig, mlsFig2, mlsFig3, fig1, fig2,
            f"{clubGDAvg:.1f}", 
            f"{clubPpgAvg:.1f}",
            f"{clubPointsAvg:.1f}", 
            f"{clubWonMax:.0f}", 
            f"{clubLostMax:.0f}", 
            f"{clubTieMax:.0f}",
            f"{clubRankAvg:.1f}",
            f"{clubWinPercentage:.1f}%"
        )
