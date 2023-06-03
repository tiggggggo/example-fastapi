import datetime

from sqlalchemy import Boolean, Column, Table, Integer, String, ForeignKey, Float, BigInteger, Text
# from sqlalchemy.sql.sqltypes import TIMESTAMP, TIME
from sqlalchemy.dialects.postgresql import *
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text

from app.database.database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default="TRUE", nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    user = relationship("User")


class Vote(Base):
    __tablename__ = "votes"

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True)


UserDevice = Table(
    'user_device',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('device_id', Integer, ForeignKey('device.id'))
)


# generate tables from sql alchemy
# try backup
# if backup does not work
# update column types based on postgres types

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))

    devices = relationship("Device", secondary=UserDevice, back_populates="users")
    # tubes = relationship('Tube', secondary=UserDevice, back_populates='users')


class Device(Base):
    __tablename__ = "device"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    group_id = Column(Integer)
    device_login = Column(Integer, nullable=False, default=0)
    device_password = Column(String(16), nullable=False)
    device_type = Column(Integer)
    device_hw_version = Column(Integer)
    device_sw_version = Column(String(16))
    check_sum_sw_version = Column(Integer)
    device_serial_number = Column(String(16))
    month_of_built = Column(Integer)
    year_of_built = Column(Integer)
    device_date_next_cal = Column(TIMESTAMP(timezone=False))
    poll_start = Column(TIME(timezone=False), nullable=False, default=datetime.time(0, 0, 0))
    poll_end = Column(TIME(timezone=False), nullable=False, default=datetime.time(0, 0, 0))
    tube_count = Column(Integer, nullable=False, default=0)
    name_enterprais = Column(String(50))
    address_enterprais = Column(String(120))
    device_install_site = Column(String(16))
    base_temperature_unit = Column(Integer)
    base_pressure_unit = Column(Integer)
    base_diffpressure_unit = Column(Integer)
    base_volume_unit = Column(Integer)
    number_my_mobile = Column(String(20))
    number_mobile_1 = Column(String(20))
    number_mobile_2 = Column(String(20))
    number_mobile_3 = Column(String(20))
    mode_input_signal1 = Column(Integer)
    mode_input_signal2 = Column(Integer)
    mode_input_signal3 = Column(Integer)
    mode_input_signal4 = Column(Integer)
    delay_input_signal1 = Column(Integer)
    delay_input_signal2 = Column(Integer)
    delay_input_signal3 = Column(Integer)
    delay_input_signal4 = Column(Integer)
    mode_output_signal1 = Column(Integer)
    mode_output_signal2 = Column(Integer)
    mode_output_signal3 = Column(Integer)
    mode_output_signal4 = Column(Integer)
    tau_output_signal1 = Column(Integer)
    tau_output_signal2 = Column(Integer)
    tau_output_signal3 = Column(Integer)
    tau_output_signal4 = Column(Integer)
    val_output_signal1 = Column(Float)
    val_output_signal2 = Column(Float)
    val_output_signal3 = Column(Float)
    val_output_signal4 = Column(Float)
    mode_change_win_sum = Column(Integer)
    hour_change_win_sum = Column(Integer)
    change_win_sum_date_time = Column(TIMESTAMP(timezone=False))
    change_sum_win_date_time = Column(TIMESTAMP(timezone=False))
    date_time_last_change = Column(TIMESTAMP(timezone=False), nullable=False,
                                   default=datetime.datetime(1980, 1, 1, 0, 0, 0))

    users = relationship("User", secondary=UserDevice, back_populates="devices",
                         primaryjoin=id == UserDevice.c.device_id, secondaryjoin=id == UserDevice.c.user_id)
    tubes = relationship("Tube", back_populates="device")


