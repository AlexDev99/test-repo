from fastapi import APIRouter, UploadFile, File

from ..endpoint.parser import parser

router = APIRouter()


@router.get('/')
def get_oper():
    return 'Work!'


@router.post('/upload')
async def uploadFile(file: UploadFile = File(...)):
    parser(file.file.read())


@router.get('/list')
def get():
    return data()
