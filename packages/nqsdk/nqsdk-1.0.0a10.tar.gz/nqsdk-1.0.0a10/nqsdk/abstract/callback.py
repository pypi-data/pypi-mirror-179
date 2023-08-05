"""
Copyright (c) 2022 Inqana Ltd.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Optional

from nqsdk.enums import CallbackStatus

if TYPE_CHECKING:  # pragma: no cover
    from .message import SentMeta


class CallbackResponse(ABC):

    DEFAULT_CODE_OK = 204
    DEFAULT_CODE_ERROR = 400
    DEFAULT_CODE_NOT_IMPLEMENTED = 501

    @property
    @abstractmethod
    def status(self) -> CallbackStatus:
        pass

    @property
    @abstractmethod
    def meta(self) -> Optional[SentMeta]:
        pass

    @property
    @abstractmethod
    def error(self) -> Optional[str]:
        pass

    @property
    def code_ok(self) -> int:
        return CallbackResponse.DEFAULT_CODE_OK

    @property
    def code_error(self) -> int:
        return CallbackResponse.DEFAULT_CODE_ERROR

    def get_code(self) -> int:
        """HTTP status code."""

        if self.status == CallbackStatus.OK:
            return self.code_ok
        else:
            return self.code_error

    def get_content_type(self) -> Optional[str]:
        """Content type header value, e.g. `application/json`."""
        return None

    def get_content(self) -> Optional[str]:
        """Content as a string."""
        return None
