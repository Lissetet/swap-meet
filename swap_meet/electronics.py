from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, type="Unknown", id=None, condition=0, age="Unknown"):
        super().__init__(id, condition, age)
        self.type = type

    def __str__(self):
        return f"{super().__str__()} This is a {self.type} device."
