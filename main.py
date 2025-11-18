from dataclasses import dataclass, field
from decimal import Decimal
from typing import List 

@dataclass
class Item:
    id: str
    name: str
    price: Decimal
    quantity: int=1
    
    
class EventBus:
    
    def __init__(self):
        self.subscribers = []
    
    def subscribe(self, listener):
        self.subscribers.append(listener)
        
    def publish(self, event_name, data):
        for listener in self.subscribers:
            listener(event_name, data)
        
    
@dataclass
class Cart:
    cart_id:str
    event_bus: EventBus
    items: List[Item] = field(default_factory=list)
    
    def find_by_id_v1(self, item_id: str):
        return next((item for item in self.items if item.id == item_id), None)
    
    def add_item(self, item:Item):
        exists = self.find_by_id_v1(item.id)
        if exists:
            exists.quantity+=item.quantity
        else:
            self.items.append(item)
            self.event_bus.publish("item_added",{"item": item})
        
    def get_items(self):
        return self.items
    
    def get_total(self):
        return sum(list(map(lambda x:x.price, self.items)))