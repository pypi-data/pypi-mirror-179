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
状态常量

"""


# --------------------------------------------------------------------------
class Project:
    """
    [ 项目状态常量 ]

    """
    Null = '未知'
    """ 未知 """


# --------------------------------------------------------------------------
class Result:
    """
    [ 结果常量 ]

    """
    Null      = '未知'
    """ 未知 """

    Success   = '成功'
    """ 成功 """

    Unsuccess = '失败'
    """ 失败 """

    Error     = '异常'
    """ 异常 """


# --------------------------------------------------------------------------
class Switch:
    """
    [ 开关常量 ]

    """
    Null = '未知'
    """ 未知 """

    Off  = '关'
    """ 关 """

    On   = '开'
    """ 开 """


# --------------------------------------------------------------------------
class RunProcess:
    """
    [ 运行过程常量 ]

    """
    Null  = '未知'
    """ 未知 """
    
    Start = '开始'
    """ 开始 """

    End   = '结束'
    """ 结束 """