class Tube(Base):
    __tablename__ = "tube"

    id = Column(Integer, primary_key=True)
    tube_no = Column(Integer, nullable=False)
    device_id = Column(Integer, ForeignKey("device.id"), nullable=False)
    flowmeter_install_site = Column(String(16))
    type_flowmeter = Column(String(16))
    serial_number_flowmeter = Column(String(16))
    date_cal_flowmeter = Column(TIMESTAMP(timezone=False))
    flowmeter_hi = Column(Float)
    flowmeter_lo = Column(Float)
    flowmeter_zone = Column(Float)
    impuls_of_volume = Column(Float)
    mode_freq_main_impuls = Column(Integer)
    calibration_flow_chanel = Column(TIMESTAMP(timezone=False))
    flometer_hi_base = Column(Float)
    flometer_lo_base = Column(Float)
    mode_temperature_sens = Column(Integer)
    type_temperature_sens = Column(String(16))
    serial_number_temp_sens = Column(String(16))
    next_date_cal_temp_sens = Column(TIMESTAMP(timezone=False))
    range_t_max = Column(Float)
    range_t_max_unit = Column(Integer)
    range_t_min = Column(Float)
    range_t_min_unit = Column(Integer)
    calibration_temp_chanel = Column(TIMESTAMP(timezone=False))
    range_t_hi = Column(Float)
    range_t_hi_unit = Column(Integer)
    range_t_lo = Column(Float)
    range_t_lo_unit = Column(Integer)
    mode_pressure_sens = Column(Integer)
    type_pressure_sens = Column(String(16))
    serial_number_pres_sens = Column(String(16))
    next_date_cal_press_sens = Column(TIMESTAMP(timezone=False))
    range_p_max = Column(Float)
    range_p_max_unit = Column(Integer)
    range_p_min = Column(Float)
    range_p_min_unit = Column(Integer)
    calibration_p_chanel = Column(TIMESTAMP(timezone=False))
    range_p_hi = Column(Float)
    range_p_hi_unit = Column(Integer)
    range_p_lo = Column(Float)
    range_p_lo_unit = Column(Integer)
    mode_dp = Column(Integer)
    type_dp1_sens = Column(String(16))
    serial_number_dp1_sens = Column(String(16))
    next_date_cal_dpress_sens = Column(TIMESTAMP(timezone=False))
    range_dp1_max = Column(Float)
    range_dp1_max_unit = Column(Integer)
    range_dp1_min = Column(Float)
    range_dp1_min_unit = Column(Integer)
    calibration_dp_chanel = Column(TIMESTAMP(timezone=False))
    range_dp1_hi = Column(Float)
    range_dp1_hi_unit = Column(Integer)
    range_dp1_lo = Column(Float)
    range_dp1_lo_unit = Column(Integer)
    mode_dp2 = Column(Integer)
    type_dp2_sens = Column(String(16))
    serial_number_dp2_sens = Column(String(16))
    next_date_cal_dp2 = Column(TIMESTAMP(timezone=False))
    range_dp2_max = Column(Float)
    range_dp2_max_unit = Column(Integer)
    range_dp2_min = Column(Float)
    range_dp2_min_unit = Column(Integer)
    calibration_dp2_chanel = Column(TIMESTAMP(timezone=False))
    range_dp2_hi = Column(Float)
    range_dp2_hi_unit = Column(Integer)
    range_dp2_lo = Column(Float)
    range_dp2_lo_unit = Column(Integer)
    mode_dp3 = Column(Integer)
    type_dp3_sens = Column(String(16))
    serial_number_dp3_sens = Column(String(16))
    next_date_cal_dp3 = Column(TIMESTAMP(timezone=False))
    range_dp3_max = Column(Float)
    range_dp3_max_unit = Column(Integer)
    range_dp3_min = Column(Float)
    range_dp3_min_unit = Column(Integer)
    calibration_dp3_chanel = Column(TIMESTAMP(timezone=False))
    range_dp3_hi = Column(Float)
    range_dp3_hi_unit = Column(Integer)
    range_dp3_lo = Column(Float)
    range_dp3_lo_unit = Column(Integer)
    count_lf2_impuls = Column(Integer)
    interval_lf2_impuls = Column(Integer)
    contract_hour = Column(Integer, nullable=False, default=0)
    contract_day = Column(Integer)
    measurment_interval = Column(Integer)
    integrated_interval = Column(Integer)
    method_calc_k = Column(Float)
    base_temp = Column(Float)
    base_temp_unit = Column(Integer)
    base_press = Column(Float)
    base_press_unit = Column(Integer)
    base_density = Column(Float)
    base_density_unit = Column(Integer)
    co2_mol = Column(Float)
    n2_mol = Column(Float)
    barometric_press = Column(Float)
    mode_const_status = Column(Integer)
    const_temp = Column(Float)
    const_temp_unit = Column(Integer)
    const_press = Column(Float)
    const_press_unit = Column(Integer)
    const_dp = Column(Float)
    const_dp_unit = Column(Integer)
    const_compress = Column(Float)
    const_compress_unit = Column(Integer)
    const_temp_default = Column(Float)
    const_temp_default_unit = Column(Integer)
    const_press_default = Column(Float)
    const_press_default_unit = Column(Integer)
    const_dp_default = Column(Float)
    const_dp_default_unit = Column(Integer)
    const_compress_default = Column(Float)
    const_compress_default_unit = Column(Integer)
    big_orifice = Column(Float)
    small_orifice = Column(Float)
    material_tube = Column(Integer)
    material_diaf = Column(Integer)
    r_sh_tube = Column(Float)
    r_sh_tube_unit = Column(Integer)
    method_calc_kp = Column(Integer)
    radius_diafragm = Column(Float)
    radius_diafragm_unit = Column(Integer)
    tau_control_period = Column(Float)
    date_control_diaf = Column(TIMESTAMP(timezone=False))
    method_orifice = Column(Integer)

    # users = relationship("User", secondary=UserDevice, back_populates="tubes",
    #                      primaryjoin=id == UserDevice.c.tube_id, secondaryjoin=id == UserDevice.c.user_id)
    device = relationship("Device", back_populates="tubes")


