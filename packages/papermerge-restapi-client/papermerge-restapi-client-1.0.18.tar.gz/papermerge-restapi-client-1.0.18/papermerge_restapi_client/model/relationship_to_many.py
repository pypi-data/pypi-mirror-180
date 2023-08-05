# coding: utf-8

"""
    Papermerge REST API

    Document management system designed for digital archives  # noqa: E501

    The version of the OpenAPI document: 2.1.0b21
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from papermerge_restapi_client import schemas  # noqa: F401


class RelationshipToMany(
    schemas.ListSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    An array of objects each containing the 'type' and 'id' for to-many relationships
    """


    class MetaOapg:
        unique_items = True
        
        @staticmethod
        def items() -> typing.Type['Linkage']:
            return Linkage

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['Linkage'], typing.List['Linkage']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'RelationshipToMany':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'Linkage':
        return super().__getitem__(i)

from papermerge_restapi_client.model.linkage import Linkage
