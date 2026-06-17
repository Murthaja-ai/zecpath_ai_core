# stabilization_core/api_formatter.py

class APIFormatter:
    @staticmethod
    def build_response(success: bool, data: dict = None, error_message: str = None) -> dict:
        """
        The unbreakable contract between the Backend AI and the Frontend Web App.
        """
        return {
            "status": "SUCCESS" if success else "FAILED",
            "data": data if success else {},
            "error_details": error_message if not success else None
        }