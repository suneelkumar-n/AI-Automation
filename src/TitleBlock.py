# from practise import Part
# import etract_text as extractclass
# for x0,y0,x1,yx,text,*_ in extractclass.page.get_text("words"):
#     #print(f"{x0:7.1f} {y0:7.1f}  {text}")
#     continue


# p = Part("FL-200", 2.5)           # no 'new'
#print(p.describe())

class Part:
    def __init__(self, number, qty):
        self.number = number
        self.qty = qty

class Assembly:
    def __init__(self, name):
        self.name = name
        self.parts = []                  # like List<Part>

    def add(self, part):
        self.parts.append(part)

    def total_qty(self):
        return sum(p.qty for p in self.parts)


