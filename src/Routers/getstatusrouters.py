#import logging,APIRouter,GetStatus
import logging
from fastapi import APIRouter
from src.api.getstatus import GetStatus

# setting logging level(INFO)
logging.basicConfig(level=logging.INFO)



# creating instance router
router=APIRouter()

@router.get("/getstatus/")
def get_status(doc_id:int):
    logging.info("gettingstatus")
    # getting Status from get_doc_status method
    status=GetStatus().get_doc_status(doc_id)

    logging.info("status retrived sucefully")

    #getting status
    return status



