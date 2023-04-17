import numpy as np

from dash import dcc
import plotly.graph_objs as go


def get_data(raw_data: list) -> dict:
    hba_values = [int(d["molecule_properties"]["hba"]) for d in raw_data if d["molecule_properties"]["hba"]]
    return dict(component="Number of H-bond donors",
                data=hba_values,
                mean=np.mean(hba_values),
                std=np.std(hba_values),
                max_value=np.max(hba_values),
                min_value=np.min(hba_values)
                )


    
def draw_component(data_array: list) -> dcc.Graph:
    """[OPTIONAL]
       Method drawing a histogram for number of H-bond acceptors.
       You can use plotly tutorial: https://plotly.com/python/histograms/#histograms-with-gohistogram 
       to style the histogram as you like it or to replace it by other object, e.g. Bars or PieChart.
       To style graph layout, use reference manual: https://plotly.com/python/reference/index/
    Args:
        data_array (list): list of ints

    Returns:
        dcc.Graph: dash graph object that will be shown on the dashboard
    """
    plot = [go.Histogram(x=data_array,
                         marker={"color": "#00b0f0",
                                 "line": {"width": 3,
                                          "color": "#028DBF"}},
                         xbins=dict(start=min(data_array)-1,
                                    end=max(data_array)+1,
                                    size=1),
                         ),
            ]
    layout = go.Layout(xaxis={"title": "H-bond acceptors",
                              "dtick": 1},
                       yaxis={"title": "Frequency"},
                       margin={"t": 5})
    fig = go.Figure(data=plot,
                    layout=layout)
    
    return dcc.Graph(figure=fig)
    