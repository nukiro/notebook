use serde::Deserialize;
use serde_json::Value;

#[derive(Deserialize, Debug)]
#[serde(rename_all = "lowercase")]
enum FieldType {
    String,
    Integer,
    // Add more types as needed
}

#[derive(Deserialize, Debug)]
struct FieldDefinition {
    field_type: FieldType,
    required: bool,
    nullable: bool,
    // rules: Vec<ValidationRule>,
}

#[derive(Deserialize, Debug)]
struct Schema {
    name: String,
    fields: std::collections::HashMap<String, FieldDefinition>,
}

fn validate(schema: &Schema, payload: &Value) -> bool {
    println!("Validating payload against schema: {}", schema.name);
    println!("{}", payload["name"]);
    return true;
}

fn main() {
    let payload = r#"
    {
        "name": "Carlos",
        "age": 30
    }
    "#;

    let payload = serde_json::from_str::<Value>(payload).expect("Failed to parse payload");

    let schema = r#"
    {
        "name": "user",
        "fields": {
            "name": {
                "field_type": "string",
                "required": true,
                "nullable": false,
                "rules": [{"min_length": 3}, {"max_length": 50}]
            },
            "age": {
                "field_type": "integer",
                "required": false,
                "nullable": true,
                "rules": [{"min_value": 0}]
            }
        }
    }
    "#;

    println!("Payload: {}", schema);

    let schema = serde_json::from_str::<Schema>(schema).expect("Failed to parse schema as JSON");

    let is_valid = validate(&schema, &payload);
    println!("Is payload valid? {}", is_valid);
}
