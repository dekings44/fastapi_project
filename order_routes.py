from fastapi import APIRouter

order_router = APIRouter(
    prefix = '/orders',
    tags = ['Order']
)


@order_router.get('/')
async def hello():
    return {'message': 'Welcome to orders'}