"""
Resources: 

1. https://plotly.com/python/static-image-export/

"""


import dash
import inspect
import numpy as np
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html

from base64 import b64encode
from numpy.random import seed, rand
from dash.dependencies import Input, Output
from plotly.missing_ipywidgets import FigureWidget
from Support.SupportProvider import SupportProvider

class WebServedVisual(object):

    _class_name:str = None
    _support:SupportProvider = None

    def __init__(self) -> None:  
        try:

            self._support = SupportProvider()
            self._class_name = __class__.__name__

        except Exception as ex:
            self._support.ExceptMessage(classname = self._class_name,
                                        funcname=inspect.currentframe().f_code.co_name,
                                        exception=ex)

    def BuiltWebApp(self,
                fig:(FigureWidget | any)) ->  any:  
        try:
            
            app = dash.Dash(__name__)

            app.layout = html.Div([
                html.P("Render Option:"),
                dcc.RadioItems(
                    id='render-option',
                    options=[{'value': x, 'label': x} 
                            for x in ['interactive', 'image']],
                    value='image'
                ),
                html.Div(id='output'),
            ])

            return app

        except Exception as ex:
            self._support.ExceptMessage(classname = self._class_name,
                                        funcname=inspect.currentframe().f_code.co_name,
                                        exception=ex)

    def ServeWebApp(self,
                    app:any,
                    fig:(FigureWidget | any),
                    debug:bool = True) ->  None:  
        try:

            @app.callback(
                Output("output", "children"), 
                [Input('render-option', 'value')])
            def display_graph(render_option):
                if render_option == 'image':
                    img_bytes = fig.to_image(format="png")
                    encoding = b64encode(img_bytes).decode()
                    img_b64 = "data:image/png;base64," + encoding
                    return html.Img(src=img_b64, style={'width': '100%'})
                else:
                    return dcc.Graph(figure=fig)

            app.run_server(debug=debug)
        except Exception as ex:
            self._support.ExceptMessage(classname = self._class_name,
                                        funcname=inspect.currentframe().f_code.co_name,
                                        exception=ex)

if __name__ == "__main__":
    WebServedVisual()