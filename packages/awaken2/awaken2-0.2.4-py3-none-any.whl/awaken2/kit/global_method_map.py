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
脚本全局方法映射

"""
import re

from .global_method import G_GLOBAL_METHOD


GLOBAL_METHOD_TYPE = type(G_GLOBAL_METHOD)
GLOBAL_METHOD_FUNCTION_MAP = {}


for fn, fv in GLOBAL_METHOD_TYPE.__dict__.items():
    if fn[0] != '_':
        fn = ''.join([n.title() for n in fn.rsplit('_')])
        cn_fn = re.findall(r'\[ (.*) \]', fv.__doc__)[0]
        GLOBAL_METHOD_FUNCTION_MAP.update({fn:fv})
        GLOBAL_METHOD_FUNCTION_MAP.update({cn_fn:fv})
