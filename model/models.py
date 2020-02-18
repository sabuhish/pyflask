from utils.dbsetup import Model,Integer,Text,Column,String




class Contact(Model):
    __tablename__ = "contact"
    
    identity = Column(String(length=10),default=None)
    name = Column(String(),default=None)
    surname = Column(String(),default=None)

