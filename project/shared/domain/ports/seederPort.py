from project.shared.config.database import SessionFactory
from abc import abstractmethod


class SeederPort:
    
    session = SessionFactory
    
    @abstractmethod
    def handle(self):
        pass
