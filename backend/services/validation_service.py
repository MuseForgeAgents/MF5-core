from jsonschema import validate, ValidationError

def validate_against_schema(schema: dict, input_data: dict):
    try:
        validate(instance=input_data, schema=schema)
        return {"valid": True}
    except ValidationError as e:
        return {"valid": False, "error": str(e)}
