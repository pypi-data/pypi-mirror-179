# Copyright (c) 2021, NVIDIA CORPORATION & AFFILIATES.  All rights reserved.
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

import pynini
from nemo_text_processing.text_normalization.en.graph_utils import NEMO_NOT_QUOTE, GraphFst, delete_space
from pynini.lib import pynutil


class OrdinalFst(GraphFst):
    """
    Finite state transducer for verbalizing ordinal, e.g.
        ordinal { integer: "13" morphosyntactic_features: "o" } -> 13.º
    """

    def __init__(self):
        super().__init__(name="ordinal", kind="verbalize")
        graph = (
            pynutil.delete("integer:")
            + delete_space
            + pynutil.delete("\"")
            + pynini.closure(NEMO_NOT_QUOTE, 1)
            + pynutil.delete("\"")
        )

        replace_suffix = pynini.union(
            pynini.cross(" morphosyntactic_features: \"o\"", ".º"),
            pynini.cross(" morphosyntactic_features: \"a\"", ".ª"),
            pynini.cross(" morphosyntactic_features: \"er\"", ".ᵉʳ"),
        )

        graph = graph + replace_suffix

        delete_tokens = self.delete_tokens(graph)
        self.fst = delete_tokens.optimize()
