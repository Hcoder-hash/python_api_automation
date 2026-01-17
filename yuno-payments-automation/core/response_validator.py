"""
Response validator for API responses
"""
import json
from jsonschema import validate, ValidationError


class ResponseValidator:
    """
    Validator class for API response validation against schemas
    """
    
    def __init__(self, schema_path=None):
        """
        Initialize response validator
        
        Args:
            schema_path (str, optional): Path to JSON schema file
        """
        self.schema_path = schema_path
        self.schema = None
        if schema_path:
            self.load_schema(schema_path)
    
    def load_schema(self, schema_path):
        """
        Load JSON schema from file
        
        Args:
            schema_path (str): Path to schema file
            
        Raises:
            FileNotFoundError: If schema file not found
            json.JSONDecodeError: If schema is invalid JSON
        """
        try:
            with open(schema_path, 'r') as f:
                self.schema = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Schema file not found: {schema_path}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in schema: {str(e)}", "", 0)
    
    def validate_response(self, response_data):
        """
        Validate response against schema
        
        Args:
            response_data (dict): Response data to validate
            
        Returns:
            bool: True if valid
            
        Raises:
            ValidationError: If validation fails
        """
        if not self.schema:
            raise ValueError("Schema not loaded")
        
        try:
            validate(instance=response_data, schema=self.schema)
            return True
        except ValidationError as e:
            raise ValidationError(f"Response validation failed: {str(e)}")
    
    def validate_status_code(self, response, expected_status):
        """
        Validate HTTP status code
        
        Args:
            response: Response object
            expected_status (int): Expected status code
            
        Returns:
            bool: True if status matches
        """
        return response.status_code == expected_status
    
    def validate_required_fields(self, response_data, required_fields):
        """
        Validate that response contains required fields
        
        Args:
            response_data (dict): Response data
            required_fields (list): List of required field names
            
        Returns:
            bool: True if all fields present
            
        Raises:
            ValueError: If required fields missing
        """
        missing_fields = [field for field in required_fields if field not in response_data]
        
        if missing_fields:
            raise ValueError(f"Missing required fields: {missing_fields}")
        
        return True
    
    def validate_field_type(self, response_data, field_name, expected_type):
        """
        Validate field type in response
        
        Args:
            response_data (dict): Response data
            field_name (str): Field name to validate
            expected_type (type): Expected type
            
        Returns:
            bool: True if type matches
            
        Raises:
            ValueError: If type doesn't match
        """
        if field_name not in response_data:
            raise ValueError(f"Field '{field_name}' not found in response")
        
        if not isinstance(response_data[field_name], expected_type):
            raise ValueError(
                f"Field '{field_name}' has type {type(response_data[field_name])}, "
                f"expected {expected_type}"
            )
        
        return True
    
    def validate_field_value(self, response_data, field_name, expected_value):
        """
        Validate field value in response
        
        Args:
            response_data (dict): Response data
            field_name (str): Field name to validate
            expected_value: Expected value
            
        Returns:
            bool: True if value matches
            
        Raises:
            ValueError: If value doesn't match
        """
        if field_name not in response_data:
            raise ValueError(f"Field '{field_name}' not found in response")
        
        if response_data[field_name] != expected_value:
            raise ValueError(
                f"Field '{field_name}' has value {response_data[field_name]}, "
                f"expected {expected_value}"
            )
        
        return True
    
    def validate_response_contains(self, response_data, *fields):
        """
        Validate response contains multiple fields
        
        Args:
            response_data (dict): Response data
            *fields: Field names to check
            
        Returns:
            bool: True if all fields present
            
        Raises:
            ValueError: If any field missing
        """
        return self.validate_required_fields(response_data, list(fields))
