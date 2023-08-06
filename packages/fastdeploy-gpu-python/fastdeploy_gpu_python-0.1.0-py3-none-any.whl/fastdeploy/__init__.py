# Copyright (c) 2022 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
import logging

logging.warning("Due to the package size limitation, we have not provide fastdeploy-gpu-python on pypi yet, please execute the following commands to reinstall fastdeploy-gpu-python.")
logging.warning("   =================== Reinstall fastdeploy-gpu-python commands ==================")
logging.warning("   python -m pip uninstall fastdeploy-gpu-python")
logging.warning("   python -m pip install fastdeploy-gpu-python -f https://www.paddlepaddle.org.cn/whl/fastdeploy.html")
raise Exception("Failed to import fastdeploy module.")
