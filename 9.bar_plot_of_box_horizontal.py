import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

x0 = np.random.randn(50)
x1 = np.random.randn(50) + 2

trace0 = go.Box(x=x0)
trace1 = go.Box(x=x1)
data = [trace0, trace1]
py.iplot(data)
