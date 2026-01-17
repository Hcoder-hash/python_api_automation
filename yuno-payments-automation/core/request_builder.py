"""
Request builder for constructing API payloads
"""
import json
from datetime import datetime, timedelta
import uuid


class RequestBuilder:
    """
    Builder class for constructing API request payloads
    """
    
    def __init__(self):
        """Initialize request builder"""
        self.base_payload = {}
    
    def build_purchase_request(self, amount, currency, card_number, cvv, expiry, **kwargs):
        """
        Build a payment purchase request payload
        
        Args:
            amount (int): Amount in smallest currency unit
            currency (str): Currency code (e.g., 'USD')
            card_number (str): Card number
            cvv (str): Card verification value
            expiry (str): Card expiry in MM/YY format
            **kwargs: Additional optional fields
            
        Returns:
            dict: Request payload
        """
        payload = {
            'transaction_id': str(uuid.uuid4()),
            'amount': amount,
            'currency': currency,
            'payment_method': {
                'card_number': card_number,
                'cvv': cvv,
                'expiry': expiry,
                'card_holder': kwargs.get('card_holder', 'TEST USER')
            },
            'merchant_id': kwargs.get('merchant_id', 'TEST_MERCHANT'),
            'description': kwargs.get('description', 'Test Payment'),
            'metadata': kwargs.get('metadata', {})
        }
        return payload
    
    def build_authorization_request(self, amount, currency, card_number, cvv, expiry, **kwargs):
        """
        Build a payment authorization request payload
        
        Args:
            amount (int): Amount in smallest currency unit
            currency (str): Currency code
            card_number (str): Card number
            cvv (str): Card verification value
            expiry (str): Card expiry in MM/YY format
            **kwargs: Additional optional fields
            
        Returns:
            dict: Request payload
        """
        payload = self.build_purchase_request(amount, currency, card_number, cvv, expiry, **kwargs)
        payload['operation_type'] = 'AUTHORIZATION'
        return payload
    
    def build_refund_request(self, transaction_id, amount=None, reason=None, **kwargs):
        """
        Build a refund request payload
        
        Args:
            transaction_id (str): Original transaction ID
            amount (int, optional): Refund amount (None for full refund)
            reason (str, optional): Refund reason
            **kwargs: Additional optional fields
            
        Returns:
            dict: Request payload
        """
        payload = {
            'refund_id': str(uuid.uuid4()),
            'transaction_id': transaction_id,
            'refund_type': 'PARTIAL' if amount else 'FULL',
            'reason': reason or 'Customer requested',
            'metadata': kwargs.get('metadata', {})
        }
        
        if amount:
            payload['amount'] = amount
        
        return payload
    
    def build_capture_request(self, transaction_id, amount=None, **kwargs):
        """
        Build a capture request payload
        
        Args:
            transaction_id (str): Authorization transaction ID
            amount (int, optional): Capture amount (None for full amount)
            **kwargs: Additional optional fields
            
        Returns:
            dict: Request payload
        """
        payload = {
            'transaction_id': transaction_id,
            'capture_type': 'PARTIAL' if amount else 'FULL',
            'metadata': kwargs.get('metadata', {})
        }
        
        if amount:
            payload['amount'] = amount
        
        return payload
    
    def build_cancellation_request(self, transaction_id, reason=None, **kwargs):
        """
        Build a cancellation request payload
        
        Args:
            transaction_id (str): Transaction ID to cancel
            reason (str, optional): Cancellation reason
            **kwargs: Additional optional fields
            
        Returns:
            dict: Request payload
        """
        payload = {
            'transaction_id': transaction_id,
            'reason': reason or 'Merchant cancellation',
            'metadata': kwargs.get('metadata', {})
        }
        return payload
    
    def build_customer_request(self, first_name, last_name, email, phone=None, **kwargs):
        """
        Build a customer creation request payload
        
        Args:
            first_name (str): Customer first name
            last_name (str): Customer last name
            email (str): Customer email
            phone (str, optional): Customer phone number
            **kwargs: Additional optional fields
            
        Returns:
            dict: Request payload
        """
        payload = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'phone': phone or '',
            'status': 'ACTIVE',
            'metadata': kwargs.get('metadata', {})
        }
        return payload
    
    def build_verification_request(self, transaction_id, **kwargs):
        """
        Build a payment verification request payload
        
        Args:
            transaction_id (str): Transaction ID to verify
            **kwargs: Additional optional fields
            
        Returns:
            dict: Request payload
        """
        payload = {
            'transaction_id': transaction_id,
            'metadata': kwargs.get('metadata', {})
        }
        return payload
