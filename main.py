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
        pass
    
@dataclass
class Cart:
    cart_id:str
    event_bus: EventBus
    items: List[Item] = field(default_factory=list)
    
    def add_item(self, item:Item):
        self.items.append(item)
        
    def get_items(self):
        return self.items
    
    def get_total(self):
        return sum(list(map(lambda x:x.price, self.items)))