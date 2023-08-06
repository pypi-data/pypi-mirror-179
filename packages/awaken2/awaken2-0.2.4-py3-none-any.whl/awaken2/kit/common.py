# Copyright 2022 quinn.7@foxmail.com All rights reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
[ 引擎套件通用 ]

"""
from ..baseic.const import G_CONST
from .web.web_engine_method_map import WEB_ENGINE_FUNCTION_MAP


WEB_TASK_TEMPLATE = \
"""
## 自述
TaskType = '#TASK_TYPE#'
TaskName = '#TASK_NAME#'
TaskDocs = ''

## 用例
CASE :: TestName :: Docs
    Goto >> 'http://www.baidu.com/'
    Send >> 'Awaken2' >> '#kw'
    ?? True
"""


ENGINE_TYPE_FUNCTION_MAP = {
    G_CONST.Type.Task.Web: WEB_ENGINE_FUNCTION_MAP,
}
""" [ 脚本后缀与引擎类型的映射字典 ]
@ 描述 : 提供给解释器用以判断引擎的合法方法。
"""

TASK_TEMPLATE_MAP = {
    G_CONST.Type.Task.Web : WEB_TASK_TEMPLATE
}
""" [ 脚本后缀与任务模板的映射字典 ]
@ 描述 : NULL
"""
