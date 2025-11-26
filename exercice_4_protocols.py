from typing import Protocol

class Pc:
    def __init__(self, os):
        self.os = os
        
class Mobile:
    def __init__(self, os, mpx):
        self.os = os
        self.mpx = mpx

class ComponentFactory(Protocol):
    def create(self):
        ...
        
class PcFactory:
    def create(self, *args, **kwargs):
        return Pc(*args, **kwargs)
        
class MobileFactory:
    def create(self, *args, **kwargs):
        return Mobile(*args, **kwargs)

def produce_component(factory: ComponentFactory, *args, **kwargs):
    return factory.create(*args, **kwargs)    

pc = produce_component(PcFactory(), "Asus")
print("Pc os is ",pc.os)
mobile = produce_component(MobileFactory(),"Asus", 5)
print("Mobile os is ",mobile.os)
print("Mobile mpx is ",mobile.mpx)
