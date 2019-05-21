################################################################################
# Computer Project 11
#   Class Time
################################################################################

class Time(object):     
    def __init__(self,h=0,m=0,s=0,o=0):
        '''Creates Time object with hours,minutes,
           seconds and UTC offset'''
        #Checks if the hours, minutes, seconds and offset are integers
        if type(h) is int and type(m) is int and \
        type(s) is int and type(o) is int:
            self.h = self.m = self.s = 0                
                
            #Accounts for the seconds being greater than 60 or less than 0
            if s >= 60:
                m += s//60
                s = s % 60
            while s < 0:
                s += 60
                m -= 1
            if s <= 59 and s >= 0:
                self.s += s
            
            #Accounts for the minutes being greater than 60 or less than 0   
            if m > 59:
                h += m//60
                m = m % 60
            while m < 0:
                m += 60
                h -= 1
            if m <= 59 and m >= 0:
                self.m += m
                
            #Accounts for the hours being greater than 23 or less than 0
            while h > 23:
                h -= 24
            while h < 0:
                h += 24
            if h <= 23 and h >= 0:
                self.h += h  
                
                
                if abs(o) <= 12:
                    self.o = o
                else:
                    raise ValueError
                    
            else:
                raise ValueError
                
        else:
            raise ValueError
    
    def __str__(self):
        '''Creates string of time object formatted
           as hh:mm:ss+zz or hh:mm:ss-zz'''
        #Checks if there are 2 digits for hours, if not, adds a leading 0
        h_str = str(self.h)
        if len(h_str) < 2:
            lst = ["0"]
            lst.append(h_str)
            h_str = "".join(lst)            
        
        #Checks if there are 2 digits for minutes, if not, adds a leading 0
        m_str = str(self.m)
        if len(m_str) < 2:
            lst = ["0"]
            lst.append(m_str)
            m_str = "".join(lst)
        
        #Checks if there are 2 seconds for hours, if not, adds a leading 0
        s_str = str(self.s)
        if len(s_str) < 2:
            lst = ["0"]
            lst.append(s_str)
            s_str = "".join(lst)
        #Checks if there are 2 digits the offset, if not, adds a leading 0
        o_str = str(abs(self.o))
        if len(o_str) < 2:
            lst = ["0"]
            lst.append(o_str)
            o_str = "".join(lst)

        #Prints formatted string        
        if self.o >= 0:
            time_str = "{}{}{}{}{}{}{}".format\
            (h_str,":",m_str,":",s_str,"+",o_str)
        
        if self.o < 0:
            time_str = "{}{}{}{}{}{}{}".format\
            (h_str,":",m_str,":",s_str,"-",o_str)
        
        return time_str
    
    def __repr__(self):
        '''Returns correctely formatted time 
           object'''
        return str(self)
    
    def validate_str(self,other):
        '''Validates if string is in correct 
           format'''
        valid = False
        if type(other) is str:
            if len(other) == 11:
                if other[2] == other[5] == ":":
                    if other[8] == "+" or other[8]== "-":
                        count = 0
                        for i in other:
                            if other.index(i) not in [2,5,8]:
                                if i.isdigit():
                                    count+= 1
                                if count == 8:
                                    valid = True
                                    
        return valid
    
    def from_str(self,other):
        '''Converts string to time object'''
        if self.validate_str(other):
            h = int(other[0:2])
            m = int(other[3:5])
            s = int(other[6:8])
            o = int(other[8:])
        
        if h > 23 or m > 59 or s > 59 or abs(o)>12:
            raise ValueError
        else:
            self.h = h
            self.m = m
            self.s = s
            self.o = o
            
            
    def get_as_local(self):
        '''Converts 24hr clock to 12hr clock'''
        #Special conditions if time is noon or midnight
        if self.h == self.m == self.s == 0:
            return "Midnight"
        if self.h == 12 and self.m == self.s == 0:
            return "Noon"
        #Sets AM and PM time frames
        if self.h >= 0 and self.h <= 11:
            period = "AM"
        elif self.h >=12 and self.h <=23:
            self.h -= 12
            period = "PM"
            
        h_str = str(self.h)
        if len(h_str) < 2:
            lst = ["0"]
            lst.append(h_str)
            h_str = "".join(lst)            
        m_str = str(self.m)
        if len(m_str) < 2:
            lst = ["0"]
            lst.append(m_str)
            m_str = "".join(lst)
        s_str = str(self.s)
        if len(s_str) < 2:
            lst = ["0"]
            lst.append(s_str)
            s_str = "".join(lst)
        
        time_str = "{}{}{}{}{}{}".format(h_str,":",m_str,":",s_str,period)
        return time_str
        
        
    def adjust_to_UTC(self):
        '''Adjusts for the UTC offset'''

        h_new = self.h - self.o
        if h_new > 23:
            h_new -= 24
        elif h_new < 0:
            h_new += 24
        
        return Time(h_new,self.m,self.s,0)
        

    def __eq__(self,other):
        '''Checks if two times are the same'''
        if type(other) is Time:
            self_adjusted = self.adjust_to_UTC()
            other_adjusted = other.adjust_to_UTC()
            
            if self_adjusted.h == other_adjusted.h:
                if self.m == other.m:
                    if self.s == other.s:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            raise TypeError
            
    
    def __ne__(self,other):
        '''Checks if two time are not the same'''
        if type(other) is Time:
            if self == other:
                return False
            else:
                return True
        else:
            raise TypeError
    
    
    def __lt__(self,other):
        '''Checks if one time is less than the 
           other'''
        if type(other) is Time:
            self_adjusted = self.adjust_to_UTC()
            other_adjusted = other.adjust_to_UTC()
            
            if self_adjusted.h < other_adjusted.h:
                return True
            elif self_adjusted.h >other_adjusted.h:
                return False
            elif self_adjusted.h==other_adjusted.h:
                if self.m < other.m :
                    return True
                elif self.m > other.m :
                    return False
                elif self.m == other.m :
                    if self.s < other.s :
                        return True
                    else:
                        return False                         
        else:
            raise TypeError
            
            
    def __gt__(self,other):
        '''Checks if one time is greater than the 
           other'''
        if type(other) is Time:
            
            if self < other:
                return False
            elif self == other:
                return False
            else:
                return True
        else:
            raise TypeError
    
    
    def __le__(self,other):
        '''Checks if one time is less than
           or equal to the other'''
        if type(other) is Time:
            if self < other or self == other:
                return True
            else:
                return False
        else:
            raise TypeError

    def __ge__(self,other):
        '''Checks if one time is greater than
           or equal to the other'''
        if type(other) is Time:
            if self > other or self == other:
                return True
            else:
                return False
        else:
            raise TypeError
            
    def __add__(self,other):
        '''Adds an integer number of seconds to the
           time object'''
        h = self.h
        m = self.m
        s = self.s
        o = self.o
        if type(other) is int:
            s += other
            return Time(h,m,s,o)
        else:
            raise ValueError
                 

    def __sub__(self,other):
        '''Subtracts two Time objects and returns
           the number of seconds by which they 
           differ.'''
        
        HOURS_TO_SECONDS = 3600
        MINUTES_TO_SECONDS = 60        
        
        if type(other) is Time:
            
            self_adjusted = self.adjust_to_UTC()
            other_adjusted = other.adjust_to_UTC()
            
            sec_diff = 0
            
            #Finds difference in hours, converts it to seconds and adds it to
            #the ongoing count
            h_diff = self_adjusted.h - other_adjusted.h
            sec_diff += h_diff * HOURS_TO_SECONDS

            #Finds difference in minutes, converts it to seconds and adds it to
            #the ongoing count
            m_diff = self.m - other.m
            sec_diff += m_diff * MINUTES_TO_SECONDS
            
            s_diff = self.s - other.s
            sec_diff += s_diff
            
            return sec_diff
        else:
            raise TypeError
            
            
