import pytest, math
from HW_3 import Candy, Person, Kid, Host, FluxCapacitor

def test_args_candy():
    assert Candy(0, 0).mass == 0
    assert Candy(0, 0).uranium == 0

    assert Candy(0, 0.5).mass == 0
    assert Candy(0, 0.5).uranium == 0.5

    assert Candy(1, 0.2).mass == 1
    assert Candy(1, 0.2).uranium == 0.2

    assert Candy(5, 0.5).mass == 5
    assert Candy(5, 0.5).uranium == 0.5

    assert Candy(500, 1).mass == 500
    assert Candy(500, 1).uranium == 1


def test_get_mass():
    assert Candy(0, 0).get_mass() == 0
    assert Candy(0, 0.5).get_mass() == 0
    assert Candy(1, 0.2).get_mass() == 1
    assert Candy(5, 0.5).get_mass() == 5
    assert Candy(500, 1).get_mass() == 500



def test_get_uranium_quantity():
    assert Candy(0, 0).get_uranium_quantity() == 0
    assert Candy(0, 0.5).get_uranium_quantity() == 0
    assert Candy(1, 0.2).get_uranium_quantity() == 0.2
    assert Candy(5, 0.5).get_uranium_quantity() == 2.5
    assert Candy(500, 1).get_uranium_quantity() == 500



def test_args_person():
    assert Person((0, 0)).position == (0, 0)
    assert Person((0, 1)).position == (0, 1)
    assert Person((1, 2)).position == (1, 2)
    assert Person((2, 2)).position == (2, 2)
    assert Person((3, 2)).position == (3, 2)
    assert Person((3, 0)).position == (3, 0)

def test_get_position():
    assert Person((0, 0)).get_position() == (0, 0)
    assert Person((0, 1)).get_position()  == (0, 1)
    assert Person((1, 2)).get_position()  == (1, 2)
    assert Person((2, 2)).get_position()  == (2, 2)
    assert Person((3, 2)).get_position()  == (3, 2)
    assert Person((3, 0)).get_position()  == (3, 0)
   
people = [Person((0, 0)),Person((0, 1)), Person((1, 2)), Person((2, 2)),Person((3, 2)), Person((3, 0))]

def test_set_position():
    new_position = (20, 50)
    for i in people:
        i.set_position(new_position) 
        assert i.position == new_position
 


def test_args_Kid():
    assert Kid((0,0),0).position == (0,0) 
    assert Kid((0,0),0).initiative == 0 

    assert Kid((0,0),1).position == (0,0) 
    assert Kid((0,0),1).initiative == 1

    assert Kid((0,5),0).position == (0,5) 
    assert Kid((0,5),0).initiative == 0 
    
    assert Kid((0,5),1).position == (0,5) 
    assert Kid((0,5),1).initiative == 1

    assert Kid((5,0),0).position == (5,0) 
    assert Kid((5,0),0).initiative == 0 

    assert Kid((5,0),1).position == (5,0) 
    assert Kid((5,0),1).initiative == 1 

    assert Kid((5,1),0).position == (5,1) 
    assert Kid((5,1),0).initiative == 0 

    assert Kid((5,1),3).position == (5,1) 
    assert Kid((5,1),3).initiative == 3

    assert Kid((5,5),5).position == (5,5) 
    assert Kid((5,5),5).initiative == 5

def test_get_initiative():
    assert Kid((0,0), 0).get_initiative() == 0
    assert Kid((5,1), 2).get_initiative() == 2

def test_add_candy():
    pesho = Kid((5,1),3)
    bonbon = Candy(10, 0.25)

    assert len(pesho.basket_of_sweets) == 0

    pesho.add_candy(bonbon)

    assert len(pesho.basket_of_sweets) == 1 and pesho.basket_of_sweets[0].mass == bonbon.mass and pesho.basket_of_sweets[0].uranium == bonbon.uranium
    kitkat = Candy(2, 0.6)
    pesho.add_candy(kitkat)
    assert len(pesho.basket_of_sweets) == 2 and pesho.basket_of_sweets[1].mass == kitkat.mass and pesho.basket_of_sweets[1].uranium == kitkat.uranium and pesho.basket_of_sweets[0].mass == bonbon.mass and pesho.basket_of_sweets[0].uranium == bonbon.uranium



def test_is_critical():
    
    pesho = Kid((5,1),3)

    assert pesho.is_critical() == False

    pesho.basket_of_sweets = [Candy(10, 0.5), Candy(20, 0.75)]

    assert pesho.is_critical() == False

    pesho.basket_of_sweets = [Candy(10, 0.5), Candy(20, 1)]
    assert pesho.is_critical() == True

    pesho.basket_of_sweets = [Candy(5, 0.5), Candy(10, 1), Candy(15, 0.1), Candy(8,0.9)]
    assert pesho.is_critical() == True



def test_Host_remove_candy():

    Ivo = Host((1,2),[])
    assert Ivo.remove_candy(FluxCapacitor.biggest_sweet) == None

    kitkat = Candy(41, 0.3)
    Gosho = Host((1,2),[(5, 0.2), (41, 0.3)])
    removed_candy = Gosho.remove_candy(FluxCapacitor.biggest_sweet)
    assert removed_candy.mass == kitkat.mass and removed_candy.uranium == kitkat.uranium

    Eli = Host((1,2),[(5, 0.2), (41, 0.3)])
    snickers = (20, 0.2)
    removed_candy = Eli.remove_candy(FluxCapacitor.biggest_sweet)
    assert removed_candy.mass == kitkat.mass and removed_candy.uranium == kitkat.uranium


def test_FluxCapacitor():
    pesho = Kid((2,2), 9)
    mimi = Kid((3,1), 10)
    tom = Kid((-3,1), 1)

    Gosho = Host((3,2),[(1, 0.2),(200, 0.9)])
    misho = Host((-3,2),[(1, 0.2),(10, 0)])

    nino = Host((1,2),[(3, 0.1),(10, 0.2)])
    Tino = Host((1,3),[(3, 0.1),(10, 0.2)])
    
    participants = FluxCapacitor({pesho, Gosho, mimi})
    assert participants.get_victim() == {mimi}
    
    participants = FluxCapacitor({mimi, Gosho, tom })
    assert participants.get_victim() == {mimi}
    
    participants = FluxCapacitor({pesho, Gosho, tom })
    assert participants.get_victim() == None

    participants = FluxCapacitor({misho, tom})
    assert participants.get_victim() == None



   








