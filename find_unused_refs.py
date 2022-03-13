with open('thesis.bbl') as fin:
    lines = fin.read().split('\n')
used_refs = [l.split('{')[1].strip('{}, ') for l in lines if l.startswith('\\bibitem')]
with open('references.bib') as fin:
    lines = fin.read().split('\n')
all_refs = [l.split('{')[1].strip(', ') for l in lines if l.strip().startswith('@')]
unused_refs = [b for b in all_refs if b not in used_refs]
