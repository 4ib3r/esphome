import esphome.codegen as cg
import esphome.config_validation as cv
from esphome import pins
from esphome.components import display, spi
from esphome.const import CONF_BUSY_PIN, CONF_DC_PIN, CONF_FULL_UPDATE_EVERY, \
    CONF_ID, CONF_LAMBDA, CONF_MODEL, CONF_PAGES, CONF_RESET_PIN

DEPENDENCIES = ['spi']

gxepd2_epaper_ns = cg.esphome_ns.namespace('gxepd2_epaper')
GxEPD2_EPD = gxepd2_epaper_ns.class_('GxEPD2_EPD', cg.PollingComponent, spi.SPIDevice,
                                     display.DisplayBuffer)

MODELS = {
    '154c'      : { 'header': 'GxEPD2_154c.h',
                    'class': gxepd2_epaper_ns.class_('GxEPD2_154c', GxEPD2_EPD)
                  },
    '154_z90c'  : { 'header': 'GxEPD2_154_Z90c.h',
                    'class': gxepd2_epaper_ns.class_('GxEPD2_154_Z90c', GxEPD2_EPD)
                  },
    '213c'      : { 'header': 'GxEPD2_213c.h',
                    'class': gxepd2_epaper_ns.class_('GxEPD2_213c', GxEPD2_EPD)
                  },
    '270c'      : { 'header': 'GxEPD2_270c.h',
                    'class': gxepd2_epaper_ns.class_('GxEPD2_270c', GxEPD2_EPD)
                  },
    '290c'      : { 'header': 'GxEPD2_290c.h',
                    'class': gxepd2_epaper_ns.class_('GxEPD2_290c', GxEPD2_EPD)
                  },
    '420c'      : { 'header': 'GxEPD2_420c.h',
                    'class': gxepd2_epaper_ns.class_('GxEPD2_420c', GxEPD2_EPD)
                  },
    '565c'      : { 'header': 'GxEPD2_565c.h',
                    'class': gxepd2_epaper_ns.class_('GxEPD2_565c', GxEPD2_EPD)
                  },
    '583c'      : { 'header': 'GxEPD2_583c.h',
                    'class': gxepd2_epaper_ns.class_('GxEPD2_583c', GxEPD2_EPD)
                  },
    '750c'      : { 'header': 'GxEPD2_750c.h',
                    'class': gxepd2_epaper_ns.class_('GxEPD2_750c', GxEPD2_EPD)
                  },
    '750c_z08'  : { 'header': 'GxEPD2_750c_Z08.h',
                    'class': gxepd2_epaper_ns.class_('GxEPD2_750c_Z08', GxEPD2_EPD)
                  },
    '750c_z90'  : { 'header': 'GxEPD2_750c_Z90.h',
                    'class': gxepd2_epaper_ns.class_('GxEPD2_750c_Z90', GxEPD2_EPD)
                  },
    '154_d67'   : { 'header': 'GxEPD2_154_D67.h',
                    'class': gxepd2_epaper_ns.class_('GxEPD2_154_D67', GxEPD2_EPD)
                  },
    '154'       : { 'header': 'GxEPD2_154.h',
                    'class': gxepd2_epaper_ns.class_('GxEPD2_154', GxEPD2_EPD)
                  },
    '154_m09'   : { 'header': 'GxEPD2_154_M09.h',
                    'class': gxepd2_epaper_ns.class_('GxEPD2_154_M09', GxEPD2_EPD)
                  },
    '154_m10'   : { 'header': 'GxEPD2_154_M10.h',
                    'class': gxepd2_epaper_ns.class_('GxEPD2_154_M10', GxEPD2_EPD)
                  },
    '154_t8'    : { 'header': 'GxEPD2_154_T8.h',
                    'class': gxepd2_epaper_ns.class_('GxEPD2_154_T8', GxEPD2_EPD)
                  },
    '213_b72'   : { 'header': 'GxEPD2_213_B72.h',
                    'class': gxepd2_epaper_ns.class_('GxEPD2_213_B72', GxEPD2_EPD)
                  },
    '213_b73'   : { 'header': 'GxEPD2_213_B73.h',
                    'class': gxepd2_epaper_ns.class_('GxEPD2_213_B73', GxEPD2_EPD)
                  },
    '213_flex'  : { 'header': 'GxEPD2_213_flex.h',
                    'class': gxepd2_epaper_ns.class_('GxEPD2_213_flex', GxEPD2_EPD)
                  },
    '213'       : { 'header': 'GxEPD2_213.h',
                    'class': gxepd2_epaper_ns.class_('GxEPD2_213', GxEPD2_EPD)
                  },
    '260'       : { 'header': 'GxEPD2_260.h',
                    'class': gxepd2_epaper_ns.class_('GxEPD2_260', GxEPD2_EPD)
                  },
    '270'       : { 'header': 'GxEPD2_270.h',
                    'class': gxepd2_epaper_ns.class_('GxEPD2_270', GxEPD2_EPD)
                  },
    '290'       : { 'header': 'GxEPD2_290.h',
                    'class': gxepd2_epaper_ns.class_('GxEPD2_290', GxEPD2_EPD)
                  },
    '290_t5'    : { 'header': 'GxEPD2_290_T5.h',
                    'class': gxepd2_epaper_ns.class_('GxEPD2_290_T5', GxEPD2_EPD)
                  },
    '371'       : { 'header': 'GxEPD2_371.h',
                    'class': gxepd2_epaper_ns.class_('GxEPD2_371', GxEPD2_EPD)
                  },
    '420'       : { 'header': 'GxEPD2_420.h',
                    'class': gxepd2_epaper_ns.class_('GxEPD2_420', GxEPD2_EPD)
                  },
    '583'       : { 'header': 'GxEPD2_583.h',
                    'class': gxepd2_epaper_ns.class_('GxEPD2_583', GxEPD2_EPD)
                  },
    '583_t8'    : { 'header': 'GxEPD2_583_T8.h',
                    'class': gxepd2_epaper_ns.class_('GxEPD2_583_T8', GxEPD2_EPD)
                  },
    '750'       : { 'header': 'GxEPD2_750.h',
                    'class': gxepd2_epaper_ns.class_('GxEPD2_750', GxEPD2_EPD)
                  },
    '750_t7'    : { 'header': 'GxEPD2_750_T7.h',
                    'class': gxepd2_epaper_ns.class_('GxEPD2_750_T7', GxEPD2_EPD)
                  },
    'it60'      : { 'header': 'GxEPD2_it60.h',
                    'class': gxepd2_epaper_ns.class_('GxEPD2_it60', GxEPD2_EPD)
                  }
}

