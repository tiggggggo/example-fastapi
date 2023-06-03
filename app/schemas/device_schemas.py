from datetime import datetime, time

from pydantic import BaseModel


class BaseDevice(BaseModel):
    id: int
    user_id: int
    device_login: int
    device_password: str
    device_type: int
    device_hw_version: int
    device_sw_version: str
    check_sum_sw_version: int
    device_serial_number: str
    month_of_built: int
    year_of_built: int
    device_date_next_cal: datetime
    poll_start: time
    poll_end: time
    tube_count: int
    name_enterprais: str
    address_enterprais: str
    device_install_site: str
    base_temperature_unit: int
    base_pressure_unit: int
    base_diffpressure_unit: int
    base_volume_unit: int
    number_my_mobile: str
    number_mobile_1: str
    number_mobile_2: str
    number_mobile_3: str
    mode_input_signal1: int
    mode_input_signal2: int
    mode_input_signal3: int
    mode_input_signal4: int
    delay_input_signal1: int
    delay_input_signal2: int
    delay_input_signal3: int
    delay_input_signal4: int
    mode_output_signal1: int
    mode_output_signal2: int
    mode_output_signal3: int
    mode_output_signal4: int
    tau_output_signal1: int
    tau_output_signal2: int
    tau_output_signal3: int
    tau_output_signal4: int
    val_output_signal1: float
    val_output_signal2: float
    val_output_signal3: float
    val_output_signal4: float
    mode_change_win_sum: int
    hour_change_win_sum: int
    change_win_sum_date_time: datetime
    change_sum_win_date_time: datetime
    date_time_last_change: datetime

    class Config:
        orm_mode = True


class DeviceDetails(BaseDevice):
    pass
