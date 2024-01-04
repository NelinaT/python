import math


class Candy:
    def __init__(self, mass, uranium):
        self.mass = mass
        self.uranium = uranium 

    def get_uranium_quantity(self):
        return self.mass * self.uranium 
    
    def get_mass(self):
        return self.mass
    

class Person:
    def __init__(self, position):
        self.position = position
        self.basket_of_sweets = []

    def  get_position(self):
        return self.position  

    def set_position(self, new_position):
        self.position = new_position
        return self.position


class Kid(Person):
    def __init__(self, position, initiative):
        super().__init__(position)
        self.initiative = initiative
        self.history_of_positions = []
    
    def get_initiative(self):
        return self.initiative
    
    def add_candy(self, sweet):
        self.basket_of_sweets.append(sweet)

    def is_critical(self):
        uranium_q_ty = 0
        critical_uranium_q_ty = 20

        for sweet in self.basket_of_sweets:
            uranium_q_ty += sweet.get_uranium_quantity()
        return uranium_q_ty > critical_uranium_q_ty


class Host(Person):
    def __init__(self, position, candies):
        super().__init__(position)
        self.candies = candies
        
        for candy in self.candies:
            self.basket_of_sweets.append(Candy(*candy))
    
    def remove_candy(self, func):
        if not self.basket_of_sweets:
            return None
        candy = func(self.basket_of_sweets)

        self.basket_of_sweets.remove(candy)
        return candy
    

class FluxCapacitor:
    def __init__(self, participants):
        self.participants = participants
        self.kids = []
        self.hosts = []

        for person in participants:
            if type(person) is Kid:
                self.kids.append(person)
            elif type(person) is Host:
                self.hosts.append(person)

    def set_new_position(self):
        for kid in self.kids:
            distance = 0
            new_position = ()
            list_of_distances_and_positions = []
            for host in self.hosts:
                if host.get_position() in kid.history_of_positions:
                    continue
                distance = math.dist(kid.get_position(), host.get_position())
                list_of_distances_and_positions.append((distance, host.get_position()))
  
            new_position = min(list_of_distances_and_positions)[1]
            kid.set_position(new_position) 
            kid.history_of_positions.append(kid.get_position())

    @staticmethod
    def biggest_sweet(basket_of_sweets):
        biggest_sweet = max(basket_of_sweets, key=lambda x: x.mass)
        return biggest_sweet

    def recieve_candy(self):
        for host in self.hosts:
            kids_with_this_host = []

            for kid in self.kids:
                if kid.get_position() == host.get_position():
                    kids_with_this_host.append(kid)
            
            kids_with_this_host.sort(key=lambda x: x.initiative, reverse = True)
            
            for kid in kids_with_this_host:
                sweet = host.remove_candy(self.biggest_sweet)
                if sweet:
                    kid.add_candy(sweet)

    def take_kids_to_heaven(self):
        kids_in_heaven = set()

        for kid in self.kids:
            if kid.is_critical():
                kids_in_heaven.add(kid)

        return kids_in_heaven
        
    def get_victim(self):
        for host in self.hosts:
            self.set_new_position()
            self.recieve_candy()
            kids_in_heaven = self.take_kids_to_heaven()
           
            if kids_in_heaven:
                return kids_in_heaven
            
        return None   