#pragma once

#include "esphome/core/component.h"
#include "esphome/components/sensor/sensor.h"
#include "esphome/components/binary_sensor/binary_sensor.h"

#include "Keypad.h"

namespace esphome {
namespace keypad {

class KeypadSensor : public sensor::Sensor {
  friend class KeypadComponent;

 public:
  void process(Key key) {
    if (key.kstate == PRESSED) {
      this->publish_state(key.kchar - '0');
    }
  }
};

class KeypadChannel : public binary_sensor::BinarySensor {
  friend class KeypadComponent;
 public:
  void set_key(String key) { key_ = key.c_str()[0]; }
  char get_key() { return key_; }
  void process(KeyState state) {
    if (state == PRESSED) {
      this->publish_state(true);
    } else if (state == RELEASED) {
      this->publish_state(false);
    }
  }

 protected:
  char key_{0};
};

class KeypadComponent : public Component {
 private:
   bool enabled_ = true;
 public:
  void register_channel(KeypadChannel *channel) { this->channels_.push_back(channel); }
  void set_sensor(KeypadSensor *sensor) {
    this->sensor_ = sensor;
  }
  void set_column_pins(std::initializer_list<GPIOPin*> pins, size_t len);
  void set_row_pins(std::initializer_list<GPIOPin*> pins, size_t len);
  void set_keys(String keys) { hexaKeys = strdup(keys.c_str()); };
  void set_debounce(uint8_t debounce) { this->debounce_ = debounce; };
  void setup() override;
  void dump_config() override;
  float get_setup_priority() const override { return setup_priority::DATA; }
  void loop() override;
  static void keypadEvent(KeypadEvent key);
  void enable() { enabled_ = true; };
  void disable() { enabled_ = false; };
  bool isEnabled() { return enabled_; };
 protected:
  std::vector<KeypadChannel *> channels_{};
  KeypadSensor *sensor_ = nullptr;
  uint8_t debounce_{0};
  byte *row_pins_{};
  byte *col_pins_{};
  byte columns_{0};
  byte rows_{0};
  Keypad *customKeypad;
  char *hexaKeys;
};

}  // namespace keypad
}  // namespace esphome
