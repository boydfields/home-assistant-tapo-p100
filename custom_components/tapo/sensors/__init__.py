from plugp100 import TapoDeviceState
from homeassistant.helpers.typing import StateType
from homeassistant.components.sensor import (
    STATE_CLASS_MEASUREMENT,
    STATE_CLASS_TOTAL_INCREASING,
)
from homeassistant.const import (
    POWER_WATT,
    ENERGY_KILO_WATT_HOUR,
    DEVICE_CLASS_ENERGY,
    DEVICE_CLASS_POWER,
    DEVICE_CLASS_SIGNAL_STRENGTH,
    SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
)

from custom_components.tapo.sensors.sensor_config import SensorConfig
from custom_components.tapo.sensors.tapo_sensor_source import TapoSensorSource


class TodayEnergySensorSource(TapoSensorSource):
    def get_config(self) -> SensorConfig:
        return SensorConfig(
            "today energy",
            DEVICE_CLASS_ENERGY,
            STATE_CLASS_TOTAL_INCREASING,
            ENERGY_KILO_WATT_HOUR,
        )

    def get_value(self, state: TapoDeviceState | None) -> StateType:
        if state.energy_info is not None:
            return state.energy_info.today_energy / 1000
        return None


class MonthEnergySensorSource(TapoSensorSource):
    def get_config(self) -> SensorConfig:
        return SensorConfig(
            "month energy",
            DEVICE_CLASS_ENERGY,
            STATE_CLASS_TOTAL_INCREASING,
            ENERGY_KILO_WATT_HOUR,
        )

    def get_value(self, state: TapoDeviceState | None) -> StateType:
        if state.energy_info is not None:
            return state.energy_info.month_energy / 1000
        return None


class ThisMonthEnergySensorSource(TapoSensorSource):
    def get_config(self) -> SensorConfig:
        return SensorConfig(
            "this month energy",
            DEVICE_CLASS_ENERGY,
            STATE_CLASS_TOTAL_INCREASING,
            ENERGY_KILO_WATT_HOUR,
        )

    def get_value(self, state: TapoDeviceState | None) -> StateType:
        if state.energy_info is not None:
            return state.energy_info.this_month_energy / 1000
        return None


class CurrentEnergySensorSource(TapoSensorSource):
    def get_config(self) -> SensorConfig:
        return SensorConfig(
            "current power",
            DEVICE_CLASS_POWER,
            STATE_CLASS_MEASUREMENT,
            POWER_WATT,
        )

    def get_value(self, state: TapoDeviceState | None) -> StateType:
        if state.energy_info is not None:
            return state.energy_info.current_power / 1000
        return None


class OverheatSensorSource(TapoSensorSource):
    def get_config(self) -> SensorConfig:
        return SensorConfig(
            name="overheat",
            device_class="heat",
            state_class=None,
            unit_measure=None,
        )

    def get_value(self, state: TapoDeviceState | None) -> StateType:
        if state is not None:
            return state.overheated
        return None


class SignalSensorSource(TapoSensorSource):
    def get_config(self) -> SensorConfig:
        return SensorConfig(
            name="signal level",
            device_class=DEVICE_CLASS_SIGNAL_STRENGTH,
            state_class=None,
            unit_measure=SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
        )

    def get_value(self, state: TapoDeviceState | None) -> StateType:
        try:
            if state is not None:
                return state.rssi
            return 0
        except Exception:  # pylint: disable=broad-except
            return 0
