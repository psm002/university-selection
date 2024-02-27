import altair as alt
import pandas as pd
from vega_datasets import data

def plot_df(df):
    
    states = alt.topo_feature(data.us_10m.url, feature='states')

    df = pd.DataFrame(df)
    #data = df[(df['University Size'] == 'Large') & (df['Admission Rate'] < 0.5) & (df['Out-of-state Tuition'] < 40000)]

    # US states background
    background = alt.Chart(states).mark_geoshape(
        fill='lightgrey',
        stroke='white'
    ).properties(
        width=600,
        height=500
    ).project('albersUsa')

    # airport positions on background
    points = alt.Chart(df).mark_circle(
        size=30,
        color='steelblue'
        ).encode(
        longitude='Longitude:Q',
        latitude='Latitude:Q',
        color=alt.Color('Median Pay:Q', title = 'Median Pay ($)', scale=alt.Scale(scheme='darkred')),
        tooltip=[
            alt.Tooltip('University Name:N', title='University Name'),
            alt.Tooltip('rank_dis:N', title='US News Rank'),
            alt.Tooltip('In-state Tuition:Q', title='In-state Tuition ($)', format = ','),
            alt.Tooltip('Out-of-state Tuition:Q', title='Out-of-state Tuition ($)', format = ','),
            alt.Tooltip('Average GPA:Q', title='Average GPA', format = ',.1f'),
            alt.Tooltip('Average SAT:N', title='Average SAT'),
            alt.Tooltip('Median Pay:Q', title='Median Pay ($)', format = ',')
        ]
    ).properties(
        title=''
    )

    return background + points

