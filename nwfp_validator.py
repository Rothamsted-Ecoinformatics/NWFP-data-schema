import json
from jsonschema import validate,  Draft7Validator, RefResolver
from jsonschema.exceptions import ValidationError

def load_json_file(file_path):
    """ Load a JSON file and return its contents. """
    with open(file_path, 'r') as file:
        return json.load(file)

def validate_json(json_data, json_schema):
    """ Validate a JSON data against a JSON schema. """
    try:
        resolver = RefResolver(base_uri='http://geojson.org/schema/', 
            referrer=json_schema, 
            store={
                'http://geojson.org/schema/MultiPolygon.json': load_json_file('geojson/MultiPolygon.json'),
                'http://geojson.org/schema/Polygon.json': load_json_file('geojson/Polygon.json'),
                'http://geojson.org/schema/Point.json': load_json_file('geojson/Point.json'),
                'https://nwfp.rothamsted.ac.uk/schema/NwfpFarmlet.json': load_json_file('schema/NwfpFarmlet.json'),
                'https://nwfp.rothamsted.ac.uk/schema/NwfpCatchment.json': load_json_file('schema/NwfpCatchment.json'),
                'https://nwfp.rothamsted.ac.uk/schema/NwfpField.json': load_json_file('schema/NwfpField.json'),
                'https://nwfp.rothamsted.ac.uk/schema/NwfpManagementEvent.json': load_json_file('schema/NwfpManagementEvent.json'),
                'https://nwfp.rothamsted.ac.uk/schema/NwfpInstrument.json': load_json_file('schema/NwfpInstrument.json'),
                'https://nwfp.rothamsted.ac.uk/schema/NwfpMeasurement.json': load_json_file('schema/NwfpMeasurement.json')
            }
        )
        validator = Draft7Validator(json_schema,resolver=resolver)
        validator.validate(json_data)
        print("JSON data is valid.")
    except ValidationError as ve:
        print("JSON data is invalid.")
        print("Validation error message:", ve.message)

def main():
    # Load the JSON schema
    schema_file = 'schema/NwfpCatchment.json'
    json_schema = load_json_file(schema_file)

    # Load the JSON file to be validated
    json_file = 'examples/measurements_example.json'  # replace this with your actual JSON file
    json_data = load_json_file(json_file)

    # Validate JSON data against the schema
    validate_json(json_data, json_schema)

if __name__ == "__main__":
    main()