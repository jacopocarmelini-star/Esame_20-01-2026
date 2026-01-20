from dataclasses import dataclass

@dataclass
class Connessioni:
    a1_id : int
    a2_id : int
    peso : int

    def __str__(self):
        return f"{self.a1_id}, {self.a2_id}"

