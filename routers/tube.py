from fastapi import Depends, APIRouter

from app.models import models
from app.utils import depends_utils

router = APIRouter(
    prefix="/tube",
    tags=["Tube"]
)


@router.get("/{tube_id}")
def get_tubes(tube_id: int,
              tube: models.Tube = Depends(depends_utils.get_tube)):
    return tube
