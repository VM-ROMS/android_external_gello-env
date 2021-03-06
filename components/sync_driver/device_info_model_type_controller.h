// Copyright 2016 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef COMPONENTS_SYNC_DRIVER_DEVICE_INFO_MODEL_TYPE_CONTROLLER_H_
#define COMPONENTS_SYNC_DRIVER_DEVICE_INFO_MODEL_TYPE_CONTROLLER_H_

#include <memory>

#include "components/sync_driver/local_device_info_provider.h"
#include "components/sync_driver/ui_model_type_controller.h"

namespace sync_driver {
class LocalDeviceInfoProvider;
class SyncClient;
}

namespace sync_driver_v2 {

// DataTypeController for DEVICE_INFO model type.
class DeviceInfoModelTypeController : public UIModelTypeController {
 public:
  DeviceInfoModelTypeController(
      const scoped_refptr<base::SingleThreadTaskRunner>& ui_thread,
      const base::Closure& error_callback,
      sync_driver::SyncClient* sync_client,
      sync_driver::LocalDeviceInfoProvider* local_device_info_provider);

 private:
  ~DeviceInfoModelTypeController() override;

  sync_driver::LocalDeviceInfoProvider* const local_device_info_provider_;
  std::unique_ptr<sync_driver::LocalDeviceInfoProvider::Subscription>
      subscription_;
  DISALLOW_COPY_AND_ASSIGN(DeviceInfoModelTypeController);
};

}  // namespace sync_driver_v2

#endif  // COMPONENTS_SYNC_DRIVER_DEVICE_INFO_MODEL_TYPE_CONTROLLER_H_