class HourData(Base):
    __tablename__ = "hour_data"

    id = Column(Integer, primary_key=True)
    tube_id = Column(Integer, ForeignKey("tube.id"), nullable=False)
    tube = relationship("Tube")
    date = Column(TIMESTAMP(timezone=False), nullable=False)
    vm = Column(Float)
    vb = Column(Float)
    vmerr = Column(Float)
    vberr = Column(Float)
    vmqmin = Column(Float)
    vbqmin = Column(Float)
    qb = Column(Float)
    qm = Column(Float)
    pres = Column(Float)
    temp = Column(Float)
    correction_coef = Column(Float)
    compress_coef = Column(Float)
    air_temp = Column(Float)
    dp = Column(Float)
    tau = Column(Integer)
    status_flags = Column(Integer)


class DayData(Base):
    __tablename__ = "day_data"

    id = Column(Integer, primary_key=True)
    tube_id = Column(Integer, ForeignKey("tube.id"), nullable=False)
    tube = relationship("Tube")
    date = Column(TIMESTAMP(timezone=False), nullable=False)
    vc = Column(Float)
    vtot = Column(Float)
    vm = Column(Float)
    vb = Column(Float)
    vmerr = Column(Float)
    vberr = Column(Float)
    vmqmin = Column(Float)
    vbqmin = Column(Float)
    qbmin = Column(Float)
    qb = Column(Float)
    qbmax = Column(Float)
    qmmin = Column(Float)
    qm = Column(Float)
    qmmax = Column(Float)
    presmin = Column(Float)
    pres = Column(Float)
    presmax = Column(Float)
    tempmin = Column(Float)
    temp = Column(Float)
    tempmax = Column(Float)
    correction_coef_min = Column(Float)
    correction_coef = Column(Float)
    correction_coef_max = Column(Float)
    compress_coef_max = Column(Float)
    compress_coef = Column(Float)
    compress_coef_min = Column(Float)
    air_tempmin = Column(Float)
    air_temp = Column(Float)
    air_tempmax = Column(Float)
    dpmin = Column(Float)
    dp = Column(Float)
    dpmax = Column(Float)
    tau_alarm_qb = Column(Integer)
    tau_alarm_qm = Column(Integer)
    tau_alarm_p = Column(Integer)
    tau_alarm_t = Column(Integer)
    tau_alarm_k = Column(Integer)
    tau_alarm_tair = Column(Integer)
    tau_alarm_dp = Column(Integer)
    tau_alarm_qmin = Column(Integer)
    tau = Column(Integer)
    tau_active_state_uc = Column(Integer)
    counter_byte_gprs = Column(Integer)
    status_flags = Column(Integer)
    energy = Column(Float, default=0)


