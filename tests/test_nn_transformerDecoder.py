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

obj = APIBase("torch.nn.TransformerDecoder")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        decoder_layer = nn.TransformerDecoderLayer(d_model=512, nhead=8)
        transformer_decoder = nn.TransformerDecoder(decoder_layer, num_layers=6)
        memory = torch.rand(10, 32, 512)
        tgt = torch.rand(20, 32, 512)
        result = transformer_decoder(tgt, memory)
        """
    )
    obj.run(
        pytorch_code,
        ["result"],
        unsupport=True,
        reason="doesn't support torch.nn.TransformerDecoderLayer api",
    )


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        decoder_layer = nn.TransformerDecoderLayer(d_model=512, nhead=8)
        transformer_decoder = nn.TransformerDecoder(decoder_layer, 6)
        memory = torch.rand(10, 32, 512)
        tgt = torch.rand(20, 32, 512)
        result = transformer_decoder(tgt, memory)
        """
    )
    obj.run(
        pytorch_code,
        ["result"],
        unsupport=True,
        reason="doesn't support torch.nn.TransformerDecoderLayer api",
    )


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        decoder_layer = nn.TransformerDecoderLayer(d_model=512, nhead=8)
        transformer_decoder = nn.TransformerDecoder(decoder_layer=decoder_layer, num_layers=6)
        memory = torch.rand(10, 32, 512)
        tgt = torch.rand(20, 32, 512)
        result = transformer_decoder(tgt, memory)
        """
    )
    obj.run(
        pytorch_code,
        ["result"],
        unsupport=True,
        reason="doesn't support torch.nn.TransformerDecoderLayer api",
    )
