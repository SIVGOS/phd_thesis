import os
files = [f for f in os.listdir('.') if f.endswith('.tex') or f.endswith('.bib')]
for file in files:
    with open(file) as fin:
        lines = fin.read().split('\n')
        for line in lines:
            try:
                line.encode('ascii')
            except:
                print(file)
                print(line)
                print('--------------------')
