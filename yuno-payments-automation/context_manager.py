
import os
from dotenv import load_dotenv
from core.api_client import APIClient


class ContextManager:
  
    
    def __init__(self):
        """Initialize context manager with environment variables"""
        load_dotenv()
        self.config = {
            'api_url': os.getenv('API_URL', 'https://api.yuno.test'),
            'api_key': os.getenv('API_KEY', 'test_key'),
            'timeout': int(os.getenv('TIMEOUT', '30')),
            'verify_ssl': os.getenv('VERIFY_SSL', 'False').lower() == 'true'
        }
        self.api_client = APIClient(self.config)
    
    def get_api_url(self):
        """Get API base URL"""
        return self.config['api_url']
    
    def get_api_key(self):
        """Get API key"""
        return self.config['api_key']
    
    def get_timeout(self):
        """Get request timeout"""
        return self.config['timeout']
    
    def post(self, url, **kwargs):
        """Make POST request"""
        return self.api_client.post(url, **kwargs)
    
    def get(self, url, **kwargs):
        """Make GET request"""
        return self.api_client.get(url, **kwargs)
    
    def put(self, url, **kwargs):
        """Make PUT request"""
        return self.api_client.put(url, **kwargs)
    
    def delete(self, url, **kwargs):
        """Make DELETE request"""
        return self.api_client.delete(url, **kwargs)
    
    def close(self):
        """Close API client session"""
        self.api_client.close()
