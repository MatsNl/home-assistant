"""Tests for the Atag sensor platform."""

from homeassistant.components.atag.sensor import SENSORS
from homeassistant.const import CONF_DEVICE
from homeassistant.core import HomeAssistant

from tests.components.atag import init_integration
from tests.test_util.aiohttp import AiohttpClientMocker


async def test_sensors(
    hass: HomeAssistant, aioclient_mock: AiohttpClientMocker
) -> None:
    """Test the creation of ATAG sensors."""
    entry = await init_integration(hass, aioclient_mock)
    registry = await hass.helpers.entity_registry.async_get_registry()

    for item in SENSORS:
        sensor_id = "_".join(f"sensor.{item}".lower().split())
        assert registry.async_is_registered(sensor_id)
        entry = registry.async_get(sensor_id)
        assert entry.unique_id in [f"{CONF_DEVICE}-{v}" for v in SENSORS.values()]
