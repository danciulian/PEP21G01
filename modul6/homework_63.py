start = int(input('start: '))
end = int(input('end: '))
x = []
for i in range(start, start + end):
    x.append(i)
print(x)

lot_start = start//20
print('lot start:', lot_start)

lot_end = (start + end) //20
print('lot_end', lot_end)

for i in range(lot_start, lot_end):
    print(i)
print(start + end)
lista_start = []
if 20 * lot_start < start:
    for i in range(start, 20 * lot_start + 20):
        lista_start.append(i)
    print(lista_start)
else:
    for i in range(start, 20 * lot_start +20):
        lista_start.append(i)
    print('lista start:', list(lista_start))

lista_mid = []
for i in range(lot_start + 1, lot_end):
    lista_inter = []
    for j in range(0, 20):
        lista_inter.append(20 * i + j)
    lista_mid.append(lista_inter)
print('list_mid:', lista_mid)

lista_mid.insert(0,lista_start)
print('list_mid_1:', lista_mid)

lista_final = []
if 20 * lot_end <= start + end:
    for i in range(20 * lot_end, start + end):
        lista_final.append(i)

print('list_final:', lista_final)

l = len(lista_mid)
lista_mid.insert(l, lista_final)
print('Done:', lista_mid)


