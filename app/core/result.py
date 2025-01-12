from enum import Enum
from typing import Generic, Optional, TypeVar, Union

from pydantic import BaseModel

T = TypeVar("T")


class ResultStatus(str, Enum):
    SUCCESS = "success"
    FAILURE = "failure"


class ResultBase(BaseModel):
    status: ResultStatus


class Success(ResultBase, Generic[T]):
    status: ResultStatus = ResultStatus.SUCCESS
    data: Optional[T] = None


class Failure(ResultBase):
    status: ResultStatus = ResultStatus.FAILURE
    message: str = "An error occurred"


Result = Union[Success[T], Failure]
