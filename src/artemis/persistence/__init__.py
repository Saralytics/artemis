from enum import Enum
from artemis.persistence.file import FilePersistence
from artemis.persistence.s3 import S3Persistence


class PersistenceType(Enum):
    FILE = 'file', FilePersistence
    S3 = 's3', S3Persistence

    def __new__(cls, *args, **kwds):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    def __init__(
            self, _: str,
            persistence=None
    ):
        self._persistence = persistence

    @property
    def persistence(self):
        return self._persistence
