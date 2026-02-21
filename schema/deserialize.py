from enum import Enum
import json
from typing import Any

# Schema retrieve from the API
response = json.dumps(
    {
        "name": "User",
        "fields": {
            "name": {
                "field_type": "string",
                "required": True,
                "nullable": False,
                "rules": [{"min_length": 3}, {"max_length": 50}],
            },
            "age": {
                "field_type": "integer",
                "required": False,
                "nullable": True,
                "rules": [{"min_value": 0}],
            },
        },
    }
)


# From the API response, which contains the schema definition,
# we need to deserialize it into our Schema and FieldDefinition classes.
class FieldType(Enum):
    STRING = "string"
    INTEGER = "integer"


class ValidationRuleType(Enum):
    MIN_LENGTH = "min_length"
    MAX_LENGTH = "max_length"
    MIN_VALUE = "min_value"
    MAX_VALUE = "max_value"


class ValidationRule:
    def __init__(self, rule_type: ValidationRuleType, value: Any):
        self.rule_type = ValidationRuleType(rule_type)
        self.value = value

    @classmethod
    def from_dashboard(cls, rule: dict) -> "ValidationRule":
        rule_type, value = next(iter(rule.items()))
        return cls(rule_type=rule_type, value=value)


class FieldDefinition:
    def __init__(
        self,
        field_type: FieldType,
        required: bool,
        nullable: bool,
        rules: list[ValidationRule] | None = None,
    ):
        self.field_type = field_type
        self.required = required
        self.nullable = nullable
        self.rules = rules or []

    @classmethod
    def from_dashboard(cls, field_def: dict) -> "FieldDefinition":
        field_type = FieldType(field_def["field_type"])
        required = field_def["required"]
        nullable = field_def["nullable"]
        rules = [
            ValidationRule.from_dashboard(rule) for rule in field_def.get("rules", [])
        ]
        return cls(
            field_type=field_type, required=required, nullable=nullable, rules=rules
        )


class Schema:
    def __init__(self, name: str, fields: dict[str, "FieldDefinition"]):
        self.name = name
        self.fields = fields

    @classmethod
    def from_dashboard(cls, response: str) -> "Schema":
        # Load data from dashboard response
        data = json.loads(response)

        fields = {}
        for field_name, field_def in data["fields"].items():
            fields[field_name] = FieldDefinition.from_dashboard(field_def)

        return cls(name=data["name"], fields=fields)


user_schema = Schema.from_dashboard(response)
print(user_schema.__dict__)
for field in user_schema.fields.values():
    print(field.__dict__)
    for rule in field.rules:
        print(rule.__dict__)
