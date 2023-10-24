### Fun Plot

Today we're gonna be working on a tool to plot python functions on a graph.
Functions like:
```python
def curve(x):
  return 0.05*x*x + - x * 2.5
```
To do this we'll need 3 functions:

### make_graph(x, y)

This function is used to create a 2-dimensional (2D) list containing a string containing one space.
```python
graph = make_graph(2,3)
print(graph)
# result: [[' ', ' '], [' ', ' '], [' ', ' ']]
```

### def print_graph(graph)

This function will output the graph to the users, with positions for values being graph[y][x].

### plot_graph(graph, function, symbol)

This function will place a symbol on each y value for x, where y = function(x).