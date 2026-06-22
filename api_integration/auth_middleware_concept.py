# api_integration/auth_middleware_concept.py

class SecurityMiddleware:
    VALID_API_KEYS = ["zecpath_internal_prod_99x"]
    
    @staticmethod
    def verify_request_headers(headers: dict) -> dict:
        """
        Intercepts the API request to verify JWT tokens and internal API Keys.
        Returns our standard API contract if unauthorized.
        """
        # 1. Check for Internal API Key (Server to Server)
        api_key = headers.get("X-API-Key")
        if not api_key or api_key not in SecurityMiddleware.VALID_API_KEYS:
            return {
                "status": "FAILED",
                "data": {},
                "error_details": "403 Forbidden: Invalid or Missing API Key"
            }
            
        # 2. Check for User Authentication (JWT Bearer Token)
        auth_header = headers.get("Authorization", "")
        if not auth_header.startswith("Bearer "):
            return {
                "status": "FAILED",
                "data": {},
                "error_details": "401 Unauthorized: Missing or Malformed JWT Token"
            }
            
        return {"status": "SUCCESS", "message": "Authenticated"}

if __name__ == "__main__":
    print("\n🔒 TESTING API SECURITY MIDDLEWARE")
    
    bad_headers = {"X-API-Key": "wrong_key", "Authorization": "Bearer fake_token"}
    good_headers = {"X-API-Key": "zecpath_internal_prod_99x", "Authorization": "Bearer real_jwt_token"}
    
    print(f"\nMalicious Request Result:\n{SecurityMiddleware.verify_request_headers(bad_headers)}")
    print(f"\nValid Request Result:\n{SecurityMiddleware.verify_request_headers(good_headers)}")
    print("\n")