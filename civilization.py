#необходимые константы 
REPRODUCE_NEW_COEF=5.5
REPRODUCE_POPULATION_COEF=10
REPRODUCE_OLD_COEF = 3
ID_COUNTER=0
MAX_HERBIVORE_AGE = 3
MAX_PLANT_AGE=2
PLANT_ENERGY_INC_COEF = 3
SHORT_LIFESPAN_COEF=0.2
LONG_LIFESPAN_ENERGY_COEF = 0.5
LONG_LIFESPAN_COEF = 2
SHORT_LIFESPAN_ENERGY_COEF = 2.5
HIGH_FERTILITY_COEF = 2.3
HIGH_FERTILITY_ENERGY_COEF=1.5
MUTATION_POSSIBILITY = 60
PLANT_EATEN_COEF = 4
PLANT_ENERGY_EATEN_COEF = 2
TOXIC_COEF = 2
RESILIENT_COEF=1.5



#основная часть

from abc import ABC, abstractmethod
import random

class Organism(ABC):
    toxicity = False
    resilient_coef = 1
    identifiestoxicplants = False
    resilienttotoxicplants = False
    longlifespan_en_coef = 1
    shortlifespan_en_coef = 1
    longlifespan_age_coef = 1
    shortlifespan_age_coef = 1
    fertility_population_multiplier = 1
    fertility_energy_decreaser = 1
    
    @property
    def alive(self):
        return (self.current_age<=self.max_age) and (self.current_energy>0)
    @alive.setter
    def alive(self, boolean_value):
        if boolean_value:
            self.current_age= self.max_age-1
        else:
            self.current_age= self.max_age+1 
    
    
    def __bool__(self):
        return self.alive
        
    @classmethod 
    def spawn(cls, population_size, current_age):
        new_one = cls()
        new_one.population_size = population_size
        new_one.current_age = current_age
        return new_one
    
    @abstractmethod
    def __str__(self):
        pass
    @abstractmethod
    def replenish_energy(self):
        pass
        
    def __init__(self):
        
        self.population_size = 0
        self.current_age = 0
        self.current_energy = 0
        global ID_COUNTER
        ID_COUNTER+=1
        self.id=ID_COUNTER
        
    def reproduce(self):
        if (self.current_energy>0) and (self.current_age<=self.max_age) :
            child = self.__class__()
            child.current_age = 0
            child.current_energy = self.current_energy/int(REPRODUCE_NEW_COEF)* self.fertility_energy_decreaser
            child.population_size  = self.population_size /int(REPRODUCE_POPULATION_COEF) * self.fertility_population_multiplier
            self.current_energy = self.current_energy/REPRODUCE_OLD_COEF/ self.fertility_energy_decreaser
            print(f'{self} размножилось, родился ребенок - {child}. Популяция родителя - {self.population_size}, популяция ребенка - {child.population_size}')
            return child
        print(f'{self} мертво')

    
    def mutate(self):
        num = random.randint(1,100)
        if num<=MUTATION_POSSIBILITY:

            new_mixin = random.choice(self._possible_mixins)
            if not new_mixin in self.__class__.__mro__:

        # проверка, есть ли new_mixin в self.__classes__.__bases__ ?
                new_class = type("some_name", (new_mixin, ) + (self.__class__,), {})
                # self.__class__ = new_class
                new_self = new_class()
                new_self.__dict__ = self.__dict__
                print(f'Добавился миксин {new_mixin}')
                return new_self

                # new_self = new_class()
                # new_self.__dict__ = self.__dict__

                # return new_self
                # a = a.mutate()
            else:
                print(f'У {self} уже есть миксин {new_mixin}')
                return self
        else:
            if not (set(self._possible_mixins) & set(self.__class__.__bases__)):
                print(f'У организма {self} еще нет миксинов')
                return self

            else:
                flag=True
                while flag:
                    deleted_parent = random.choice(self.__class__.__bases__)
                    if deleted_parent in self._possible_mixins:
                        flag=False
                new_class = type("some_name1", tuple(i for i in  self.__class__.__bases__ if i!= deleted_parent) , {})
                new_self = new_class()
                new_self.__dict__ = self.__dict__
                print(f'Миксин {deleted_parent} удален')
                return new_self
        # либо удаляем старый

        
        
    def ShortLifespan_method(self):
        pass
        
    def LongLifespan_method(self):
        pass

    def HighFertility_method(self):
        pass

    def Toxic_method(self):
        pass

    def IdentifiesToxicPlants_method(self):
        pass

    def ResilientToToxicPlants_method(self):
        pass


class ShortLifespanMixin:
    def ShortLifespan_method(self):
        self.shortlifespan_age_coef = SHORT_LIFESPAN_COEF 
        self.longlifespan_en_coef = SHORT_LIFESPAN_ENERGY_COEF
       
        
class LongLifeSpanMixin:
    def LongLifespan_method(self):
        self.longlifespan_age_coef = LONG_LIFESPAN_COEF
        self.shortlifespan_en_coef = LONG_LIFESPAN_ENERGY_COEF


class HighFertilityMixin:
    def HighFertility_method(self):
        self.fertility_population_multiplier = HIGH_FERTILITY_COEF
        self.fertility_energy_decreaser = HIGH_FERTILITY_ENERGY_COEF

