import linecache
filename = 'CMU_Dict_Final.txt'
i = 1

with open(filename, 'w') as f:
    while i <= 134298:
        line = linecache.getline('cmudictC.txt', i)
        line = line.rstrip('\n')
        f.write(line + ',' + '\n')
        i += 1
