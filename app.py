import dash
from dash import dcc, html, dash_table
from dash.dependencies import Output, Input, State
import plotly.express as px
import dash_bootstrap_components as dbc

import pandas as pd
import os

import fsspec
import gcsfs


####### Utility Functions #####################


def data_in():

    # if cloud == False:
    #     data = os.path.join('data/data.csv')

    # else:
    #     project = 'dash-example-265811'
    #     project_name = 'dash-example-265811.appspot.com'
    #     folder_name = 'data'
    #     file_name = 'data.csv'

    #     if local == True:
    #         GCP = GCPDownloaderLocal() # run locally
    #     else:
    #         GCP = GCPDownloaderCloud()  # run on cloud

    #     bytes_file = GCP.getData(project, project_name, folder_name, file_name)
    #     s = str(bytes_file, encoding='utf-8')
    #     data = StringIO(s)

    data_df = pd.read_csv("gs://gcf-sources-134756275535-us-central1/nfl.csv")

    return data_df

# youtube_stats_df = pd.read_csv("development_nb/youtube_stats_clean.csv")
# keyword_options = sorted(youtube_stats_df.Keyword.unique())

def app_layout():
    nfl_df = data_in()

    navbar = dbc.NavbarSimple(
        brand="Recent NFL Comments Sentiment",
        brand_style = {"font-family": "Verdana, sans-serif", "font-size": "2em"},
        brand_href="#",
        color="red",
        dark=True,
        id = "navbar-example-update"
    )

    return html.Div(children=[
        navbar,

        dbc.Container([
        dcc.Markdown(''' 
        These are recent comments scraped from nfl reddit teams along with their sentiment score.
        Model used: https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english
        ''', 
        style={"font-family": "Verdana, sans-serif"}),

        dash_table.DataTable(nfl_df.to_dict('records'), [{"name": i, "id": i} for i in nfl_df.columns], style_cell={'textAlign': 'left'},   style_data={
        'whiteSpace': 'normal',
        'height': 'auto',
    },)

        
        ], style = {"margin-top": "5%", "margin-bottom": "5%"})
    ])



##########################################

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], meta_tags=[{'name': 'viewport','content': 'width=device-width, initial-scale=1.0'}])
app.title = "NFL Reddit Comments"
server = app.server

nfl_df = data_in()


app.layout = app_layout

####### Callbacks #######################


##########################################

if __name__=='__main__':
    # app.run_server(debug=False, port=8005)
    app.run_server(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))