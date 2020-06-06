#pragma once

#include "esphome/core/component.h"
#include "esphome/core/automation.h"
#include "esphome/core/helpers.h"
#include "esphome/components/light/light_state.h"

namespace esphome {
namespace light_selector {
  
class SelectorComponent : public Component {
 public:
  operator light::LightState*() const { return lights_[idx_]; }
  void setup() override {}
  void loop() override {}
  
  void prev();
  void set(byte idx);
  void next();
  light::LightState *get_light();
  void add_light(light::LightState *state);

  void add_lights(std::initializer_list<light::LightState*> lights) {
    for (light::LightState* light : lights)
      add_light(light);
  }
  void add_on_state_callback(std::function<void(int)> &&callback) {
    state_callback_.add(std::move(callback));
  }

 protected:
   byte idx_ = 0;
   CallbackManager<void(int)> state_callback_{};
   std::vector<light::LightState *> lights_{};
};

class SelectorStateTrigger : public Trigger<int> {
 public:
  explicit SelectorStateTrigger(SelectorComponent *parent) {
    parent->add_on_state_callback([this](int value) { this->trigger(value); });
  }
};


template<typename... Ts> class SelectorSetAction : public Action<Ts...> {
 public:
  explicit SelectorSetAction(SelectorComponent *parent) : parent_(parent) {}

  void play(Ts... x) override { this->parent_->set(idx_); }

  void set_value(byte v) {
    idx_ = v;
  }

 protected:
  SelectorComponent *parent_;
  byte idx_ = 0;
};

template<typename... Ts> class SelectorNextAction : public Action<Ts...> {
 public:
  explicit SelectorNextAction(SelectorComponent *parent) : parent_(parent) {}

  void play(Ts... x) override { this->parent_->next(); }

 protected:
  SelectorComponent *parent_;
};

template<typename... Ts> class SelectorPrevAction : public Action<Ts...> {
 public:
  explicit SelectorPrevAction(SelectorComponent *parent) : parent_(parent) {}

  void play(Ts... x) override { this->parent_->prev(); }

 protected:
  SelectorComponent *parent_;
};



}  // namespace light_selector
}  // namespace esphome
