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
名称常量

"""


# --------------------------------------------------------------------------
class DirName:
    """
    [ 目录名称常量 ]
    
    """

    EngineeringData     = 'EngineeringData'
    """ 工程数据目录 """

    EngineeringLogs     = 'Logs'
    """ 工程日志目录 """

    EngineeringProjects = 'Projects'
    """ 项目目录 """

    EngineeringBaseCode = 'BaseCode'
    """ 工程底层编码目录 """


# --------------------------------------------------------------------------
class FileName:
    """
    [ 文件名称常量 ]
    
    """

    EngineeringInit     = 'AwakenEngineering.ini'
    """ 工程INI文件 """

    EngineeringConfig   = 'AwakenConfig.yaml'
    """ 工程配置文件 """

    EngineeringDatabase = 'AwakenDatabase.db'
    """ 工程数据库文件 """

    ProjectInit         = 'AwakenProject.ini'
    """ 项目INI文件 """
