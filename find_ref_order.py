with open('thesis.bbl') as fin:
    lines = fin.read().split('\n')
bib_lines = [l.split('{')[1].strip('{}, ') for l in lines if l.startswith('\\bibitem')]
with open('references.bib') as fin:
    ref_lines = fin.read().split('\n')
ref_text = []
for i, bl in enumerate(bib_lines):
    for k, rl in enumerate(ref_lines):
        if f'{{{bl},' in rl:
            while not ref_lines[k].strip().startswith('year'):
                k+=1
            year = ref_lines[k].split('{')[1].strip('{}, ')
            cite = f'\\cite{{{bl}}}'
            ref_text.append((year, cite))


##
text = '''85:Formulation of equivalent circuit model from cavity model.
86:Equivalent circuit model of EBG metamaterial structure.
87:Modeling broad band printed antenna as cascaded filter stages.
88:Bode-Fano integral is used for estimating the bandwidth of an antenna.
89:Equivalent circuit model of a UWB antenna as a cascade structure of RLC bandpass filters.
90:A mathematical formulation for calculating the lumped elements of equivalent circuit model.
91:Analytical equivalent circuit model of a wide-band filter with notch frequency.
92:A method for enhancing the accuracy of equivalent circuit model.
93:Computer aided formulation of the equivalent circuit model of a metamaterial based antenna.
94:A hybrid between analytical and filter-based equivalent circuit model.
95:Hybrid equivalent circuit model of a complex antenna structure involving several rings and vias.
96:Vector fitting technique is used for rational function approximation of the equivalent circuit modeling of a broad-band antenna.
97:A combination of an analytical narrow band model and a rational functions based macromodel.
98:A computer aided formulation of the cavity model of a substrate integrated waveguide (SIW) antenna.
99:Transmission line model (TLM) of a super wide band (SWB) monopole antenna with three notch bands.'''
cite_lines = text.split('\n')
for i, cl in enumerate(cite_lines):
    ref_num, desc = cl.split(':')
    ref_num = int(ref_num)-1
    print(f'{i+1} & {desc} & {ref_text[ref_num][1]} & {ref_text[ref_num][0]} \\\\ \hline')

