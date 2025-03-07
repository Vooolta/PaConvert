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

obj = APIBase("torch.nn.functional.local_response_norm")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn.functional as F
        x = torch.tensor([[[[-1.2392, -0.1310, -0.6679,  0.5476],
                            [ 1.1738, -1.7384, -0.7733,  0.3261],
                            [-0.0926, -1.0448, -1.2557, -1.5503],
                            [ 0.6402,  0.9072,  0.6780, -1.9885]],

                            [[ 0.0639, -1.1592,  1.4242, -0.4641],
                            [-0.1920,  0.1826,  1.9217, -0.4359],
                            [ 1.1926, -0.0247,  0.4744, -1.0216],
                            [-0.0360, -1.1656,  0.3661, -1.8147]],

                            [[-0.3582,  0.7141,  0.8222, -0.0466],
                            [-0.1383, -0.6718, -1.4062,  0.3552],
                            [-0.8480,  1.1629,  0.5633,  0.4056],
                            [ 1.5017,  1.1490, -0.7503, -0.1636]],

                            [[ 0.6353,  0.4463, -2.0130,  0.2581],
                            [-0.2878, -0.9019,  0.7903,  1.6045],
                            [-0.9478, -0.8246,  0.3295,  1.7501],
                            [-0.4648,  1.5492, -0.8700, -0.7079]]]])
        result = F.local_response_norm(x, 2)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn.functional as F
        x = torch.tensor([[[[-1.2392, -0.1310, -0.6679,  0.5476],
                            [ 1.1738, -1.7384, -0.7733,  0.3261],
                            [-0.0926, -1.0448, -1.2557, -1.5503],
                            [ 0.6402,  0.9072,  0.6780, -1.9885]],

                            [[ 0.0639, -1.1592,  1.4242, -0.4641],
                            [-0.1920,  0.1826,  1.9217, -0.4359],
                            [ 1.1926, -0.0247,  0.4744, -1.0216],
                            [-0.0360, -1.1656,  0.3661, -1.8147]],

                            [[-0.3582,  0.7141,  0.8222, -0.0466],
                            [-0.1383, -0.6718, -1.4062,  0.3552],
                            [-0.8480,  1.1629,  0.5633,  0.4056],
                            [ 1.5017,  1.1490, -0.7503, -0.1636]],

                            [[ 0.6353,  0.4463, -2.0130,  0.2581],
                            [-0.2878, -0.9019,  0.7903,  1.6045],
                            [-0.9478, -0.8246,  0.3295,  1.7501],
                            [-0.4648,  1.5492, -0.8700, -0.7079]]]])
        result = F.local_response_norm(x, 2, alpha=1e-4, beta=0.75, k=1.)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn.functional as F
        x = torch.tensor([[[[-1.2392, -0.1310, -0.6679,  0.5476],
                            [ 1.1738, -1.7384, -0.7733,  0.3261],
                            [-0.0926, -1.0448, -1.2557, -1.5503],
                            [ 0.6402,  0.9072,  0.6780, -1.9885]],

                            [[ 0.0639, -1.1592,  1.4242, -0.4641],
                            [-0.1920,  0.1826,  1.9217, -0.4359],
                            [ 1.1926, -0.0247,  0.4744, -1.0216],
                            [-0.0360, -1.1656,  0.3661, -1.8147]],

                            [[-0.3582,  0.7141,  0.8222, -0.0466],
                            [-0.1383, -0.6718, -1.4062,  0.3552],
                            [-0.8480,  1.1629,  0.5633,  0.4056],
                            [ 1.5017,  1.1490, -0.7503, -0.1636]],

                            [[ 0.6353,  0.4463, -2.0130,  0.2581],
                            [-0.2878, -0.9019,  0.7903,  1.6045],
                            [-0.9478, -0.8246,  0.3295,  1.7501],
                            [-0.4648,  1.5492, -0.8700, -0.7079]]]])
        result = F.local_response_norm(input=x, size=2, alpha=1e-4, beta=0.75, k=2.)
        """
    )
    obj.run(pytorch_code, ["result"])
