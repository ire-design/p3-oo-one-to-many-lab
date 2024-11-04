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

