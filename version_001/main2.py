from model import Unit, Storage, Shop, Loader, Actor, Truck

kg:Unit = Unit("kg","kilogram")

storage_1 = Storage("Avaron st., 12", 900, 893, kg)
storage_2 = Storage("SaintOcean st, 2/23", 1200, 1200, kg)
storage_3 = Storage("SaintOcean sdfas faefasdf st, 2/23", 2000, 0, kg)

shop_1 = Shop("WildTree st., 65", 300, 300, kg)
shop_2 = Shop("GreenLief st., 1/a", 250, 300, kg)

print(storage_1, '\n' ,storage_2)
print(shop_1, '\n' ,shop_2)

ld: Loader = Loader(2, 0, kg)

actors: list[Actor] = list()
for i in range(0,6):
    actors.append(Truck(10,0,kg))

for i in range(0,6):
    actors.append(Loader(2,0,kg))

hasToDo = True
i = 0
while (hasToDo):
    hasToDo = False
    for a in actors:
        hasToDo = hasToDo or a.tick()
    i += 1

print("=====================================")

print(f'{i} {storage_1}')
print(f'{i} {storage_3}')




