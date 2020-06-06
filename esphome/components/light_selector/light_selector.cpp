#include "light_selector.h"
#include "esphome/core/log.h"

namespace esphome {
namespace light_selector {

static const char *TAG = "light_selector";

  void SelectorComponent::prev() {
    if (idx_ == 0) {
      idx_ = lights_.size();
    }
    idx_--;
    this->state_callback_.call(idx_);
    ESP_LOGD(TAG, "selected light %s", lights_[idx_]->get_name().c_str());
  }

  void SelectorComponent::set(byte idx) {
    idx_ = constrain(idx, 0, lights_.size() - 1);
    this->state_callback_.call(idx_);
    ESP_LOGD(TAG, "selected light %s", lights_[idx_]->get_name().c_str());
  }

  void SelectorComponent::next() {
    idx_++;
    if (idx_ >= lights_.size()) {
      idx_ = 0;
    }  
    this->state_callback_.call(idx_);
    ESP_LOGD(TAG, "selected light %s", lights_[idx_]->get_name().c_str());
  }

  light::LightState *SelectorComponent::get_light() {
    return lights_[idx_];
  }

  void SelectorComponent::add_light(light::LightState *state) {
    lights_.push_back(state);
  }

}  // namespace light_selector
}  // namespace esphome
