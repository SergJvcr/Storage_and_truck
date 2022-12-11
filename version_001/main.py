from utils import *
from classes import Unit, Storage, Shop, CarParking, Truck, Loader, Timer

kg:Unit = Unit("kg","kilogram")

storage_1 = Storage("Avaron st., 12", 900, 900, kg)
storage_2 = Storage("SaintOcean st, 2/23", 1200, 1200, kg)
storage_3 = Storage("SaintOcean sdfas faefasdf st, 2/23", 1200, 0, kg)

shop_1 = Shop("WildTree st., 65", 300, 300, kg)
shop_2 = Shop("GreenLief st., 1/a", 250, 300, kg)

print(storage_1, '\n' ,storage_2)
print(shop_1, '\n' ,shop_2)

ld: Loader = Loader(2, 0, kg)

trucks: list[Truck] = list()
for i in range(0,3):
    trucks.append(Truck(10,0,kg))

while (not storage_1.is_empty()):
    for t in trucks: 
        cargo = storage_1.take(t.get_capacity())
        t.put(cargo)
        t.run()

        ld.unload(t, t.amount)
        # t.unload()

        print(storage_1)
        print(t)



print("=====================================")
storage_1 = Storage("Avaron st., 12", 900, 900, kg)
storage_3 = Storage("SaintOcean sdfas faefasdf st, 2/23", 1200, 0, kg)

