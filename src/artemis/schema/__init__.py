from marshmallow import Schema, fields, post_load, pre_dump, EXCLUDE, post_dump, ValidationError
from artemis.util import get_logger

logger = get_logger(__file__)
