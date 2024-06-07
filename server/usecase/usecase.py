from .response import resp
from repository import Repository
from decimal import Decimal
from models.models import CreateRatingRequest

class Usecase:
    repository = Repository()
    async def get_data(self):
        result = {} 
        result['code'] = 200
        result['message'] = "success retrieve data"
        projects = await self.repository.get_data()
        result['data'] = {
            "rating": str(projects[0].quantize(Decimal('0.01')))
        } 
        return result


    async def add_data(self,data:CreateRatingRequest):
        result = {}
        await self.repository.add_data(data)
        result['code'] = 200
        result['message'] = "success insert data"
        result = resp(result)
        return result