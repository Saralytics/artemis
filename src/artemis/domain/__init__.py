from marshmallow import (
    fields,
    EXCLUDE,
    post_load,
    post_dump,
    Schema,
    pre_dump,
    pre_load,
    INCLUDE,
    validates_schema,
    ValidationError,
    validates
)
from artemis.util import get_logger

logger = get_logger(__file__)


class SomedomainSchema(Schema):
    something = fields.String(required=True)

    class Meta:
        unknown = EXCLUDE
