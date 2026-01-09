from math import ceil
from abc import ABC, abstractmethod
from enum import Enum

class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient

class Property(ABC):
    @abstractmethod
    def __init__(self, locality):
        self.locality = locality

    @abstractmethod
    def calculate_tax(self):
        pass

class EstateType(Enum):
    LAND = 1
    BUILDING_SITE = 2
    FORREST = 3
    GARDEN = 4

class Estate(Property):
    def __init__(self, locality, estate_type, area):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area
    
        # Pomocný slovník pro výpočet daně:
        self.tax_coefficient = {
            EstateType.LAND: 0.85,
            EstateType.BUILDING_SITE: 9,
            EstateType.FORREST: 0.35,
            EstateType.GARDEN: 2
        }

        # Pomocný slovník pro názvy typů pozemků:
        self.estate_names = {
            EstateType.LAND: "Zemědělský pozemek",
            EstateType.BUILDING_SITE: "Stavební pozemek",
            EstateType.FORREST: "Les",
            EstateType.GARDEN: "Zahrada"
        }

    def calculate_tax(self):
        tax = self.area * self.tax_coefficient[self.estate_type] * self.locality.locality_coefficient
        return ceil(tax)
    
    def __str__(self):
        return f"{self.estate_names[self.estate_type]} o rozloze {self.area} metrů čtverečních, lokalita {self.locality.name}, daň {self.calculate_tax()} Kč."
    
class Residence(Property):
    def __init__(self, locality, area, commercial):
        super().__init__(locality)
        self.area = area
        self.commercial = commercial
    
    def calculate_tax(self):
        residence_tax = self.area * self.locality.locality_coefficient * 15

        if self.commercial:
            residence_tax = 2 * residence_tax
        
        return ceil(residence_tax)
    
    def __str__(self):
        base_string = f"Nemovitost s podlahovou plochou {self.area} metrů čtverečních, lokalita {self.locality.name}, daň {self.calculate_tax()} Kč"

        if self.commercial:
            return base_string + ", je využívaná ke komerčním účelům."
        else:
            return base_string + ", není využívaná ke komerčním účelům."
        
manetin = Locality("Manětín", 0.8)
brno = Locality("Brno", 3)

pozemek = Estate(manetin, EstateType.LAND, 900)
print(pozemek.calculate_tax())
print(pozemek)

dum = Residence(manetin, 120, False)
print(dum.calculate_tax())
print(dum)

kancelar = Residence(brno, 90, True)
print(kancelar.calculate_tax())
print(kancelar)

class TaxReport:
    def __init__(self, name, property_list):
        self.name = name
        self.property_list = property_list
    
    def add_property(self, property):
        return self.property_list.append(property)
    
    def calculate_tax(self):
        tax = 0
        for property in self.property_list:
            tax += property.calculate_tax()
        
        return ceil(tax)

# kontrolní výpočty:

# lokalita = Locality("někde", 2)
# zkusebni_pozemek = Estate(lokalita, EstateType.FORREST, 500)
# print(zkusebni_pozemek.calculate_tax())

# lokalita_2 = Locality("někde", 3)
# zkusebni_byt = Residence(lokalita_2, 60, False)
# print(zkusebni_byt.calculate_tax())
# zkusebni_byt2 = Residence(lokalita_2, 60, True)
# print(zkusebni_byt2.calculate_tax())

# tax_report = TaxReport("Jan Novák", [pozemek])
# tax_report.property_list.append(dum)
# print(tax_report.calculate_tax())