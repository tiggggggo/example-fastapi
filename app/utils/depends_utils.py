from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models import models
from app.security import oauth2


def get_tube(tube_id: int,
             db: Session = Depends(get_db),
             current_user: models.Device = Depends(oauth2.get_current_user)):
    tube = db.query(models.Tube).filter(models.Tube.id == tube_id).first()
    if tube is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Tube with id={tube_id} not found")
    user_devices = [device.id for device in current_user.devices]
    if tube.device.id not in user_devices:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")
    return tube


def get_device(device_id: int,
               db: Session = Depends(get_db),
               current_user: models.Device = Depends(oauth2.get_current_user)):
    user_devices = [device.id for device in current_user.devices]
    if device_id not in user_devices:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")
    device = db.query(models.Device) \
        .filter(models.Device.id == device_id) \
        .first()
    return device
