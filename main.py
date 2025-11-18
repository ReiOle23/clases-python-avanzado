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
    items: dict[Item] = field(default_factory=dict)
    
    def add_item(self, item:Item):
        if item.id in self.items:
            self.items[item.id].quantity+=item.quantity 
        else:
            self.items[item.id]= item
            self.event_bus.publish("item_added",{"item": item})
        
    def get_items(self):
        return self.items
    
    def get_total(self):
        return sum(self.items.values())