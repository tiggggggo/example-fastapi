from fastapi import Depends, APIRouter, HTTPException, Query
from sqlalchemy.orm import Session
from starlette import status

from app.database.database import get_db
from app.models import models
from app.utils import date_utils, depends_utils

router = APIRouter(
    prefix="/data",
    tags=["Data"]
)


@router.get("/hour", description='Return hour (for specific tubes 15 min) data')
def get_hour_data(tube_id: int = Query(description='Description Tube id', example=235),
                  start_date: str = Query(description='Start date in format "%Y-%m-%d"', example='2023-04-23'),
                  end_date: str = Query(description='End date in format "%Y-%m-%d"', example='2023-04-24'),
                  tube: models.Tube = Depends(depends_utils.get_tube),
                  db: Session = Depends(get_db)):
    contract_hour = get_tube_contract_hour(db, tube_id)

    start_date = date_utils.get_datetime(start_date, contract_hour=contract_hour)
    end_date = date_utils.get_datetime(end_date, contract_hour=contract_hour)

    hour_data = db.query(models.HourData) \
        .filter(models.HourData.date > start_date,
                models.HourData.date <= end_date,
                models.HourData.tube_id == tube_id) \
        .order_by(models.HourData.date.asc()) \
        .all()
    return hour_data


@router.get("/day", description='Return daily data for period')
def get_day_data(tube_id: int = Query(description='Tube id', example=235),
                 start_date: str = Query(description='Start date in format "%Y-%m-%d"', example='2023-04-01'),
                 end_date: str = Query(description='End date in format "%Y-%m-%d"', example='2023-05-01'),
                 tube: models.Tube = Depends(depends_utils.get_tube),
                 db: Session = Depends(get_db)):
    contract_hour = get_tube_contract_hour(db, tube_id)

    start_date = date_utils.get_datetime(start_date, contract_hour=contract_hour)
    end_date = date_utils.get_datetime(end_date, contract_hour=contract_hour)

    day_data = db.query(models.DayData) \
        .filter(models.DayData.date > start_date,
                models.DayData.date <= end_date,
                models.DayData.tube_id == tube_id) \
        .order_by(models.DayData.date.asc()) \
        .all()
    return day_data


@router.get("/month", description='Return month data for period')
def get_month_data(tube_id: int = Query(description='Tube id', example=235),
                   start_date: str = Query(description='Start date in format "%Y-%m"', example='2023-04'),
                   end_date: str = Query(description='End date in format "%Y-%m"', example='2023-05'),
                   tube: models.Tube = Depends(depends_utils.get_tube),
                   db: Session = Depends(get_db)):
    start_date = date_utils.get_datetime(start_date, date_format=date_utils.QUERY_MONTH_FORMAT)
    end_date = date_utils.get_datetime(end_date, date_format=date_utils.QUERY_MONTH_FORMAT)
    month_data = db.query(models.MonthData) \
        .filter(models.MonthData.date > start_date,
                models.MonthData.date <= end_date,
                models.MonthData.tube_id == tube_id) \
        .order_by(models.MonthData.date.asc()) \
        .all()
    return month_data


@router.get("/alarm")
def get_alarm_data(device_id: int = Query(description='Device id', example=223),
                   start_date: str = Query(description='Start date in format "%Y-%m-%d"', example='2023-01-13'),
                   end_date: str = Query(description='End date in format "%Y-%m-%d"', example='2023-05-25'),
                   device: models.Device = Depends(depends_utils.get_device),
                   db: Session = Depends(get_db)):
    start_date = date_utils.get_datetime(start_date)
    end_date = date_utils.get_datetime(end_date)
    alarm_data = db.query(models.AlarmData) \
        .filter(models.AlarmData.date >= start_date,
                models.AlarmData.date < end_date,
                models.AlarmData.device_id == device_id) \
        .order_by(models.AlarmData.date.asc()) \
        .all()
    return alarm_data


@router.get("/event")
def get_event_data(device_id: int,
                   start_date: str,
                   end_date: str,
                   device: models.Device = Depends(depends_utils.get_device),
                   db: Session = Depends(get_db)):
    start_date = date_utils.get_datetime(start_date)
    end_date = date_utils.get_datetime(end_date)
    event_data = db.query(models.EventData) \
        .filter(models.EventData.date >= start_date,
                models.EventData.date < end_date,
                models.EventData.device_id == device_id) \
        .order_by(models.EventData.date.asc()) \
        .all()
    return event_data


@router.get("/audit")
def get_audit_data(tube_id: int,
                   start_date: str,
                   end_date: str,
                   tube: models.Tube = Depends(depends_utils.get_tube),
                   db: Session = Depends(get_db),
                   ):
    start_date = date_utils.get_datetime(start_date)
    end_date = date_utils.get_datetime(end_date)
    audit_data = db.query(models.AuditData) \
        .filter(models.AuditData.date >= start_date,
                models.AuditData.date < end_date,
                models.AuditData.tube_id == tube_id) \
        .order_by(models.AuditData.date.asc()) \
        .all()
    return audit_data


def get_tube_contract_hour(db: Session, tube_id: int) -> int:
    tube = db.query(models.Tube).filter(models.Tube.id == tube_id).first()
    if not tube:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Tube with id={tube_id} not found")
    return tube.contract_hour
