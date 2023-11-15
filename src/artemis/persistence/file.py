import os

from artemis.persistence.base import BasePersistence


class FilePersistence(BasePersistence):

    def __init__(self, base_path=None):
        self.base_path = base_path or '.'

    def write_binary(self, path, value):
        key_path = os.path.join(self.base_path, path)
        dir_path, _ = os.path.split(key_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(key_path, 'wb') as write_file:
            write_file.write(value)
        return True

    def read_binary(self, path):
        key_path = os.path.join(self.base_path, path)
        try:
            with open(key_path, 'rb') as read_file:
                contents = read_file.read()
            return contents
        except FileNotFoundError:
            return None

    def get_exists_status(self, path):
        key_path = os.path.join(self.base_path, path)
        return os.path.isfile(key_path)

    def get_presigned_url(self, path):
        return None
