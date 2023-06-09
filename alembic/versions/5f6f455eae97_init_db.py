"""init db

Revision ID: 5f6f455eae97
Revises: 
Create Date: 2023-06-10 18:37:34.317265

"""
import datetime

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '5f6f455eae97'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('device',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('group_id', sa.Integer(), nullable=True),
                    sa.Column('device_login', sa.Integer(), nullable=False, default=0),
                    sa.Column('device_password', sa.String(length=16), nullable=False),
                    sa.Column('device_type', sa.Integer(), nullable=True),
                    sa.Column('device_hw_version', sa.Integer(), nullable=True),
                    sa.Column('device_sw_version', sa.String(length=16), nullable=True),
                    sa.Column('check_sum_sw_version', sa.Integer(), nullable=True),
                    sa.Column('device_serial_number', sa.String(length=16), nullable=True),
                    sa.Column('month_of_built', sa.Integer(), nullable=True),
                    sa.Column('year_of_built', sa.Integer(), nullable=True),
                    sa.Column('device_date_next_cal', postgresql.TIMESTAMP(), nullable=True),
                    sa.Column('poll_start', postgresql.TIME(), nullable=False, default=datetime.time(0, 0, 0)),
                    sa.Column('poll_end', postgresql.TIME(), nullable=False, default=datetime.time(0, 0, 0)),
                    sa.Column('tube_count', sa.Integer(), nullable=False, default=0),
                    sa.Column('name_enterprais', sa.String(length=50), nullable=True),
                    sa.Column('address_enterprais', sa.String(length=120), nullable=True),
                    sa.Column('device_install_site', sa.String(length=16), nullable=True),
                    sa.Column('base_temperature_unit', sa.Integer(), nullable=True),
                    sa.Column('base_pressure_unit', sa.Integer(), nullable=True),
                    sa.Column('base_diffpressure_unit', sa.Integer(), nullable=True),
                    sa.Column('base_volume_unit', sa.Integer(), nullable=True),
                    sa.Column('number_my_mobile', sa.String(length=20), nullable=True),
                    sa.Column('number_mobile_1', sa.String(length=20), nullable=True),
                    sa.Column('number_mobile_2', sa.String(length=20), nullable=True),
                    sa.Column('number_mobile_3', sa.String(length=20), nullable=True),
                    sa.Column('mode_input_signal1', sa.Integer(), nullable=True),
                    sa.Column('mode_input_signal2', sa.Integer(), nullable=True),
                    sa.Column('mode_input_signal3', sa.Integer(), nullable=True),
                    sa.Column('mode_input_signal4', sa.Integer(), nullable=True),
                    sa.Column('delay_input_signal1', sa.Integer(), nullable=True),
                    sa.Column('delay_input_signal2', sa.Integer(), nullable=True),
                    sa.Column('delay_input_signal3', sa.Integer(), nullable=True),
                    sa.Column('delay_input_signal4', sa.Integer(), nullable=True),
                    sa.Column('mode_output_signal1', sa.Integer(), nullable=True),
                    sa.Column('mode_output_signal2', sa.Integer(), nullable=True),
                    sa.Column('mode_output_signal3', sa.Integer(), nullable=True),
                    sa.Column('mode_output_signal4', sa.Integer(), nullable=True),
                    sa.Column('tau_output_signal1', sa.Integer(), nullable=True),
                    sa.Column('tau_output_signal2', sa.Integer(), nullable=True),
                    sa.Column('tau_output_signal3', sa.Integer(), nullable=True),
                    sa.Column('tau_output_signal4', sa.Integer(), nullable=True),
                    sa.Column('val_output_signal1', sa.Float(), nullable=True),
                    sa.Column('val_output_signal2', sa.Float(), nullable=True),
                    sa.Column('val_output_signal3', sa.Float(), nullable=True),
                    sa.Column('val_output_signal4', sa.Float(), nullable=True),
                    sa.Column('mode_change_win_sum', sa.Integer(), nullable=True),
                    sa.Column('hour_change_win_sum', sa.Integer(), nullable=True),
                    sa.Column('change_win_sum_date_time', postgresql.TIMESTAMP(), nullable=True),
                    sa.Column('change_sum_win_date_time', postgresql.TIMESTAMP(), nullable=True),
                    sa.Column('date_time_last_change', postgresql.TIMESTAMP(), nullable=False,
                              default=datetime.datetime(1980, 1, 1, 0, 0, 0)),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('group',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('group_name', sa.String(length=25), nullable=False),
                    sa.Column('description', sa.Text(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                              nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_table('alarm_data',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('device_id', sa.Integer(), nullable=False),
                    sa.Column('date', postgresql.TIMESTAMP(), nullable=False),
                    sa.Column('code_alarm', sa.Integer(), nullable=True),
                    sa.Column('value_alarm', sa.Float(), nullable=True),
                    sa.Column('status', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['device_id'], ['device.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('event_data',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('device_id', sa.Integer(), nullable=False),
                    sa.Column('date', postgresql.TIMESTAMP(), nullable=False),
                    sa.Column('code_event', sa.Integer(), nullable=True),
                    sa.Column('value_event', sa.BigInteger(), nullable=True),
                    sa.Column('status', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['device_id'], ['device.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('tube',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('tube_no', sa.Integer(), nullable=False),
                    sa.Column('device_id', sa.Integer(), nullable=False),
                    sa.Column('flowmeter_install_site', sa.String(length=16), nullable=True),
                    sa.Column('type_flowmeter', sa.String(length=16), nullable=True),
                    sa.Column('serial_number_flowmeter', sa.String(length=16), nullable=True),
                    sa.Column('date_cal_flowmeter', postgresql.TIMESTAMP(), nullable=True),
                    sa.Column('flowmeter_hi', sa.Float(), nullable=True),
                    sa.Column('flowmeter_lo', sa.Float(), nullable=True),
                    sa.Column('flowmeter_zone', sa.Float(), nullable=True),
                    sa.Column('impuls_of_volume', sa.Float(), nullable=True),
                    sa.Column('mode_freq_main_impuls', sa.Integer(), nullable=True),
                    sa.Column('calibration_flow_chanel', postgresql.TIMESTAMP(), nullable=True),
                    sa.Column('flometer_hi_base', sa.Float(), nullable=True),
                    sa.Column('flometer_lo_base', sa.Float(), nullable=True),
                    sa.Column('mode_temperature_sens', sa.Integer(), nullable=True),
                    sa.Column('type_temperature_sens', sa.String(length=16), nullable=True),
                    sa.Column('serial_number_temp_sens', sa.String(length=16), nullable=True),
                    sa.Column('next_date_cal_temp_sens', postgresql.TIMESTAMP(), nullable=True),
                    sa.Column('range_t_max', sa.Float(), nullable=True),
                    sa.Column('range_t_max_unit', sa.Integer(), nullable=True),
                    sa.Column('range_t_min', sa.Float(), nullable=True),
                    sa.Column('range_t_min_unit', sa.Integer(), nullable=True),
                    sa.Column('calibration_temp_chanel', postgresql.TIMESTAMP(), nullable=True),
                    sa.Column('range_t_hi', sa.Float(), nullable=True),
                    sa.Column('range_t_hi_unit', sa.Integer(), nullable=True),
                    sa.Column('range_t_lo', sa.Float(), nullable=True),
                    sa.Column('range_t_lo_unit', sa.Integer(), nullable=True),
                    sa.Column('mode_pressure_sens', sa.Integer(), nullable=True),
                    sa.Column('type_pressure_sens', sa.String(length=16), nullable=True),
                    sa.Column('serial_number_pres_sens', sa.String(length=16), nullable=True),
                    sa.Column('next_date_cal_press_sens', postgresql.TIMESTAMP(), nullable=True),
                    sa.Column('range_p_max', sa.Float(), nullable=True),
                    sa.Column('range_p_max_unit', sa.Integer(), nullable=True),
                    sa.Column('range_p_min', sa.Float(), nullable=True),
                    sa.Column('range_p_min_unit', sa.Integer(), nullable=True),
                    sa.Column('calibration_p_chanel', postgresql.TIMESTAMP(), nullable=True),
                    sa.Column('range_p_hi', sa.Float(), nullable=True),
                    sa.Column('range_p_hi_unit', sa.Integer(), nullable=True),
                    sa.Column('range_p_lo', sa.Float(), nullable=True),
                    sa.Column('range_p_lo_unit', sa.Integer(), nullable=True),
                    sa.Column('mode_dp', sa.Integer(), nullable=True),
                    sa.Column('type_dp1_sens', sa.String(length=16), nullable=True),
                    sa.Column('serial_number_dp1_sens', sa.String(length=16), nullable=True),
                    sa.Column('next_date_cal_dpress_sens', postgresql.TIMESTAMP(), nullable=True),
                    sa.Column('range_dp1_max', sa.Float(), nullable=True),
                    sa.Column('range_dp1_max_unit', sa.Integer(), nullable=True),
                    sa.Column('range_dp1_min', sa.Float(), nullable=True),
                    sa.Column('range_dp1_min_unit', sa.Integer(), nullable=True),
                    sa.Column('calibration_dp_chanel', postgresql.TIMESTAMP(), nullable=True),
                    sa.Column('range_dp1_hi', sa.Float(), nullable=True),
                    sa.Column('range_dp1_hi_unit', sa.Integer(), nullable=True),
                    sa.Column('range_dp1_lo', sa.Float(), nullable=True),
                    sa.Column('range_dp1_lo_unit', sa.Integer(), nullable=True),
                    sa.Column('mode_dp2', sa.Integer(), nullable=True),
                    sa.Column('type_dp2_sens', sa.String(length=16), nullable=True),
                    sa.Column('serial_number_dp2_sens', sa.String(length=16), nullable=True),
                    sa.Column('next_date_cal_dp2', postgresql.TIMESTAMP(), nullable=True),
                    sa.Column('range_dp2_max', sa.Float(), nullable=True),
                    sa.Column('range_dp2_max_unit', sa.Integer(), nullable=True),
                    sa.Column('range_dp2_min', sa.Float(), nullable=True),
                    sa.Column('range_dp2_min_unit', sa.Integer(), nullable=True),
                    sa.Column('calibration_dp2_chanel', postgresql.TIMESTAMP(), nullable=True),
                    sa.Column('range_dp2_hi', sa.Float(), nullable=True),
                    sa.Column('range_dp2_hi_unit', sa.Integer(), nullable=True),
                    sa.Column('range_dp2_lo', sa.Float(), nullable=True),
                    sa.Column('range_dp2_lo_unit', sa.Integer(), nullable=True),
                    sa.Column('mode_dp3', sa.Integer(), nullable=True),
                    sa.Column('type_dp3_sens', sa.String(length=16), nullable=True),
                    sa.Column('serial_number_dp3_sens', sa.String(length=16), nullable=True),
                    sa.Column('next_date_cal_dp3', postgresql.TIMESTAMP(), nullable=True),
                    sa.Column('range_dp3_max', sa.Float(), nullable=True),
                    sa.Column('range_dp3_max_unit', sa.Integer(), nullable=True),
                    sa.Column('range_dp3_min', sa.Float(), nullable=True),
                    sa.Column('range_dp3_min_unit', sa.Integer(), nullable=True),
                    sa.Column('calibration_dp3_chanel', postgresql.TIMESTAMP(), nullable=True),
                    sa.Column('range_dp3_hi', sa.Float(), nullable=True),
                    sa.Column('range_dp3_hi_unit', sa.Integer(), nullable=True),
                    sa.Column('range_dp3_lo', sa.Float(), nullable=True),
                    sa.Column('range_dp3_lo_unit', sa.Integer(), nullable=True),
                    sa.Column('count_lf2_impuls', sa.Integer(), nullable=True),
                    sa.Column('interval_lf2_impuls', sa.Integer(), nullable=True),
                    sa.Column('contract_hour', sa.Integer(), nullable=False),
                    sa.Column('contract_day', sa.Integer(), nullable=True),
                    sa.Column('measurment_interval', sa.Integer(), nullable=True),
                    sa.Column('integrated_interval', sa.Integer(), nullable=True),
                    sa.Column('method_calc_k', sa.Float(), nullable=True),
                    sa.Column('base_temp', sa.Float(), nullable=True),
                    sa.Column('base_temp_unit', sa.Integer(), nullable=True),
                    sa.Column('base_press', sa.Float(), nullable=True),
                    sa.Column('base_press_unit', sa.Integer(), nullable=True),
                    sa.Column('base_density', sa.Float(), nullable=True),
                    sa.Column('base_density_unit', sa.Integer(), nullable=True),
                    sa.Column('co2_mol', sa.Float(), nullable=True),
                    sa.Column('n2_mol', sa.Float(), nullable=True),
                    sa.Column('barometric_press', sa.Float(), nullable=True),
                    sa.Column('mode_const_status', sa.Integer(), nullable=True),
                    sa.Column('const_temp', sa.Float(), nullable=True),
                    sa.Column('const_temp_unit', sa.Integer(), nullable=True),
                    sa.Column('const_press', sa.Float(), nullable=True),
                    sa.Column('const_press_unit', sa.Integer(), nullable=True),
                    sa.Column('const_dp', sa.Float(), nullable=True),
                    sa.Column('const_dp_unit', sa.Integer(), nullable=True),
                    sa.Column('const_compress', sa.Float(), nullable=True),
                    sa.Column('const_compress_unit', sa.Integer(), nullable=True),
                    sa.Column('const_temp_default', sa.Float(), nullable=True),
                    sa.Column('const_temp_default_unit', sa.Integer(), nullable=True),
                    sa.Column('const_press_default', sa.Float(), nullable=True),
                    sa.Column('const_press_default_unit', sa.Integer(), nullable=True),
                    sa.Column('const_dp_default', sa.Float(), nullable=True),
                    sa.Column('const_dp_default_unit', sa.Integer(), nullable=True),
                    sa.Column('const_compress_default', sa.Float(), nullable=True),
                    sa.Column('const_compress_default_unit', sa.Integer(), nullable=True),
                    sa.Column('big_orifice', sa.Float(), nullable=True),
                    sa.Column('small_orifice', sa.Float(), nullable=True),
                    sa.Column('material_tube', sa.Integer(), nullable=True),
                    sa.Column('material_diaf', sa.Integer(), nullable=True),
                    sa.Column('r_sh_tube', sa.Float(), nullable=True),
                    sa.Column('r_sh_tube_unit', sa.Integer(), nullable=True),
                    sa.Column('method_calc_kp', sa.Integer(), nullable=True),
                    sa.Column('radius_diafragm', sa.Float(), nullable=True),
                    sa.Column('radius_diafragm_unit', sa.Integer(), nullable=True),
                    sa.Column('tau_control_period', sa.Float(), nullable=True),
                    sa.Column('date_control_diaf', postgresql.TIMESTAMP(), nullable=True),
                    sa.Column('method_orifice', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['device_id'], ['device.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('user_device',
                    sa.Column('user_id', sa.Integer(), nullable=True),
                    sa.Column('device_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['device_id'], ['device.id'], ),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
                    )
    op.create_table('audit_data',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('tube_id', sa.Integer(), nullable=False),
                    sa.Column('date', postgresql.TIMESTAMP(), nullable=False),
                    sa.Column('level_and_user', sa.Integer(), nullable=True),
                    sa.Column('code_audit', sa.Integer(), nullable=True),
                    sa.Column('old_value_audit', sa.String(length=50), nullable=True),
                    sa.Column('new_value_audit', sa.String(length=50), nullable=True),
                    sa.ForeignKeyConstraint(['tube_id'], ['tube.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('day_data',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('tube_id', sa.Integer(), nullable=False),
                    sa.Column('date', postgresql.TIMESTAMP(), nullable=False),
                    sa.Column('vc', sa.Float(), nullable=True),
                    sa.Column('vtot', sa.Float(), nullable=True),
                    sa.Column('vm', sa.Float(), nullable=True),
                    sa.Column('vb', sa.Float(), nullable=True),
                    sa.Column('vmerr', sa.Float(), nullable=True),
                    sa.Column('vberr', sa.Float(), nullable=True),
                    sa.Column('vmqmin', sa.Float(), nullable=True),
                    sa.Column('vbqmin', sa.Float(), nullable=True),
                    sa.Column('qbmin', sa.Float(), nullable=True),
                    sa.Column('qb', sa.Float(), nullable=True),
                    sa.Column('qbmax', sa.Float(), nullable=True),
                    sa.Column('qmmin', sa.Float(), nullable=True),
                    sa.Column('qm', sa.Float(), nullable=True),
                    sa.Column('qmmax', sa.Float(), nullable=True),
                    sa.Column('presmin', sa.Float(), nullable=True),
                    sa.Column('pres', sa.Float(), nullable=True),
                    sa.Column('presmax', sa.Float(), nullable=True),
                    sa.Column('tempmin', sa.Float(), nullable=True),
                    sa.Column('temp', sa.Float(), nullable=True),
                    sa.Column('tempmax', sa.Float(), nullable=True),
                    sa.Column('correction_coef_min', sa.Float(), nullable=True),
                    sa.Column('correction_coef', sa.Float(), nullable=True),
                    sa.Column('correction_coef_max', sa.Float(), nullable=True),
                    sa.Column('compress_coef_max', sa.Float(), nullable=True),
                    sa.Column('compress_coef', sa.Float(), nullable=True),
                    sa.Column('compress_coef_min', sa.Float(), nullable=True),
                    sa.Column('air_tempmin', sa.Float(), nullable=True),
                    sa.Column('air_temp', sa.Float(), nullable=True),
                    sa.Column('air_tempmax', sa.Float(), nullable=True),
                    sa.Column('dpmin', sa.Float(), nullable=True),
                    sa.Column('dp', sa.Float(), nullable=True),
                    sa.Column('dpmax', sa.Float(), nullable=True),
                    sa.Column('tau_alarm_qb', sa.Integer(), nullable=True),
                    sa.Column('tau_alarm_qm', sa.Integer(), nullable=True),
                    sa.Column('tau_alarm_p', sa.Integer(), nullable=True),
                    sa.Column('tau_alarm_t', sa.Integer(), nullable=True),
                    sa.Column('tau_alarm_k', sa.Integer(), nullable=True),
                    sa.Column('tau_alarm_tair', sa.Integer(), nullable=True),
                    sa.Column('tau_alarm_dp', sa.Integer(), nullable=True),
                    sa.Column('tau_alarm_qmin', sa.Integer(), nullable=True),
                    sa.Column('tau', sa.Integer(), nullable=True),
                    sa.Column('tau_active_state_uc', sa.Integer(), nullable=True),
                    sa.Column('counter_byte_gprs', sa.Integer(), nullable=True),
                    sa.Column('status_flags', sa.Integer(), nullable=True),
                    sa.Column('energy', sa.Float(), nullable=True, default=0),
                    sa.ForeignKeyConstraint(['tube_id'], ['tube.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('hour_data',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('tube_id', sa.Integer(), nullable=False),
                    sa.Column('date', postgresql.TIMESTAMP(), nullable=False),
                    sa.Column('vm', sa.Float(), nullable=True),
                    sa.Column('vb', sa.Float(), nullable=True),
                    sa.Column('vmerr', sa.Float(), nullable=True),
                    sa.Column('vberr', sa.Float(), nullable=True),
                    sa.Column('vmqmin', sa.Float(), nullable=True),
                    sa.Column('vbqmin', sa.Float(), nullable=True),
                    sa.Column('qb', sa.Float(), nullable=True),
                    sa.Column('qm', sa.Float(), nullable=True),
                    sa.Column('pres', sa.Float(), nullable=True),
                    sa.Column('temp', sa.Float(), nullable=True),
                    sa.Column('correction_coef', sa.Float(), nullable=True),
                    sa.Column('compress_coef', sa.Float(), nullable=True),
                    sa.Column('air_temp', sa.Float(), nullable=True),
                    sa.Column('dp', sa.Float(), nullable=True),
                    sa.Column('tau', sa.Integer(), nullable=True),
                    sa.Column('status_flags', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['tube_id'], ['tube.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('month_data',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('tube_id', sa.Integer(), nullable=False),
                    sa.Column('date', postgresql.TIMESTAMP(), nullable=False),
                    sa.Column('vc', sa.Float(), nullable=True),
                    sa.Column('vtot', sa.Float(), nullable=True),
                    sa.Column('vm', sa.Float(), nullable=True),
                    sa.Column('vb', sa.Float(), nullable=True),
                    sa.Column('vmerr', sa.Float(), nullable=True),
                    sa.Column('vberr', sa.Float(), nullable=True),
                    sa.Column('vmqmin', sa.Float(), nullable=True),
                    sa.Column('vbqmin', sa.Float(), nullable=True),
                    sa.Column('qbmin', sa.Float(), nullable=True),
                    sa.Column('qb', sa.Float(), nullable=True),
                    sa.Column('qbmax', sa.Float(), nullable=True),
                    sa.Column('qmmin', sa.Float(), nullable=True),
                    sa.Column('qm', sa.Float(), nullable=True),
                    sa.Column('qmmax', sa.Float(), nullable=True),
                    sa.Column('presmin', sa.Float(), nullable=True),
                    sa.Column('pres', sa.Float(), nullable=True),
                    sa.Column('presmax', sa.Float(), nullable=True),
                    sa.Column('tempmin', sa.Float(), nullable=True),
                    sa.Column('temp', sa.Float(), nullable=True),
                    sa.Column('tempmax', sa.Float(), nullable=True),
                    sa.Column('correction_coef_min', sa.Float(), nullable=True),
                    sa.Column('correction_coef', sa.Float(), nullable=True),
                    sa.Column('correction_coef_max', sa.Float(), nullable=True),
                    sa.Column('compress_coef_max', sa.Float(), nullable=True),
                    sa.Column('compress_coef', sa.Float(), nullable=True),
                    sa.Column('compress_coef_min', sa.Float(), nullable=True),
                    sa.Column('air_tempmin', sa.Float(), nullable=True),
                    sa.Column('air_temp', sa.Float(), nullable=True),
                    sa.Column('air_tempmax', sa.Float(), nullable=True),
                    sa.Column('dpmin', sa.Float(), nullable=True),
                    sa.Column('dp', sa.Float(), nullable=True),
                    sa.Column('dpmax', sa.Float(), nullable=True),
                    sa.Column('tau_alarm_qb', sa.Integer(), nullable=True),
                    sa.Column('tau_alarm_qm', sa.Integer(), nullable=True),
                    sa.Column('tau_alarm_p', sa.Integer(), nullable=True),
                    sa.Column('tau_alarm_t', sa.Integer(), nullable=True),
                    sa.Column('tau_alarm_k', sa.Integer(), nullable=True),
                    sa.Column('tau_alarm_tair', sa.Integer(), nullable=True),
                    sa.Column('tau_alarm_dp', sa.Integer(), nullable=True),
                    sa.Column('tau_alarm_qmin', sa.Integer(), nullable=True),
                    sa.Column('tau', sa.Integer(), nullable=True),
                    sa.Column('tau_active_state_uc', sa.Integer(), nullable=True),
                    sa.Column('counter_byte_gprs', sa.Integer(), nullable=True),
                    sa.Column('status_flags', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['tube_id'], ['tube.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('month_data')
    op.drop_table('hour_data')
    op.drop_table('day_data')
    op.drop_table('audit_data')
    op.drop_table('user_device')
    op.drop_table('tube')
    op.drop_table('event_data')
    op.drop_table('alarm_data')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    op.drop_table('group')
    op.drop_table('device')
    # ### end Alembic commands ###
