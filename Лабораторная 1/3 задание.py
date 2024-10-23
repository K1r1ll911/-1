# TODO Найдите количество книг, которое можно разместить на дискете
obiem=1.44*1024*1024
str=100
stroki=50
simvolov=25
simvol=4
kniga = 4 * 25 * 50 * 100
kol = obiem // kniga

print("Количество книг, помещающихся на дискету:", int(kol))