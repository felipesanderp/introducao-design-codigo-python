from abc import ABC, abstractmethod
from typing import List


class DriverHandlerInterface(ABC):
    @abstractmethod
    def stardard_derivation(self, numbers: List[float]) -> float:
        pass

    @abstractmethod
    def variance(self, numbers: List[float]) -> float:
        pass

    def mean(self, numbers: List[float]) -> float:
        pass
