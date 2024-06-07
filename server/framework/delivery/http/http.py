from usecase import Usecase
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Depends, Body
from framework.error import Error
from framework.validator.validator import Validate
from models import Rating, CreateRatingRequest

router_group = "/api/ratings"

class HttpDelivery:
    usecase = Usecase
    error = Error()
    def __init__(self, app:FastAPI):
        self.app = app
        
    def init_usecase(self):
        self.usecase = Usecase()
        return self.usecase
        
    def delivery_http(self):
        @self.app.get(router_group)
        async def get_rating(usecase:Usecase = Depends(self.init_usecase)):
            try:
                response = await usecase.get_data()
                return JSONResponse(response, status_code=response['code'])
            except Exception as e:
                return self.error.error(e)
        @self.app.post(router_group)
        async def post(request: CreateRatingRequest,usecase:Usecase = Depends(self.init_usecase)):
            try:
                response = await self.usecase.add_data(request)
                return JSONResponse(response, status_code=response['code'])
            except Exception as e:
                return self.error.error(e)
