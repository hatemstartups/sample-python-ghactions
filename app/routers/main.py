from fastapi import APIRouter
from starlette.responses import PlainTextResponse

router = APIRouter()


@router.get("/", include_in_schema=False)
def home():
    """Main endpoint."""
    return PlainTextResponse('type anything after the /')


@router.get("/{echo}", include_in_schema=False)
def getword(echo: str):
    """Optional name endpoint."""
    return PlainTextResponse(f'you typed  {echo}')
