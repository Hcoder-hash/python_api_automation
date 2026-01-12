import os
from dotenv import load_dotenv
from robot.libraries.BuiltIn import BuiltIn

class DotEnv:
    """Robot Framework library for loading .env environment variables"""
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    
    def __init__(self):
        env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
        load_dotenv(env_path)
        
        builtin = BuiltIn()
        builtin.set_suite_variable('${PUBLIC_API_KEY}', os.getenv('PUBLIC_API_KEY'))
        builtin.set_suite_variable('${PRIVATE_SECRET_KEY}', os.getenv('PRIVATE_SECRET_KEY'))
        builtin.set_suite_variable('${BASE_URL}', os.getenv('BASE_URL'))
