import pytest
from decimal import Decimal
from main import Item, EventBus, Cart

@pytest.fixture
def event_bus():
    """EventBus limpio para cada test"""
    return EventBus()

@pytest.fixture
def cart(event_bus):
    """Carrito conectado al EventBus"""
    return Cart(cart_id="cart-001", event_bus=event_bus)

@pytest.fixture
def laptop():
    """Item de ejemplo: Laptop"""
    return Item(
        id="item-001",
        name="Laptop",
        price=Decimal("999.99"),
        quantity=1
    )

@pytest.fixture
def mouse():
    """Item de ejemplo: Mouse"""
    return Item(
        id="item-002",
        name="Mouse",
        price=Decimal("29.99"),
        quantity=1
    )