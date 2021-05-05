graphs = [[None, 12, 5, None], [12, None, 5, 6], [8, 5, None, 4], [None, 6, 4, None]]

for i in range(len(graphs)):
    for j in range(len(graphs)):
        for k in range(len(graphs)):
            if graphs[i][j] is None or graphs[j][k] is None:
                continue
            elif graphs[i][k] is None:
                graphs[i][k] = graphs[i][j] + graphs[j][k]
            elif graphs[i][k] > graphs[i][j] + graphs[j][k]:
                print(graphs[i][k], graphs[i][j], graphs[j][k])
                graphs[i][k] = graphs[i][j] + graphs[j][k]

print(graphs)