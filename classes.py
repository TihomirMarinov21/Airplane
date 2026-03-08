import random
import asyncio
from typing import List
import nicegui as ui


class Airplane:
    """Represents an airplane with altitude, passengers and basic flight actions."""

    def __init__(self) -> None:
        self.passenger_count: int = 0
        self.z: int = 0  # current altitude in meters
        self.passengers: List[dict] = []  # optional: store passenger objects later
    async def start(self, height_label) -> None:
        """Simulates the airplane taking off and loading registered passengers."""
        # plane rises
        while self.z < 1000:
            self.z += 10
            if 10 < self.z < 1000:
                height_label.set_text("Plane is rising")
            elif self.z == 1000:
                height_label.set_text("Plane has reached max height !!!")
            await asyncio.sleep(0.1)


    async def land(self, height_label) -> None:
        """Simulates the airplane descending and unloading passengers."""
        while self.z != 0:
            self.z -= 10
            if 10 < self.z < 1000:
                height_label.set_text("Plane is Descending !!!")
            elif self.z == 0:
                height_label.set_text("Plane has landed")
            await asyncio.sleep(0.1)
        #unload passengers gradually
        while self.passenger_count > 0:
            self.passenger_count -= 1
            await asyncio.sleep(0.1)


class Person:
    """Randomly generated person used for crew simulation."""

    def __init__(self) -> None:
        self.first_name: str = random.choice(["John", "Anna", "Max", "Lena", "Marie"])
        self.last_name: str = random.choice(["Smith", "Müller", "Johnson", "Schmidt", "Williams"])
        self.age: int = random.randint(18, 60)


class Pilot(Person, Airplane):
    """Pilot inherits random personal data and airplane attributes (for simplicity)."""

    def __init__(self) -> None:
        super().__init__()
