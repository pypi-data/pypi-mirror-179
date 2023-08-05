#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2011
# Brett Alistair Kromkamp - brettkromkamp@gmail.com
# Copyright (C) 2012-2017
# Xiaming Chen - chenxm35@gmail.com
# and other contributors.
# All rights reserved.
#
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
#
# This file contains modifications by Tecton, Inc.
"""
This is a public location to maintain contributed
utilities to extend the basic Tree class.

Deprecated! We prefer a unified processing of Tree object.
"""
from .misc import deprecated


@deprecated(alias='tree.to_graphviz()')
def export_to_dot(tree, filename=None, shape='circle', graph='digraph'):
    """Exports the tree in the dot format of the graphviz software"""
    tree.to_graphviz(filename=filename, shape=shape, graph=graph)
