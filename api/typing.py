"""Typing module for api."""
import typing

from flask_sqlalchemy.extension import _FSAModel  # noqa WPS450

ModelType: typing.TypeAlias = typing.Type[_FSAModel]