class MonthData(Base):
    __tablename__ = "month_data"

    id = Column(Integer, primary_key=True)
    tube_id = Column(Integer, ForeignKey("tube.id"), nullable=False)
    tube = relationship("Tube")
    date = Column(TIMESTAMP(timezone=False), nullable=False)
    vc = Column(Float)
    vtot = Column(Float)
    vm = Column(Float)
    vb = Column(Float)
    vmerr = Column(Float)
    vberr = Column(Float)
    vmqmin = Column(Float)
    vbqmin = Column(Float)
    qbmin = Column(Float)
    qb = Column(Float)
    qbmax = Column(Float)
    qmmin = Column(Float)
    qm = Column(Float)
    qmmax = Column(Float)
    presmin = Column(Float)
    pres = Column(Float)
    presmax = Column(Float)
    tempmin = Column(Float)
    temp = Column(Float)
    tempmax = Column(Float)
    correction_coef_min = Column(Float)
    correction_coef = Column(Float)
    correction_coef_max = Column(Float)
    compress_coef_max = Column(Float)
    compress_coef = Column(Float)
    compress_coef_min = Column(Float)
    air_tempmin = Column(Float)
    air_temp = Column(Float)
    air_tempmax = Column(Float)
    dpmin = Column(Float)
    dp = Column(Float)
    dpmax = Column(Float)
    tau_alarm_qb = Column(Integer)
    tau_alarm_qm = Column(Integer)
    tau_alarm_p = Column(Integer)
    tau_alarm_t = Column(Integer)
    tau_alarm_k = Column(Integer)
    tau_alarm_tair = Column(Integer)
    tau_alarm_dp = Column(Integer)
    tau_alarm_qmin = Column(Integer)
    tau = Column(Integer)
    tau_active_state_uc = Column(Integer)
    counter_byte_gprs = Column(Integer)
    status_flags = Column(Integer)


class EventData(Base):
    __tablename__ = "event_data"

    id = Column(Integer, primary_key=True)
    device_id = Column(Integer, ForeignKey("device.id"), nullable=False)
    device = relationship("Device")
    date = Column(TIMESTAMP(timezone=False), nullable=False)
    code_event = Column(Integer)
    value_event = Column(BigInteger)
    status = Column(Integer)


class AlarmData(Base):
    __tablename__ = "alarm_data"

    id = Column(Integer, primary_key=True)
    device_id = Column(Integer, ForeignKey("device.id"), nullable=False)
    device = relationship("Device")
    date = Column(TIMESTAMP(timezone=False), nullable=False)
    code_alarm = Column(Integer)
    value_alarm = Column(Float)
    status = Column(Integer)


class AuditData(Base):
    __tablename__ = "audit_data"

    id = Column(Integer, primary_key=True)
    tube_id = Column(Integer, ForeignKey("tube.id"), nullable=False)
    tube = relationship("Tube")
    date = Column(TIMESTAMP(timezone=False), nullable=False)
    level_and_user = Column(Integer)
    code_audit = Column(Integer)
    old_value_audit = Column(String(50))
    new_value_audit = Column(String(50))


class Group(Base):
    __tablename__ = "group"

    id = Column(Integer, primary_key=True)
    group_name = Column(String(25), nullable=False)
    description = Column(Text)
