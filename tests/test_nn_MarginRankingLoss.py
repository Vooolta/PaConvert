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

obj = APIBase("torch.nn.MarginRankingLoss")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.Tensor([[1, 2], [3, 4]]).type(torch.float32)
        other = torch.Tensor([[2, 1], [2, 4]]).type(torch.float32)
        label = torch.Tensor([[1, -1], [-1, -1]]).type(torch.float32)
        margin_rank_loss = torch.nn.MarginRankingLoss()
        result = margin_rank_loss(input, other, label)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.Tensor([[1, 2], [3, 4]]).type(torch.float32)
        other = torch.Tensor([[2, 1], [2, 4]]).type(torch.float32)
        label = torch.Tensor([[1, -1], [-1, -1]]).type(torch.float32)
        margin_rank_loss = torch.nn.MarginRankingLoss(0.5, True, False, reduction='mean')
        result = margin_rank_loss(input, other, label)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.Tensor([[1, 2], [3, 4]]).type(torch.float32)
        other = torch.Tensor([[2, 1], [2, 4]]).type(torch.float32)
        label = torch.Tensor([[1, -1], [-1, -1]]).type(torch.float32)
        margin_rank_loss = torch.nn.MarginRankingLoss(0.7, reduce=False, size_average=False, reduction='mean')
        result = margin_rank_loss(input, other, label)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.Tensor([[1, 2], [3, 4]]).type(torch.float32)
        other = torch.Tensor([[2, 1], [2, 4]]).type(torch.float32)
        label = torch.Tensor([[1, -1], [-1, -1]]).type(torch.float32)
        margin_rank_loss = torch.nn.MarginRankingLoss(0.7, reduce=False, size_average=False, reduction='mean')
        result = margin_rank_loss(input, other, label)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.Tensor([[1, 2], [3, 4]]).type(torch.float32)
        other = torch.Tensor([[2, 1], [2, 4]]).type(torch.float32)
        label = torch.Tensor([[1, -1], [-1, -1]]).type(torch.float32)
        margin_rank_loss = torch.nn.MarginRankingLoss(0.7, reduce=False, size_average=False, reduction='mean')
        result = margin_rank_loss(input, other, label)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_6():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.Tensor([[1, 2], [3, 4]]).type(torch.float32)
        other = torch.Tensor([[2, 1], [2, 4]]).type(torch.float32)
        label = torch.Tensor([[1, -1], [-1, -1]]).type(torch.float32)
        margin_rank_loss = torch.nn.MarginRankingLoss(0.7, reduce=False, size_average=False, reduction='mean')
        result = margin_rank_loss(input, other, label)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_7():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.Tensor([[1, 2], [3, 4]]).type(torch.float32)
        other = torch.Tensor([[2, 1], [2, 4]]).type(torch.float32)
        label = torch.Tensor([[1, -1], [-1, -1]]).type(torch.float32)
        margin_rank_loss = torch.nn.MarginRankingLoss(0.7, reduce=False, size_average=True, reduction='mean')
        result = margin_rank_loss(input, other, label)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_8():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.Tensor([[1, 2], [3, 4]]).type(torch.float32)
        other = torch.Tensor([[2, 1], [2, 4]]).type(torch.float32)
        label = torch.Tensor([[1, -1], [-1, -1]]).type(torch.float32)
        margin_rank_loss = torch.nn.MarginRankingLoss(0.7, reduce=True, size_average=True, reduction='mean')
        result = margin_rank_loss(input, other, label)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_9():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.Tensor([[1, 2], [3, 4]]).type(torch.float32)
        other = torch.Tensor([[2, 1], [2, 4]]).type(torch.float32)
        label = torch.Tensor([[1, -1], [-1, -1]]).type(torch.float32)
        margin_rank_loss = torch.nn.MarginRankingLoss(0.7, reduce=False, size_average=False, reduction='sum')
        result = margin_rank_loss(input, other, label)
        """
    )
    obj.run(pytorch_code, ["result"])
