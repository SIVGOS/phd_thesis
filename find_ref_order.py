with open('thesis.bbl') as fin:
    lines = fin.read().split('\n')
bib_lines = [l.split('{')[1].strip('{}, ') for l in lines if l.startswith('\\bibitem')]
with open('references.bib') as fin:
    ref_lines = fin.read().split('\n')
for i, bl in enumerate(bib_lines):
    for k, rl in enumerate(ref_lines):
        if f'{{{bl},' in rl:
            while not ref_lines[k].strip().startswith('year'):
                k+=1
            year = ref_lines[k].split('{')[1].strip('{}, ')
    print(i+1, f'\\cite{{{bl}}}', year)

