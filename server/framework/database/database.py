from decouple import config
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker



class Database:
    def postgres(self):
        engine = create_async_engine(config('PG_URI'))
        return engine
    
    def session_maker(self, engine)->sessionmaker:
        return sessionmaker(
            bind=engine,
            class_=AsyncSession
        )
        
