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
[ 基础装饰器 ]

"""


# --------------------------------------------------------------------------
def deco_singleton(cls):
    """
    [ 单例模式装饰器 ]

    ---
    描述
    - 冠以该装饰器的类在整个程序的生命周期中只会被实例化一次, 重复实例化返回已有实例。

    """
    global_instances = {}
    def _deco_singleton(*args, **kwargs):
        if cls not in global_instances:
            global_instances[cls] = cls(*args, **kwargs)
        return global_instances[cls]
    return _deco_singleton
