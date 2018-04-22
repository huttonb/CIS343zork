class Weapon(object):
    def __init__(self):
            self.wName = 'generic'
            self.aMod = 1.0
            self.uses = 1
            self.ammo = self.uses
    def getAmmo(self):
        return self.ammo
    def useWeapon(self):
        return self.ammo-1
