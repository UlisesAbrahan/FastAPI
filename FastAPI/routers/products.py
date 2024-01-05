from fastapi import APIRouter

router = APIRouter 


@router.get("/products/")
async def products():
    return ["producto1","producto2","producto3","producto4"]