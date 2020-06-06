from esphome import config_validation as cv, automation
from esphome import codegen as cg
from esphome.const import CONF_ID, CONF_VALUE, CONF_ON_VALUE, CONF_TRIGGER_ID
from esphome.core import coroutine_with_priority
from esphome.cpp_types import Component

light_ns = cg.esphome_ns.namespace('light')
LightState = light_ns.class_('LightState', cg.Nameable, cg.Component)

CONF_LIGHTS = "lights"
CONF_LIGHT = "light"

MULTI_CONF = True

light_selector_ns = cg.esphome_ns.namespace('light_selector')
SelectorComponent = light_selector_ns.class_('SelectorComponent', cg.Component)
SelectorSetAction = light_selector_ns.class_('SelectorSetAction', automation.Action)
SelectorNextAction = light_selector_ns.class_('SelectorNextAction', automation.Action)
SelectorPrevAction = light_selector_ns.class_('SelectorPrevAction', automation.Action)

SelectorStateTrigger = light_selector_ns.class_('SelectorStateTrigger', automation.Trigger.template(cg.int_))

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(SelectorComponent),
    cv.Optional(CONF_LIGHT): cv.use_id(Component),
    cv.Optional(CONF_LIGHTS): cv.All([cv.use_id(Component)], cv.Length(min=1)),
    cv.Optional(CONF_ON_VALUE): automation.validate_automation({
        cv.GenerateID(CONF_TRIGGER_ID): cv.declare_id(SelectorStateTrigger),
    }),
}).extend(cv.COMPONENT_SCHEMA)

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)
    lights_ = []
    for conf in config[CONF_LIGHTS]:
       templ = yield cg.get_variable(conf)
       lights_.append(templ)
    cg.add(var.add_lights(lights_))


@automation.register_action('light_selector.set', SelectorSetAction, cv.Schema({
    cv.Required(CONF_ID): cv.use_id(SelectorComponent),
    cv.Required(CONF_VALUE): cv.templatable(cv.int_),
}))
def light_selector_set_to_code(config, action_id, template_arg, args):
    paren = yield cg.get_variable(config[CONF_ID])
    var = cg.new_Pvariable(action_id, template_arg, paren)
    template_ = yield cg.templatable(config[CONF_VALUE], args, int)
    cg.add(var.set_value(template_))
    yield var

@automation.register_action('light_selector.next', SelectorNextAction, automation.maybe_simple_id({
    cv.Required(CONF_ID): cv.use_id(SelectorComponent),
}))
def light_selector_next_to_code(config, action_id, template_arg, args):
    paren = yield cg.get_variable(config[CONF_ID])
    var = cg.new_Pvariable(action_id, template_arg, paren)
    yield var

@automation.register_action('light_selector.prev', SelectorPrevAction, automation.maybe_simple_id({
    cv.Required(CONF_ID): cv.use_id(SelectorComponent),
}))
def light_selector_prev_to_code(config, action_id, template_arg, args):
    paren = yield cg.get_variable(config[CONF_ID])
    var = cg.new_Pvariable(action_id, template_arg, paren)
    yield var