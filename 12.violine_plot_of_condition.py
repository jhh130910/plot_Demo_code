import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/violin_data.csv")

fig = {
    "data": [
        {
            "type": 'violin',
            "x": df['day'] [ df['sex'] == 'Male' ],
            "y": df['total_bill'] [ df['sex'] == 'Male' ],
            "legendgroup": 'M',
            "scalegroup": 'M',
            "name": 'M',
            "box": {
                "visible": True
            },
            "meanline": {
                "visible": True
            },
            "line": {
                "color": 'blue'
            }
        },
        {
            "type": 'violin',
            "x": df['day'] [ df['sex'] == 'Female' ],
            "y": df['total_bill'] [ df['sex'] == 'Female' ],
            "legendgroup": 'F',
            "scalegroup": 'F',
            "name": 'F',
            "box": {
                "visible": True
            },
            "meanline": {
                "visible": True
            },
            "line": {
                "color": 'pink'
            }
        }
    ],
    "layout" : {
        "yaxis": {
            "zeroline": False,
        },
        "violinmode": "group"
    }
}


py.iplot(fig, filename = 'violin/grouped', validate = False)
