lar = float(input('Largura da parede (m) :'))
h = float(input('Altura da parede (m):'))
area = lar*h
print('Sua parede tem dimensão de {}mx{}m e area de {}m²'.format(lar, h, area))
tinta = area/2
print('Para pintar essa parede, voce precisara de {}L de tinta. '.format(tinta))
