def logic_mixin_factory(mass, mass_attr_name, material, material_attr_name, float_method_name):
    class Mixin:
        def is_a_witch(self):
            if hasattr(self, mass_attr_name) and getattr(self,mass_attr_name) == mass:
                return "Burn her!"
            elif hasattr(self, material_attr_name) and getattr(self, material_attr_name) == material:
                return "Burn her!"
            elif hasattr(self, float_method_name) and callable(getattr(self, float_method_name)):
                return "Burn her!"
            else:
                return "No, but it's a pity, cuz she looks like a witch!"
    return Mixin
