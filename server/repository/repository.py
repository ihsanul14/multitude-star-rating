from framework.database import Database
from sqlalchemy.future import select
from sqlalchemy import func
from models import Rating

class Repository:
    db = Database()
    async def get_data(self):
        engine = self.db.postgres()
        session_maker = self.db.session_maker(engine)()
        result = {}
        async with session_maker as session:
            async with session.begin():
                result = await session.execute(select(func.avg(Rating.rating)))
                result = result.scalars().all()
                await session.close()
        return result

    async def add_data(self,data:Rating):        
        engine = self.db.postgres()
        session_maker = self.db.session_maker(engine)()
        async with session_maker as session:
            async with session.begin():
                session.add(Rating(rating=data.rating))
                await session.commit()
                await session.close()
        return data
