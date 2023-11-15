from typing import List
from artemis.repo import ApplicationDatabase
from artemis.domain import SomedomainSchema
from collections import defaultdict


class SomedomainRepository:

    def __init__(self):
        self.application_database = ApplicationDatabase()

