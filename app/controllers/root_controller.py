class RootController:
    @staticmethod
    def health_check():
        return {"success": "Server is available"}