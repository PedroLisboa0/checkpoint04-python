from pathlib import Path
import json
from typing import List, Dict
from stages import Lead

class LeadRepo:
    def __init__(self, db_filename: str = "leads.json"):
        self.DATA_DIR = Path(__file__).resolve().parent
        self.DATA_DIR.mkdir(exist_ok=True)
        self.DB_PATH = self.DATA_DIR / db_filename 

    def _load_raw_data(self) -> List[Dict]:
        if not self.DB_PATH.exists():
            return []
        try:
            return json.loads(self.DB_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return []

    def _save(self, leads: List[Dict]):
        self.DB_PATH.write_text(
            json.dumps(leads, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )

    def load_leads(self) -> List[Lead]:
        raw_data = self._load_raw_data()
        # Converte cada dicionário em um objeto Lead
        return [Lead.from_dict(data) for data in raw_data]

    def create(self, lead: Lead):
        existing_leads = self.load_leads()
        existing_leads.append(lead)
        raw_data_to_save = [l.to_dict() for l in existing_leads]

        self._save(raw_data_to_save)