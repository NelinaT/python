
        

def logic_mixin_factory(mass, mass_attr_name, material,material_attr_name, float_method_name):
    class Mixin:
        def is_a_witch(self):
            if  self.__getattribute__(mass_attr_name) == mass:
                return "Burn her"
            elif self.__getattribute__(material_attr_name) ==  material:
                return "Burn her"
            elif type(self.__getattribute__(float_method_name)) is function:
                return "Burn her"
            else:
                return "No, but it's a pity, cuz she looks like a witch!"
    return Mixin
LogicMixin = logic_mixin_factory(20, 'mass', 'wood', 'material', 'float')

class Woman(LogicMixin):
    def __init__(self):
        self.mass = 2
        self.material = ''
    def float():
       pass

woman = Woman()

print(woman.is_a_witch())