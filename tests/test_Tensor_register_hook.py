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

obj = APIBase("torch.Tensor.register_hook")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        v = torch.tensor([0., 0., 0.], requires_grad=True)
        h = v.register_hook(lambda grad: grad * 2)  # double the gradient
        v.backward(torch.tensor([1., 2., 3.]))
        result = torch.tensor(v.grad)
        """
    )
    obj.run(pytorch_code, ["result"])
