#include "keypad.h"
#include "esphome/core/log.h"

namespace esphome {
namespace keypad {

static const char *TAG = "keypad";

void KeypadComponent::setup() {
  ESP_LOGCONFIG(TAG, "Setting up KEYPAD...");
  customKeypad = new Keypad(hexaKeys, row_pins_, col_pins_, rows_, columns_); 
};

void KeypadComponent::dump_config() {
  ESP_LOGCONFIG(TAG, "KEYPAD:");
  ESP_LOGCONFIG(TAG, "Keys: %s", hexaKeys);
  ESP_LOGCONFIG(TAG, "Columns: %d", columns_);
  ESP_LOGCONFIG(TAG, "Rows: %d", rows_);
}

void KeypadComponent::set_column_pins(std::initializer_list<GPIOPin*> pins, size_t len) {
  ESP_LOGCONFIG(TAG, "_Columns: %d", len);
  columns_ = len;
  col_pins_ = new byte[len];
  byte i = 0;
  for (GPIOPin* pin : pins)
    col_pins_[i++] = pin->get_pin();
}
void KeypadComponent::set_row_pins(std::initializer_list<GPIOPin*> pins, size_t len) {
  ESP_LOGCONFIG(TAG, "_Rows: %d", len);
  rows_ = len;
  row_pins_ = new byte[len];
  byte i = 0;
  for (GPIOPin* pin : pins)
    row_pins_[i++] = pin->get_pin();
}

void KeypadComponent::loop() {
  if (customKeypad->getKeys()) {
    for(byte i = 0; i < LIST_MAX; i++) {
      Key key = customKeypad->key[i];
      if (key.stateChanged) {
        if (key.kstate == PRESSED) 
          ESP_LOGD(TAG,"PRESSED %c", key.kchar);
        else if (key.kstate ==  RELEASED) ESP_LOGD(TAG,"RELEASED %c", key.kchar);
        if (sensor_ != nullptr && key.kchar >= '0' && key.kchar <= '9') {
          sensor_->process(key);
        }
        for (auto *channel : channels_) {
          if (channel->get_key() == key.kchar) {
            channel->process(key.kstate);
            break;
          }
        }
      }
    }
  }
}

}  // namespace keypad
}  // namespace esphome
