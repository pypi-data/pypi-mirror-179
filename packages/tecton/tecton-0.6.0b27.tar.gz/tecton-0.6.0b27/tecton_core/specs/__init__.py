"""The specs module contains "Tecton object specs", i.e. Python data models for Tecton objects.

Specs provide a unified, frozen (i.e. immutable), and more useful abstraction over args and data protos for use within
the Python SDK.

See the RFC;
https://www.notion.so/tecton/RFC-Unified-SDK-for-Notebook-Driven-Development-a377af9d320f46488ea238e51e2ce656
"""
# nopycln: file
from tecton_core.specs.data_source_spec import *
from tecton_core.specs.entity_spec import *
from tecton_core.specs.transformation_spec import *
