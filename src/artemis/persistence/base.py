"""This module defines the base interface that all persistence classes must implement in order to be non-abstract."""
from abc import abstractmethod, ABC
from dataclasses import dataclass
import re


class BasePersistence(ABC):
    """This class defines an abstract base interface of a persistence class, which is used to store and load
    objects.
    """

    @abstractmethod
    def write_binary(self, path, value):
        """This is a method interface for writing a binary file."""
        raise NotImplementedError

    @abstractmethod
    def read_binary(self, path):
        """This is a method interface for reading a binary file."""
        raise NotImplementedError

    @abstractmethod
    def get_exists_status(self, path):
        """This is a method interface for determining if a file exists."""
        raise NotImplementedError

    @abstractmethod
    def get_presigned_url(self, path):
        """This is a method interface for retrieving a pre-signed URL for a file stored in the cloud."""
        raise NotImplementedError
