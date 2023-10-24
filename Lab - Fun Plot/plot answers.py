from math import sin

def make_graph(x, y):
  return [[' ' for _ in range(x)] for _ in range(y)]

def print_graph(graph):
  length = len(graph[0])
  for line in graph:
    print("".join(line))
  print("-"*length)

def plot_graph(graph, function,symbol):
  length = len(graph[0])
  height = len(graph)
  for x in range(length):
    result = height - int(function(x))
    if result >= 0 and result < height:
      graph[result][x] = symbol 

  return graph

def test_1():
  graph = make_graph(50,50)

  graph = plot_graph(graph, lambda x: -0.05*x*x + x * 2.5 + 5, "@")
  graph = plot_graph(graph, lambda x: -0.05*x*x + x * 2.5 + 4, "@")
  graph = plot_graph(graph, lambda x: -0.05*x*x + x * 2.5 + 3, "@")

  graph = plot_graph(graph, lambda x: 0.05*x*x + - x * 2.5 + 35 if x > 7 and x < 43 else 100, "F")
  graph = plot_graph(graph, lambda x: 0.05*x*x + - x * 2.5 + 40 if x < 30 and x > 20 else 100, "P")
  graph = plot_graph(graph, lambda x: 20 if x in [18, 19, 32, 31] else 100, "o")
  graph = plot_graph(graph, lambda x: 21 if x in [18, 19, 32, 31] else 100, "o")
  
  print_graph(graph)


def test_2():
  graph = make_graph(50,50)
  sw = lambda x: (abs(sin(x * 4) * 4) + 2)

  graph = plot_graph(graph, lambda x: -0.05*x*x + x * 2.5 + 2 + sin(x * 20) + sw(x) if x > 6 and x < 44 else 100, "@")
  graph = plot_graph(graph, lambda x: -0.05*x*x + x * 2.5 + 1 + sin(x * 20) + sw(x) if x > 6 and x < 44 else 100, "@")
  graph = plot_graph(graph, lambda x: -0.05*x*x + x * 2.5 + sin(x * 20) + sw(x) if x > 6 and x < 44 else 100, "@")

  graph = plot_graph(graph, lambda x: -0.05*x*x + x * 2.5 + 5 if x > 7 and x < 43 else 100, "E")
  graph = plot_graph(graph, lambda x: 0.05*x*x + - x * 2.5 + 35 if x > 7 and x < 43 else 100, "F")
  graph = plot_graph(graph, lambda x: 0.05*x*x + - x * 2.5 + 40 if x < 30 and x > 20 else 100, "P")
  graph = plot_graph(graph, lambda x: 20 if x in [18, 19, 32, 31] else 100, "o")
  graph = plot_graph(graph, lambda x: 21 if x in [18, 19, 32, 31] else 100, "o")
  
  print_graph(graph)

test_1()
test_2()