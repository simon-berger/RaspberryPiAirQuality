import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import datetime

def get_line_plot(df, x, y, color=None):
    """
    Creates a line plot from the given data.

    Args:
        df:
            Data handle of the read csv
        x:
            Column name of the x-axis
        y:
            Column name of the y-axis
        color: (optional)
            Column name of the color separator
    
    Returns:
        Figure containing the line plot
    """
    if color == None:
        return px.line(df, x=x, y=y)
    else:
        return px.line(df, x=x, y=y, color=color)

def load_csv(path):
    """
    Loads the csv file from the given path.

    Args:
        path:
            File path of the csv file to load
    
    Returns:
        Handle for the csv file.
    """
    return pd.read_csv(path, sep=";")

def serve_layout():
    """
    Creates the app layout.

    Returns:
        Layout of the application.
    """
    # Read the dataset
    df = load_csv("/home/pi/RaspberryPiAirQuality/data/measurements.csv")
    x = "datetime"

    return html.Div(
        children=[
            html.H1(children="Indoor Air Quality Measurement"),
            html.Div(children="Developed by Simon Berger"),
            html.Div(children="Last update: " + str(datetime.datetime.now())),

            # IAQ
            html.H2(children="Indoor Air Quality:"),
            html.H3(children="IAQ (0-500):"),
            dcc.Graph(
                id="iaq_graph",
                figure=get_line_plot(df, x, "iaq")
            ),
            html.H3(children="IAQ Accuracy (0-3):"),
            dcc.Graph(
                id="iaq_acc_graph",
                figure=get_line_plot(df, x, "iaq_accuracy")
            ),

            # C02
            html.H2(children="C02:"),
            html.H3(children="CO2 Equivalent in ppm:"),
            dcc.Graph(
                id="co2_graph",
                figure=get_line_plot(df, x, "co2_equivalent")
            ),

            # VOC
            html.H2(children="VOC:"),
            html.H3(children="Breath VOC in ppm:"),
            dcc.Graph(
                id="breath_voc_graph",
                figure=get_line_plot(df, x, "breath_voc_equivalent")
            ),

            # Temperature
            html.H2(children="Temperature:"),
            dcc.Graph(
                id="temp_graph",
                figure=get_line_plot(df, x, "temperature")
            ),

            # Humidity
            html.H2(children="Humidity:"),
            dcc.Graph(
                id="humidity_graph",
                figure=get_line_plot(df, x, "humidity")
            ),
            
            # Comp gas
            html.H2(children="Comp Gas:"),
            html.H3(children="Comp Gas Value:"),
            dcc.Graph(
                id="comp_gas_graph",
                figure=get_line_plot(df, x, "comp_gas_value")
            ),
            
            # Comp gas
            html.H2(children="Gas Percentage:"),
            html.H3(children="Gas Perventage Value:"),
            dcc.Graph(
                id="gas_percentage_graph",
                figure=get_line_plot(df, x, "gas_percentage")
            )
    ])

def main():
    # Create the app
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

    # Define the method which provides the app layout
    app.layout = serve_layout

    # Start the server
    app.run_server(debug=False, port=9090, host="0.0.0.0")

if __name__ == "__main__":
    main()