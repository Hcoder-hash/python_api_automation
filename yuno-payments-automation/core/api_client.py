"""
API Client for making HTTP requests to the Yuno Payments API
"""
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class APIClient:
    """
    HTTP client for API requests with retry logic and session management
    """
    
    def __init__(self, config):
        """
        Initialize API client with configuration
        
        Args:
            config (dict): Configuration dictionary with api_url, api_key, etc.
        """
        self.config = config
        self.api_url = config.get('api_url')
        self.api_key = config.get('api_key')
        self.timeout = config.get('timeout', 30)
        self.verify_ssl = config.get('verify_ssl', True)
        self.session = self._create_session()
    
    def _create_session(self):
        """Create requests session with retry strategy"""
        session = requests.Session()
        
        # Configure retry strategy
        retry_strategy = Retry(
            total=3,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET", "POST", "PUT", "DELETE"],
            backoff_factor=1
        )
        
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        
        # Set default headers
        session.headers.update({
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
        
        return session
    
    def get(self, url, **kwargs):
        """
        Make GET request
        
        Args:
            url (str): Request URL
            **kwargs: Additional arguments for requests.get
            
        Returns:
            Response object
        """
        return self.session.get(
            url,
            timeout=self.timeout,
            verify=self.verify_ssl,
            **kwargs
        )
    
    def post(self, url, **kwargs):
        """
        Make POST request
        
        Args:
            url (str): Request URL
            **kwargs: Additional arguments for requests.post
            
        Returns:
            Response object
        """
        return self.session.post(
            url,
            timeout=self.timeout,
            verify=self.verify_ssl,
            **kwargs
        )
    
    def put(self, url, **kwargs):
        """
        Make PUT request
        
        Args:
            url (str): Request URL
            **kwargs: Additional arguments for requests.put
            
        Returns:
            Response object
        """
        return self.session.put(
            url,
            timeout=self.timeout,
            verify=self.verify_ssl,
            **kwargs
        )
    
    def delete(self, url, **kwargs):
        """
        Make DELETE request
        
        Args:
            url (str): Request URL
            **kwargs: Additional arguments for requests.delete
            
        Returns:
            Response object
        """
        return self.session.delete(
            url,
            timeout=self.timeout,
            verify=self.verify_ssl,
            **kwargs
        )
    
    def patch(self, url, **kwargs):
        """
        Make PATCH request
        
        Args:
            url (str): Request URL
            **kwargs: Additional arguments for requests.patch
            
        Returns:
            Response object
        """
        return self.session.patch(
            url,
            timeout=self.timeout,
            verify=self.verify_ssl,
            **kwargs
        )
    
    def close(self):
        """Close the session"""
        self.session.close()
