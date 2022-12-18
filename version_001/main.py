# from model import Unit, Storage, Shop, Loader, Actor, Truck
# import model.Unit as Unit, model.Storage as Storage, model.Shop as Shop, model.Loader as Loader, model.Truck as Truck

from model.Unit import Unit
from model.Storage import Storage
from model.Truck import Truck
from model.Loader import Loader
from model.Shop import Shop
from model.ActorStatus import ActorStatus


kg:Unit = Unit("kg","kilogram")
AS_READY : ActorStatus = ActorStatus("READY","Готов",[])

storage_1 = Storage("Avaron st., 12", 900, 893, kg)
storage_2 = Storage("SaintOcean st, 2/23", 1200, 1200, kg)
storage_3 = Storage("SaintOcean sdfas faefasdf st, 2/23", 2000, 0, kg)

shop_1 = Shop("WildTree st., 65", 300, 300, kg)
shop_2 = Shop("GreenLief st., 1/a", 250, 300, kg)

print(storage_1, '\n' ,storage_2)
print(shop_1, '\n' ,shop_2)

ld: Loader = Loader(2, 0, kg, AS_READY)

trucks: list[Truck] = list()
for i in range(0,6):
    trucks.append(Truck(10,0,kg))

i = 1
while (not storage_1.is_empty()):
    for t in trucks:
        t.put(storage_1.take(t.get_capacity()))
        # print(t)

        storage_3.put(t.take(t.get_amount()))

    # print(f'{i} {storage_1}')
    # print(f'{i} {storage_3}')
    i += 1

print("=====================================")

print(f'{i} {storage_1}')
print(f'{i} {storage_3}')