CONFIG_SCHEMA = cv.All(display.FULL_DISPLAY_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(GxEPD2_EPD),
    cv.Required(CONF_DC_PIN): pins.gpio_output_pin_schema,
    cv.Required(CONF_MODEL): cv.one_of(*MODELS, lower=True),
    cv.Optional(CONF_RESET_PIN): pins.gpio_output_pin_schema,
    cv.Optional(CONF_BUSY_PIN): pins.gpio_input_pin_schema,
    cv.Optional(CONF_FULL_UPDATE_EVERY): cv.uint32_t,
}).extend(cv.polling_component_schema('1s')).extend(spi.spi_device_schema()),
                       cv.has_at_most_one_key(CONF_PAGES, CONF_LAMBDA))

def to_code(config):
    model=MODELS[config[CONF_MODEL]]
    #cg.RawStatement(f'#include "{model["header"]}"') 
    rhs = model["class"].new()
    var = cg.Pvariable(config[CONF_ID], rhs)

    yield cg.register_component(var, config)
    yield display.register_display(var, config)
    yield spi.register_spi_device(var, config)

    dc = yield cg.gpio_pin_expression(config[CONF_DC_PIN])
    cg.add(var.set_dc_pin(dc))

    if CONF_LAMBDA in config:
        lambda_ = yield cg.process_lambda(config[CONF_LAMBDA], [(display.DisplayBufferRef, 'it')],
                                          return_type=cg.void)
        cg.add(var.set_writer(lambda_))
    if CONF_RESET_PIN in config:
        reset = yield cg.gpio_pin_expression(config[CONF_RESET_PIN])
        cg.add(var.set_reset_pin(reset))
    if CONF_BUSY_PIN in config:
        reset = yield cg.gpio_pin_expression(config[CONF_BUSY_PIN])
        cg.add(var.set_busy_pin(reset))
    if CONF_FULL_UPDATE_EVERY in config:
        cg.add(var.set_full_update_every(config[CONF_FULL_UPDATE_EVERY]))
    yield var

