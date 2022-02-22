for k in range(1,7):
    print('Chapter {}'.format(k))
    with open('Chapter_{}.tex'.format(k)) as fin:
        lines = [l for l in fin.read().split('\n') if l.startswith('\\section')]
    for l in lines:
        print(l)
