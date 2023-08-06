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
命令行指令 - 运行服务器

"""
from ..baseic.const import G_CONST
from ..baseic.common.template_rendering import G_TEMPLATE_RENDERING
from ..core.perform.perform_server import PerformServer


# --------------------------------------------------------------------------
def instruction_running_server(argv: list):
    """
    [ 命令行指令 - 运行服务器 ]

    ---
    参数
    - argv : { list } - 参数列表。

    """
    if not G_CONST.Path.FilePath.EngineeringInit.exists():
        G_TEMPLATE_RENDERING.render_print(
            title='Awaken - 运行服务器',
            is_show_number=False,
            source=[
                '当前运行路径不是工程根目录;',
                '请在工程根目录执行该命令.'
            ],
        )
        exit(0)

    port: int = 3700
    if len(argv) >= 1:
        try:
            port = int(argv[0])
        except ValueError:
            G_TEMPLATE_RENDERING.render_print(
                title='Awaken - 运行服务器',
                is_show_number=False,
                source=[
                    '运行服务器指令的端口参数必须为数字 !'
                ],
            )
            exit(0)

    G_TEMPLATE_RENDERING.render_print(
        title='Awaken - 运行服务器',
        is_show_number=False,
        source=[
            f'服务器正在运行 >> 端口号 :: [ {port} ] !'
        ],
    )
    perform_server = PerformServer()
    perform_server.running(port)
