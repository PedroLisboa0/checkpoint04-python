from datetime import date
from typing import Dict

# Definição do estágio inicial para novos leads
INITIAL_STAGE = "Novo"

class Lead:
    def __init__(self, name: str, company: str, email: str, stage: str = None, created: str = None):
        self.name = name  
        self.company = company 
        self.email = email  

        self.stage = stage if stage is not None else self._default_stage

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
            stage=data.get("stage", cls._default_stage),
            created=data.get("created"),
        )