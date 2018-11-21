import dateutil
import datetime
class Person(object): 
    def __init__(self,first_name=None,last_name=None,
                 middle_name='',sex='F', dob=None, **kwargs):
        self.sex = sex
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        if dob == None:
            self.__dob = None
        elif isinstance(dob,str):
            try:
                self.__dob = dateutil.parser.parse(dob)
            except Exception as error:
                print(error)
                self.__dob = None
        elif isinstance(dob.datetime.date):
            self.__dob = dob
        else:
            raise TypeError("Invalid date of birth specification")
        
        
    @property
    def dob(self):
        return self.__dob
    @property
    def age(self):
        td = datetime.datetime.now()-self.__dob
        return {"years":td.days//365, "months":td.days%365//30}
        
    @property
    def sex(self):
        return self.__sex
    @sex.setter
    def sex(self, value):
        if not isinstance(value,str):
            raise TypeError("Sex must be a string")
        if not value.upper()[0] in "MF":
            raise ValueError("Sex must be Male or Female")
        self.__sex = value.upper()[0]
    @property 
    def first_name(self):
        return self.__first_name
    @first_name.setter
    def first_name(self, value):
        if value == None:
            if self.sex == 'F':
                value = "Jane"
            else:
                value = "John"
        if not isinstance(value,str):
            raise TypeError("first name must be a string")
        self.__first_name = value
    @property 
    def last_name(self):
        return self.__last_name
    @last_name.setter
    def last_name(self, value):
        if value == None:
            value = "Doe"
        if not isinstance(value,str):
            raise TypeError("last name must be a string")
        self.__last_name = value
        
    @property 
    def middle_name(self):
        return self.__middle_name
    @middle_name.setter
    def middle_name(self, value):

        if not isinstance(value,str):
            raise TypeError("last name must be a string")
        self.__middle_name = value
    def get_full_name(self):
        name = "%s %s %s"%(self.first_name,
                           self.middle_name,
                           self.last_name)
        return name
        
    def __repr__(self):
        """Get the individual characteristics in a string"""
        txt = """First Name=%s\n"""%self.first_name
        txt += """Middle Name=%s\n"""%self.middle_name
        txt +="""Last Name=%s\n"""%self.last_name
        txt += """Sex=%s\n"""%self.sex
        txt += "Age=%d years, %d months\n"%(self.age["years"],
                                            self.age["months"])
        return txt
    
    def __str__(self):
        return """%s %s (Age=%d years, %d months)"""%(self.first_name,
                                                      self.last_name,
                                                      self.age["years"],
                                                      self.age["months"])
    def __lt__(self,p):
        return self.dob < p.dob
    def __le__(self,p):
        return self.dob <= p.dob
    def __gt__(self,p):
        return self.dob > p.dob
    def __ge__(self,p):
        return self.dob >= p.dob
    def __eq__(self,p):
        return self.dob == p.dob
    def __ne__(self,p):
        return self.dob != p.dob