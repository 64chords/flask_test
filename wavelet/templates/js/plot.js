// plot funciton
var graphs = {{graphJSON | safe}};
Plotly.newPlot(
  "wavelet",
  graphs.data,
  graphs.layout
)