class ToxicMixin:
    def Toxic_method(self):
        self.toxicity = True


class IdentifiesToxicPlantsMixin:
    def IdentifiesToxicPlants_method(self):
        self.identifiestoxicplants = True

class ResilientToToxicPlantsMixin:
    def ResilientToToxicPlants_method(self):
        self.resilient_coef = RESILIENT_COEF
    
    


class Herbivore(Organism):
    _possible_mixins = [ShortLifespanMixin, LongLifeSpanMixin, HighFertilityMixin, IdentifiesToxicPlantsMixin, ResilientToToxicPlantsMixin]
    energy_consumption = 5
    def __init__(self):
        super().__init__()
        self.ShortLifespan_method()
        self.LongLifespan_method()
        self.HighFertility_method()
        self.IdentifiesToxicPlants_method()
        self.ResilientToToxicPlants_method()
        self.max_age = MAX_HERBIVORE_AGE*self.longlifespan_age_coef*self.shortlifespan_age_coef
        

    def __str__(self):
        return f'Травоядное c id {self.id} (возраст - {self.current_age}, запас энергии - {self.current_energy}, продолжительность жизни - {self.max_age})'

    def replenish_energy(self, plant):
        if plant.toxicity:
            if (self.identifiestoxicplants):
                print(f'{self} отказалось лакомиться организмом {plant} из-за токсичности')
            else:
                old_population = self.population_size
                self.population_size /= (TOXIC_COEF/self.resilient_coef)
                print(f'{self} съело токсичное {plant}, популяция сокращена c {old_population} до {self.population_size} ')
            
        else:
            plant.population_size /= PLANT_EATEN_COEF
            energy_before_eating = plant.current_energy
            plant.current_energy /= PLANT_ENERGY_EATEN_COEF
            delta_energy = energy_before_eating - plant.current_energy
            old_energy = self.current_energy
            self.current_energy += delta_energy*self.shortlifespan_en_coef*self.longlifespan_en_coef
            print(f'{self} полакомилось {plant} и пополнил свою энергию на {self.current_energy-old_energy}')
    




class Plant(Organism):
    _possible_mixins = [ShortLifespanMixin, LongLifeSpanMixin, HighFertilityMixin, ToxicMixin]
    energy_consumption = 3
    def __init__(self):
        super().__init__()
        self.ShortLifespan_method()
        self.LongLifespan_method()
        self.HighFertility_method()
        self.Toxic_method()
        self.max_age = MAX_PLANT_AGE*self.longlifespan_age_coef*self.shortlifespan_age_coef

    def replenish_energy(self):
        self.current_energy += PLANT_ENERGY_INC_COEF*self.shortlifespan_en_coef*self.longlifespan_en_coef
        print(f'{self} пополнило свою энергию')

    def __str__(self):
        return f'Растение c id {self.id} (возраст - {self.current_age}, запас энергии - {self.current_energy}, продолжительность жизни - {self.max_age})'
    

class Game:
    def __init__(self):
        self.plants = []
        self.herbivores = []
        for i in range(5):  # 5 травоядных
            herb = Herbivore()
            herb.population_size = (i+2)*100
            herb.current_energy = (i+1)*40
            self.herbivores.append(herb)
        
        
    
        for i in range(10):  # 10 растений
            pl = Plant()
            pl.population_size = (i+3)*110
            pl.current_energy = (i+1)*20
            self.plants.append(pl)
            
        
    def correct_age_energy(self):
        dead_organisms = []
        for org in self.plants+self.herbivores:
            org.current_energy -= org.energy_consumption
            org.current_age += 1
            if not org.alive:
                dead_organisms.append(org)
                print(f'Умерло {org}')
        alive_plants = [organ for organ in self.plants if organ not in dead_organisms]
        alive_herbivores = [organ for organ in self.herbivores if organ not in dead_organisms]
        self.plants = alive_plants
        self.herbivores = alive_herbivores
        
    def cycle_through_actions(self):
        new_organisms = []
        for org in self.plants+self.herbivores:
            action = random.choice(['replenish_energy', 'reproduce', 'mutate'])
            if action == 'replenish_energy':
                if isinstance(org, Herbivore):
                    miserable_plant = random.choice(self.plants)
                    org.replenish_energy(miserable_plant)     
                elif isinstance(org,Plant):
                    org.replenish_energy()
            elif action == 'reproduce':
                org_child = org.reproduce()
                new_organisms.append(org_child)
                
            elif action=='mutate':
                org = org.mutate()
        for new_org in new_organisms:
            if isinstance(new_org, Herbivore):
                self.herbivores.append(new_org)
            elif isinstance(new_org, Plant):
                self.plants.append(new_org)
        

    def play_game(self,n):
        for i in range(n):
            print(f'ПРОШЛО {i} ЛЕТ С МОМЕНТА ЗАПУСКА')
            self.cycle_through_actions()
            self.correct_age_energy()
            print(f'Осталось {len(self.plants)} живых растений и {len(self.herbivores)} живых травоядных')


#запуск

my_game = Game()
my_game.play_game(4)

