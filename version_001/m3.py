# import model.Unit as Unit, model.Storage as Storage, model.Shop as Shop, model.Loader as Loader, model.Truck as Truck
# import model.Truck as Truck
# import model.Unit as Unit

# import model.Unit as Unit

from model.ActorStatus import ActorStatus
from model.Actor import Actor

from model.Unit import Unit
from model.Storage import Storage
from model.Truck import Truck
from model.Loader import Loader
from model.Loader3 import Loader3

kg:Unit = Unit("kg","kilogram")

# print(Truck(1000,200, kg))
print(kg)

print("jsdfjksdf")

print(type(Unit))
# print(Unit.Unit())


actorStatus = ActorStatus("sss","s",[])
print(actorStatus)

actor: Actor = Actor(actorStatus)
print(actor)

ld3:Loader3 = Loader3(actorStatus)
print(ld3)
