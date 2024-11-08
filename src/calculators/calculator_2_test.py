from typing import Dict, List
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from .calculator_2 import Calculator2


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


class MockDriverHandler(DriverHandlerInterface):
    def stardard_derivation(self, number: List[float]) -> float:
        return 3

    def variance(self, number: List[float]) -> float:
        return 3


# Integração entre NumpyHandler e Calculator2
def test_calculate_integration():
    mock_request = MockRequest(body={"numbers": [2.12, 4.62, 1.32]})

    driver = NumpyHandler()
    calculator2 = Calculator2(driver)
    formated_response = calculator2.calculate(mock_request)

    assert isinstance(formated_response, dict)
    assert formated_response == {"data": {"Calculator": 2, "result": 0.08}}


def test_calculate():
    mock_request = MockRequest(body={"numbers": [2.12, 4.62, 1.32]})

    driver = MockDriverHandler()
    calculator2 = Calculator2(driver)
    formated_response = calculator2.calculate(mock_request)

    assert isinstance(formated_response, dict)
    assert formated_response == {"data": {"Calculator": 2, "result": 0.33}}
