from abc import ABC, abstractmethod
from typing import List


class DriverHandlerInterface(ABC):
    @abstractmethod
    def stardard_derivation(self, numbers: List[float]) -> float:
        pass
