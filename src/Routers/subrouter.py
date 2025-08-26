from fastapi import APIRouter
from src.api.add import add
router=APIRouter(tags=[" "])


@router.get("/sub/")
def subtraction(a:int,b:int):
    """

    :param a: input filed which is integer
    :param b:
    :return:
    """

    c=a+b

    return c