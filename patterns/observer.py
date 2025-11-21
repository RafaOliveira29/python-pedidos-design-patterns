from abc import ABC, abstractmethod


class OrderObserver(ABC):
    @abstractmethod
    def update(self, message: str) -> None:
        pass


class EmailObserver(OrderObserver):
    def update(self, message: str) -> None:
        print(f"[Email] {message}")


class LogObserver(OrderObserver):
    def update(self, message: str) -> None:
        print(f"[Log] {message}")
