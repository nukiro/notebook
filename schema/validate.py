from dataclasses import dataclass
from enum import Enum
import json


class FieldType(Enum):
    STRING = "string"
    INTEGER = "integer"


class ValidationErrorType(Enum):
    INVALID_JSON = "invalid json"
    MISSING_FIELD = "field is required but missing"
    INVALID_TYPE = "field has invalid type"
    NULLABLE_FIELD = "field is not nullable but value is null"
    RULE_VIOLATION = "field violates validation rules"


@dataclass
class ValidationError:
    field_name: str
    error_type: ValidationErrorType
    message: str

    def __str__(self) -> str:
        return f"field='{self.field_name}', type='{self.error_type.value}', message='{self.message}')"


@dataclass
class FieldDefinition:
    field_type: str
    required: bool
    nullable: bool
    rules: list[dict]


@dataclass
class Schema:
    name: str
    fields: dict

    def add_field(self, name: str, definition: FieldDefinition):
        self.fields[name] = definition


def validate(schema: Schema, payload: str) -> list[ValidationError]:
    """
    Validates the given JSON payload against the provided schema.

    Args:
        schema (Schema): The schema to validate against.
        payload (str): The JSON payload as a string.

    Returns:
        list[ValidationError]: A list of validation errors. If the list is empty, the payload is valid.
    """
    # Parse the JSON payload
    try:
        data = json.loads(payload)
    except json.JSONDecodeError as e:
        return [
            ValidationError(
                field_name="payload",
                error_type=ValidationErrorType.INVALID_JSON,
                message=f"Invalid JSON: {str(e)}",
            )
        ]

    # There are four main validation steps:
    # 1. Check for required fields
    # 2. Check for nullability
    # 3. Validate field types
    # 4. Validate against rules

    errors: list[ValidationError] = []

    # Validate each schema field against the payload
    for field_name, field_def in schema.fields.items():
        # Check for required fields
        if field_def.required and field_name not in data:
            errors.append(
                ValidationError(
                    field_name=field_name,
                    error_type=ValidationErrorType.MISSING_FIELD,
                    message=f"'{field_name}' is required but missing",
                )
            )
            continue

        # Check for nullability
        if (
            field_def.nullable is False
            and field_name in data
            and data[field_name] is None
        ):
            errors.append(
                ValidationError(
                    field_name=field_name,
                    error_type=ValidationErrorType.NULLABLE_FIELD,
                    message=f"'{field_name}' is not nullable but value is null",
                )
            )
            continue

    return errors
