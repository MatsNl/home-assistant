"""Initialization of ATAG One climate platform."""
from typing import List, Optional

from homeassistant.components.climate import ClimateDevice
from homeassistant.components.climate.const import (
    CURRENT_HVAC_HEAT,
    CURRENT_HVAC_IDLE,
<<<<<<< HEAD
    HVAC_MODE_AUTO,
    HVAC_MODE_HEAT,
    PRESET_AWAY,
    PRESET_BOOST,
    SUPPORT_PRESET_MODE,
    SUPPORT_TARGET_TEMPERATURE,
)
from homeassistant.const import ATTR_TEMPERATURE, TEMP_CELSIUS, TEMP_FAHRENHEIT

from . import CLIMATE, DOMAIN, ENTITY_TYPES, AtagEntity

PRESET_SCHEDULE = "Auto"
PRESET_MANUAL = "Manual"
PRESET_EXTEND = "Extend"
SUPPORT_PRESET = [
    PRESET_MANUAL,
    PRESET_SCHEDULE,
    PRESET_EXTEND,
    PRESET_AWAY,
    PRESET_BOOST,
]
SUPPORT_FLAGS = SUPPORT_TARGET_TEMPERATURE | SUPPORT_PRESET_MODE
HVAC_MODES = [HVAC_MODE_AUTO, HVAC_MODE_HEAT]


async def async_setup_entry(hass, entry, async_add_entities):
    """Load a config entry."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([AtagThermostat(coordinator, ENTITY_TYPES[CLIMATE])])


class AtagThermostat(AtagEntity, ClimateDevice):
    """Atag climate device."""

    @property
    def supported_features(self):
        """Return the list of supported features."""
        return SUPPORT_FLAGS
=======
    DEFAULT_MAX_TEMP,
    DEFAULT_MIN_TEMP,
    HVAC_MODE_AUTO,
    HVAC_MODE_HEAT,
    HVAC_MODE_OFF,
    SUPPORT_TARGET_TEMPERATURE,
)
from homeassistant.const import ATTR_TEMPERATURE, TEMP_CELSIUS
from homeassistant.helpers.restore_state import RestoreEntity

from . import CLIMATE, DOMAIN, ENTITY_TYPES, AtagEntity


async def async_setup_platform(hass, _config, async_add_devices, _discovery_info=None):
    """Atag updated to use config entry."""
    pass


async def async_setup_entry(hass, entry, async_add_devices):
    """Load a config entry."""
    atag = hass.data[DOMAIN][entry.entry_id]
    async_add_devices([AtagThermostat(atag, ENTITY_TYPES[CLIMATE])])


class AtagThermostat(AtagEntity, ClimateDevice, RestoreEntity):
    """Atag climate device."""

    def __init__(self, atag, atagtype):
        """Initialize with fake on/off state."""
        super().__init__(atag, atagtype)
        self._on = None

    async def async_added_to_hass(self):
        """Register callbacks & state restore for fake "Off" mode."""
        await super().async_added_to_hass()
        last_state = await self.async_get_last_state()
        if last_state:
            self._on = last_state.state != HVAC_MODE_OFF

    @property
    def supported_features(self):
        """Return the list of supported features."""
        return SUPPORT_TARGET_TEMPERATURE
>>>>>>> add atag integration

    @property
    def hvac_mode(self) -> Optional[str]:
        """Return hvac operation ie. heat, cool mode."""
<<<<<<< HEAD
        if self.coordinator.atag.hvac_mode in HVAC_MODES:
            return self.coordinator.atag.hvac_mode
        return None
=======
        if not self._on:
            return HVAC_MODE_OFF
        return self.atag.hvac_mode
>>>>>>> add atag integration

    @property
    def hvac_modes(self) -> List[str]:
        """Return the list of available hvac operation modes."""
<<<<<<< HEAD
        return HVAC_MODES
=======
        return [HVAC_MODE_HEAT, HVAC_MODE_AUTO, HVAC_MODE_OFF]
>>>>>>> add atag integration

    @property
    def hvac_action(self) -> Optional[str]:
        """Return the current running hvac operation."""
<<<<<<< HEAD
        if self.coordinator.atag.cv_status:
=======
        if self.atag.cv_status:
>>>>>>> add atag integration
            return CURRENT_HVAC_HEAT
        return CURRENT_HVAC_IDLE

    @property
    def temperature_unit(self):
        """Return the unit of measurement."""
<<<<<<< HEAD
        if self.coordinator.atag.temp_unit in [TEMP_CELSIUS, TEMP_FAHRENHEIT]:
            return self.coordinator.atag.temp_unit
        return None
=======
        return TEMP_CELSIUS
>>>>>>> add atag integration

    @property
    def current_temperature(self) -> Optional[float]:
        """Return the current temperature."""
<<<<<<< HEAD
        return self.coordinator.atag.temperature
=======
        return self.atag.temperature
>>>>>>> add atag integration

    @property
    def target_temperature(self) -> Optional[float]:
        """Return the temperature we try to reach."""
<<<<<<< HEAD
        return self.coordinator.atag.target_temperature

    @property
    def preset_mode(self) -> Optional[str]:
        """Return the current preset mode, e.g., auto, manual, fireplace, extend, etc."""
        return self.coordinator.atag.hold_mode

    @property
    def preset_modes(self) -> Optional[List[str]]:
        """Return a list of available preset modes."""
        return SUPPORT_PRESET

    async def async_set_temperature(self, **kwargs) -> None:
        """Set new target temperature."""
        await self.coordinator.atag.set_temp(kwargs.get(ATTR_TEMPERATURE))
        self.async_write_ha_state()

    async def async_set_hvac_mode(self, hvac_mode: str) -> None:
        """Set new target hvac mode."""
        await self.coordinator.atag.set_hvac_mode(hvac_mode)
        self.async_write_ha_state()

    async def async_set_preset_mode(self, preset_mode: str) -> None:
        """Set new preset mode."""
        await self.coordinator.atag.set_hold_mode(preset_mode)
        self.async_write_ha_state()
=======
        return self.atag.target_temperature

    @property
    def max_temp(self):
        """Return the maximum temperature."""
        return DEFAULT_MAX_TEMP

    @property
    def min_temp(self):
        """Return the minimum temperature."""
        return DEFAULT_MIN_TEMP

    async def async_set_temperature(self, **kwargs) -> None:
        """Set new target temperature."""
        if self._on and await self.atag.set_temp(kwargs.get(ATTR_TEMPERATURE)):
            self.async_schedule_update_ha_state(True)

    async def async_set_hvac_mode(self, hvac_mode: str) -> None:
        """Set new target hvac mode."""
        self._on = hvac_mode != HVAC_MODE_OFF
        if self._on:
            await self.atag.set_hvac_mode(hvac_mode)
        self.async_schedule_update_ha_state()
>>>>>>> add atag integration
