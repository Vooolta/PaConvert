# Copyright (c) 2023 PaddlePaddle Authors. All Rights Reserved.
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

import textwrap

from apibase import APIBase

obj = APIBase("torch.Tensor.sort")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.tensor([[4, 9], [23, 2]])
        result = a.sort()
        if isinstance(result, tuple):
            result = result[0]
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.tensor([[4, 9], [23, 2]])
        result = a.sort(0)
        if isinstance(result, tuple):
            result = result[0]
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.tensor([[4, 9], [23, 2]])
        result = a.sort(dim=1, descending=True, stable=True)
        if isinstance(result, tuple):
            result = result[0]
        """
    )
    obj.run(
        pytorch_code, ["result"], unsupport=True, reason="unsupprt stable parameter"
    )


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        descending=False
        a = torch.tensor([[4, 9], [23, 2]])
        result = a.sort(dim=1, descending=descending)
        if isinstance(result, tuple):
            result = result[0]
        """
    )
    obj.run(pytorch_code, ["result"])
