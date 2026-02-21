from dataclasses import dataclass
import json

from validate import FieldDefinition, Schema, ValidationError, validate


@dataclass
class Result:
    payload: dict
    errors: list[ValidationError]


user = Schema(name="User", fields={})
user.add_field(
    name="name",
    definition=FieldDefinition(
        field_type="string",
        required=True,
        nullable=False,
        rules=[{"min_length": 3}, {"max_length": 50}],
    ),
)
user.add_field(
    name="age",
    definition=FieldDefinition(
        field_type="integer", required=False, nullable=True, rules=[{"min_value": 0}]
    ),
)

if __name__ == "__main__":
    data = [
        {
            "name": "John Doe",
        },
        {},
    ]

    # Run validation
    validations: list[Result] = []

    for item in data:
        payload: str = json.dumps(item, indent=2)

        errors = validate(schema=user, payload=payload)
        validations.append(Result(payload=item, errors=errors))

    for result in validations:
        print("-" * 40)
        print("Payload")
        print(json.dumps(result.payload, indent=2))
        print()
        if result.errors:
            print("Validation: Failed")
            for error in result.errors:
                print(f"\t{error}")
        else:
            print("Validation: Successful!")
