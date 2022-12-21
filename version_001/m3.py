# import model.Unit as Unit, model.Storage as Storage, model.Shop as Shop, model.Loader as Loader, model.Truck as Truck
# import model.Truck as Truck
# import model.Unit as Unit

# import model.Unit as Unit

from model.ActorStatus import ActorStatus
from model.Actor import Actor

from model.Unit import Unit
from model.Storage import Storage
from model.Truck import Truck
from model.Loader import Loader, LOADER_READY, LOADER_LOADING, LOADER_UNLOADING
from model.Loader3 import Loader3
from model.Capacity import Capacity

kg:Unit = Unit("kg","kilogram")

# print(Truck(1000,200, kg))
print(kg)

print("jsdfjksdf")

print(type(Unit))
# print(Unit.Unit())

# global LOADER_READY, LOADER_LOADING
actorStatus = LOADER_READY
print(actorStatus)

actor: Actor = Actor(actorStatus)
print(actor)

ld3:Loader3 = Loader3(actorStatus)
print(ld3)

cp0:Capacity = Capacity(210, 200, kg)
cp1:Capacity = Capacity(110, 0, kg)
cp2:Capacity = Capacity(20, 0, kg)

print(cp0)
print(cp1)
print(cp2)

while (cp1.get_avail_capacity()>0):
    m = cp1.get_avail_capacity()
    m = min(m, cp2.get_avail_capacity())
    cp2.put(cp0.take(m))
    cp1.put(cp2.takeAll())

print(cp0)
print(cp1)
print(cp2)


