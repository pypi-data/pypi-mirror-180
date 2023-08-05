from abc import ABCMeta
from abc import abstractmethod
from typing import Any

from .storage_item import StorageItem
from .operation_result import OperationResult


class StorageORM(metaclass=ABCMeta):
    _db_instance: Any

    @abstractmethod
    def __init__(
        self,
        client: Any = None,
        host: str = None,
        port: int = 6379,
        db: int = 0,
    ) -> None:
        raise NotImplementedError

    @abstractmethod
    async def save(self, item: StorageItem) -> OperationResult:
        raise NotImplementedError

    @abstractmethod
    async def bulk_create(self, items: list[StorageItem]) -> OperationResult:
        raise NotImplementedError

    @abstractmethod
    async def bulk_delete(self, items: list[StorageItem]) -> OperationResult:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, item: StorageItem) -> OperationResult:
        raise NotImplementedError
