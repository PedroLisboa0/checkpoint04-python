from datetime import date
from typing import Dict

INITIAL_STAGE = "Novo"

class Lead:
    def __init__(self, name: str, company: str, email: str, stage: str = None, created: str = None):
        self.name = name  
        self.company = company 
        self.email = email  

        # Define o estágio inicial se não for fornecido
        self.stage = stage if stage is not None else INITIAL_STAGE

        # Define a data de criação
        if created is None:
            self.created = date.today().strftime("%d/%m/%Y")
        else:
            self.created = created

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "company": self.company,
            "email": self.email,
            "stage": self.stage,
            "created": self.created,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Lead':
        return cls(
            name=data.get("name"),
            company=data.get("company"),
            email=data.get("email"),
            stage=data.get("stage", INITIAL_STAGE),
            created=data.get("created"),
        )
