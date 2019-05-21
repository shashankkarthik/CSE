
##
## Class PetError -- complete
##

class PetError( ValueError ):
    
    pass

##
## Class Pet -- not complete
##

class Pet( object ):
    
    def __init__( self, species=None, name="" ):        
        species_list = ["dog","cat","horse","gerbil","hamster","ferret"]
        if species:
            self.species_str = species.title()
            self.name_str = name.title()
            
        if species.lower() not in species_list:
            
            raise PetError()
            
    def __str__( self ):
        
        result_str = "species of {:s}, named {:s}".format(self.species_str,self.name_str)
        
        return result_str

##
## Class Dog -- not complete
##

class Dog( Pet ):

    def __init__(self,name="",chases="Cats"):
        Pet.__init__(self,"dog",name)
        self.chases_str = chases
    def __str__(self):
        if self.name_str:
            result_str = "species of {:s}, named {:s} and chases {:s}".format(self.species_str,self.name_str,self.chases_str)
        else:
            result_str = "species of {:s}, unamed and chases {:s}".format(self.species_str,self.chases_str)
        
        return result_str
        

##
## Class Cat -- not complete
##

class Cat( Pet ):

    def __init__(self,name="",hates="Dogs"):
        Pet.__init__(self,"cat",name)
        self.hates_str = hates
    def __str__(self):
        if self.name_str:
            result_str = "species of {:s}, named {:s} and chases {:s}".format(self.species_str,self.name_str,self.hates_str)
        else:
            result_str = "species of {:s}, unamed and chases {:s}".format(self.species_str,self.hates_str)
        
        return result_str
