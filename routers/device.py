from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models import models
from app.schemas.device_schemas import DeviceDetails
from app.security import oauth2
from app.utils import depends_utils

router = APIRouter(
    prefix="/device",
    tags=["Device"]
)


@router.get("/")
def get_devices(db: Session = Depends(get_db),
                current_user: models.Device = Depends(oauth2.get_current_user)):
    user_devices = [device.id for device in current_user.devices]
    devices = db.query(models.Device).filter(models.Device.id.in_(user_devices)).all()
    return devices


@router.get("/{device_id}")
def get_device_details(device_id: int,
                       device: models.Device = Depends(depends_utils.get_device)) \
        -> DeviceDetails:
    return device


@router.get("/{device_id}/tube")
def get_device_tubes(device_id: int,
                     db: Session = Depends(get_db),
                     device: models.Device = Depends(depends_utils.get_device)):
    tubes = db.query(models.Tube).filter(models.Tube.device_id == device_id).all()
    return tubes
