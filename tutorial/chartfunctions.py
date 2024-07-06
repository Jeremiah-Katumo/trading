

# Will add a marker to the chart. Adds a marker to the indicators plot that loads 
# after a backtest. This can be used to mark important events on the graph, such 
# as price crossing a certain value, marking a support level, marking a resistance level, etc
self.add_chart_marker("Overbought", symbol="circle", color="red", size=10)

# Will add a line to the chart. Adds a line data point to the indicator chart. This 
# can be used to add lines such as bollinger bands, prices for specific assets, or 
# any other line you want to add to the chart.
self.add_chart_line("Overbought", value=80, color="red", style="dotted", width=2)

# Return the markers on the indicator as a pandas DataFrame
self.get_markers_df(self)

# Returns a dataframe of the lines on the indicator chart.
self.get_lines_df(self)
