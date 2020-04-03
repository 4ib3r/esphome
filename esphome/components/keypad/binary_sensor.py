import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import binary_sensor
from esphome.const import CONF_CHANNEL, CONF_ID
from . import keypad_ns, KeypadComponent, CONF_KEYPAD_ID

DEPENDENCIES = ['keypad']
KeypadChannel = keypad_ns.class_('KeypadChannel', binary_sensor.BinarySensor)

CONFIG_SCHEMA = binary_sensor.BINARY_SENSOR_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(KeypadChannel),
    cv.GenerateID(CONF_KEYPAD_ID): cv.use_id(KeypadComponent),
    cv.Required(CONF_CHANNEL): cv.string,
})


def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield binary_sensor.register_binary_sensor(var, config)
    hub = yield cg.get_variable(config[CONF_KEYPAD_ID])
    cg.add(var.set_key(config[CONF_CHANNEL]))
    cg.add(hub.register_channel(var))
