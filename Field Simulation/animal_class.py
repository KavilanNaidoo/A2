class animal:
    """ A generic Animal"""

    def __init__(self,growth_rate,food_need,water_need):
        self._weight = 0
        self._days_growing = 0
        self._growth_rate = 0
        self._food_need = 0
        self._water_need = 0
        self._status = "Young"
        self._type = "Generic"

    def needs(self):
        return {'food need':self._food_need,'water need':self._water_need}

    def report(self):
        return{'type':self._type,'status':self._status,'growth':self._growth_rate,'days growing':self._days_growing}

    
    def _update_status(self):
        if self._growth > 15:
            self._status = 'Old'
        elif self._growth > 10:
            self._status = 'Mature'
        elif self._growth > 5:
            self._status = 'Adult'
        elif self._growth > 3:
            self._status = 'Young'
        elif self._growth > 0:
            self._status = 'Baby'

    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            self._growth += self._growth_rate
        self._days_growing += 1
        self._update_status()





















    
        
