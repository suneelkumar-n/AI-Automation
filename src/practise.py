# class Part:
#     def __init__(self, number, mass):
#         self.number = number      # attribute is created HERE by assigning it
#         self._mass = mass         # leading _ means "private"

#     @property
#     def mass(self):               # read-only property, like { get; }
#         return self._mass

#     def describe(self) -> str:
#         return f"{self.number}: {self.mass} kg"
    

# main.py
from TitleBlock import Part, Assembly        # like 'using'

asm = Assembly("Pump")
asm.add(Part("FL-200", 2))
asm.add(Part("BLT-M10", 8))
print(asm.total_qty())