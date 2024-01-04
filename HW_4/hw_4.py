import weakref

class Potion():
    instances = []

    def __init__(self,effects, duration):
        self.effects = effects
        self.duration = duration
        self.is_depleted = False
        self.is_used_in_reaction = False
        self.__class__.instances.append(weakref.proxy(self))

        for key, value in effects.items():
            setattr(self, "intensity_" + key, 1)
            setattr(self, "is_depleted_" + key, False)
            setattr(self, key, Potion.call_intensity_times(self, key, value))

    @staticmethod
    def call_intensity_times(self, key, value):
        def decorator(target):
            deplete_attr = "is_depleted_" + key
            i = 0
            if not getattr(self,deplete_attr):
                while i < getattr(self,deplete_attr):
                    value(target)
                    i += 1
                setattr(self, "is_depleted_" + key, True)
            else:
                raise TypeError("Effect is depleted.")

        return decorator

    def __add__(self, other_potion):
        Potion.is_depleted_or_used(self, other_potion)
        
        new_duration = max(self.duration, other_potion.duration)
        self.effects.update(other_potion.effects)
        new_potion = Potion(self.effects, new_duration)
        
        for key in self.effects.keys():
            intensity_name = "intensity_" + key
            if hasattr(other_potion, intensity_name) and hasattr(self, intensity_name):
                setattr(new_potion, intensity_name, getattr(self,intensity_name) + getattr(other_potion,intensity_name))
            elif hasattr(other_potion, intensity_name):
                setattr(new_potion, intensity_name, getattr(other_potion,intensity_name))
            else:
                setattr(new_potion, intensity_name,getattr(self, intensity_name))

            Potion.add_attr_used_in_reaction(self,other_potion)

        return new_potion

    def __mul__(self,number):
        Potion.is_depleted_or_used(self)

        for key in self.effects.keys():
            intensity_name = "intensity_" + key
            if 0 < number < 1:
                setattr(self,intensity_name, round( getattr(self,intensity_name)* number))

            elif hasattr(self, intensity_name):
                setattr(self,intensity_name, getattr(self,intensity_name)* number)
            
            Potion.add_attr_used_in_reaction(self)

        return self
    
    def __sub__(self, other_potion):
        Potion.is_depleted_or_used(other_potion)
        
        new_duration = self.duration
        new_potion = Potion(self.effects, new_duration)

        for key in self.effects.keys():
            intensity_name = "intensity_" + key
            if hasattr(other_potion, intensity_name) and hasattr(new_potion, intensity_name):
                if  getattr(new_potion,intensity_name) - getattr(other_potion,intensity_name) < 0:
                    delattr(new_potion, intensity_name)
                else:
                    setattr(new_potion, intensity_name, getattr(self,intensity_name) - getattr(other_potion,intensity_name))
            else: 
                raise TypeError("No such attribute!")
            
            Potion.add_attr_used_in_reaction(self,other_potion)

        return new_potion

    def __truediv__(self,number):
        Potion.is_depleted_or_used(self)
        new_potion = Potion(self.effects, self.duration)
        if number == 1:
            return self

        for key in self.effects.keys():
            intensity_name = "intensity_" + key
            setattr(new_potion,intensity_name, round( getattr(self,intensity_name) / number))
        
        potions = ( new_potion for _ in range(number))
  
        Potion.add_attr_used_in_reaction(self)
               
        return potions

    def __eq__(self,other_potion):
        for key in self.effects.keys():
            intensity_name = "intensity_" + key
            if not hasattr(other_potion,intensity_name):
                return False
            if  getattr(self,intensity_name) != getattr(other_potion,intensity_name):
                return False

        return self.effects == other_potion.effects 
    
    def __gt__(self, other_potion):
        return Potion.get_sum(self) > Potion.get_sum(other_potion)
    
    @staticmethod
    def get_sum(obj):
        sum = 0
        for key in obj.effects.keys():
            intensity_name = "intensity_" + key
            sum += getattr(obj,intensity_name)
        return sum

    @staticmethod
    def is_depleted_or_used(*potions):
        for poiton in potions:
            if poiton.is_depleted:
                raise TypeError("Potion is depleted.")
            if poiton.is_used_in_reaction:
                raise TypeError("Potion is now part of something bigger than itself.")
            
    @staticmethod    
    def add_attr_used_in_reaction(*potions):
        for potion in potions:  
            setattr(potion, "is_used_in_reaction", True)

class ГоспожатаПоХимия():
    def tick():
        all_instances_of_potions = Potion.instances
        for instance in all_instances_of_potions:
            instance.duration = instance.duration - 1

    def apply(self, target, potion):
        Potion.is_depleted_or_used(potion)
        sorted_effects = sorted(potion.effects, reverse = True)
        is_all_depleted = True

        for effect in sorted_effects:
            deplete_attr = "is_depleted_" + effect
            if not getattr(potion,deplete_attr):
                is_all_depleted = False
                getattr(potion, effect)(target)
        if is_all_depleted:
            raise TypeError("Potion is depleted.")
        
        potion.is_depleted = True
