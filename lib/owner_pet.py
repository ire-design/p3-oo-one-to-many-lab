class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    
    all = [] 
    
    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        
        if self.pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {self.pet_type}")
        
        Pet.all.append(self) 
    
    def __repr__(self):
        return f"{self.name} ({self.pet_type})"

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        
        if not isinstance(pet, Pet):
            raise Exception("Only Pet instances can be added.")
        pet.owner = self  

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
    
    def get_pets(self):
        pass
