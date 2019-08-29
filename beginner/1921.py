L = int(input())

if(3 <= L <= pow(10,5)):
    complete_graph_wo_neighbors = L*0.5*(L-1) - L
    print("{:.0f}".format(complete_graph_wo_neighbors))