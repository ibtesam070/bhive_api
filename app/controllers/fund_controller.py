from dotenv import load_dotenv
import os
import http.client
from ..constants.values import RAPID_API_HOST
import json

load_dotenv()


class FundController:
    @staticmethod
    def get_schemes(fund_family: str):
        conn = http.client.HTTPSConnection(RAPID_API_HOST)
        headers = {
            "x-rapidapi-key": os.getenv("RAPID_API_KEY"),
            "x-rapidapi-host": RAPID_API_HOST,
        }

        try:
            conn.request(
                "GET",
                f"/latest?Mutual_Fund_Family={fund_family.replace(' ', '%20')}&Scheme_Type=Open",
                headers=headers,
            )
            res = conn.getresponse()
            data = res.read()
            response_data = data.decode("utf-8")
            json_data = json.loads(response_data)
        except Exception:
            return {"success": False, "data": "Failed to fetch data from the server"}
        
        return {"success": True, "data": json_data}
