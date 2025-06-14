# generated by datamodel-codegen:
#   filename:  v1/operations/config.yaml
#   timestamp: 2025-06-12T09:53:19+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Union
from uuid import UUID

from pydantic import BaseModel, Field

from ..common.common import Connector


class OptType(Enum):
    OPT_INT = 'opt_int'
    OPT_STRING = 'opt_string'
    OPT_BOOL = 'opt_bool'
    OPT_FLOAT = 'opt_float'


class ConfigOpts(BaseModel):
    name: str
    opt_type: OptType
    default_value: Union[str, int, bool, float]
    description: str


class Configuration(BaseModel):
    name: str
    value: Union[str, int, bool, float, Dict[str, Any]]


class InternalConfigMetadata(BaseModel):
    component_id: UUID = Field(..., alias='component-id')
    component_type: Connector = Field(..., alias='component-type')
    opts: List[ConfigOpts]


class InternalConfig(BaseModel):
    configs: List[Configuration]
