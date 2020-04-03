import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import CONF_CHANNEL, CONF_ID
from . import keypad_ns, KeypadComponent, CONF_KEYPAD_ID

DEPENDENCIES = ['keypad']
KeypadChannel = keypad_ns.class_('KeypadSensor', sensor.Sensor)

CONFIG_SCHEMA = sensor.SENSOR_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(KeypadChannel),
    cv.GenerateID(CONF_KEYPAD_ID): cv.use_id(KeypadComponent)
})


def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield sensor.register_sensor(var, config)
    hub = yield cg.get_variable(config[CONF_KEYPAD_ID])
    cg.add(hub.set_sensor(var))
