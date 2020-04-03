import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import CONF_ID
from esphome import pins

from esphome.helpers import color
from esphome.util import safe_print

CONF_DEBOUNCE = "key_debounce"
CONF_KEYS = "keys"
CONF_ROW_PINS = "row_pins"
CONF_COLUMN_PINS = "col_pins"

AUTO_LOAD = ['binary_sensor', 'sensor']
MULTI_CONF = True

keypad_ns = cg.esphome_ns.namespace('keypad')
KeypadComponent = keypad_ns.class_('KeypadComponent', cg.Component)

CONF_KEYPAD_ID = 'keypad_id'

def validate_pin_length(value):
    if len(value) < 1:
        raise cv.Invalid("Keypads can either operate minimum 1 pin for row/column mode,"
                         "not {}-pin mode".format(len(value)))
    return value
    
CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(KeypadComponent),
    cv.Required(CONF_ROW_PINS): cv.All([pins.gpio_input_pin_schema], validate_pin_length),
    cv.Required(CONF_COLUMN_PINS): cv.All([pins.gpio_input_pin_schema], validate_pin_length),
    cv.Required(CONF_KEYS): cv.string,
    cv.Optional(CONF_DEBOUNCE, default=0): cv.int_range(min=0, max=7),
}).extend(cv.COMPONENT_SCHEMA)


def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)

    cg.add(var.set_keys(config[CONF_KEYS]))

    safe_print("Keypad rows: " + color('cyan', "{}".format(len(config[CONF_ROW_PINS]))))
    row_pins_ = []
    for conf in config[CONF_ROW_PINS]:
       row_pins_.append((yield cg.gpio_pin_expression(conf)))
    cg.add(var.set_row_pins(row_pins_, len(config[CONF_ROW_PINS])))

    safe_print("Keypad columns: " + color('cyan', "{}".format(len(config[CONF_COLUMN_PINS]))))
    column_pins_ = []
    for conf in config[CONF_COLUMN_PINS]:
       column_pins_.append((yield cg.gpio_pin_expression(conf)))
    cg.add(var.set_column_pins(column_pins_, len(config[CONF_COLUMN_PINS])))

    cg.add(var.set_debounce(config[CONF_DEBOUNCE]))
    # https://github.com/Chris--A/Keypad/blob/master/library.properties
    cg.add_library('165', '3.1.1')
