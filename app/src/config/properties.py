from jproperties import Properties

class properties():

    def __init__(self):
        self.config = Properties()
        with open('D:/Archivos de la U/Mis archivos/Semestre XI/Inteligencia de negocios/Proyecto/auctions_api/app/resources/app-config.properties', 'rb') as config_file:
            self.config.load(config_file)

    def get_property(self, key):
        return self.config.get(key).data