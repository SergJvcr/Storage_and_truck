# import model.Unit as Unit, model.Storage as Storage, model.Shop as Shop, model.Loader as Loader, model.Truck as Truck
import model.Unit as Unit, model.Truck as Truck

kg:Unit = Unit("kg","kilogram")

print(Truck(1000,200, kg))

