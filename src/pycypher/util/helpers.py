"""Place for functions that might be used across the project."""

import datetime
import queue
import uuid
from pathlib import Path
from typing import Any, Generator, Optional, Type
from urllib.parse import ParseResult, urlparse

from pycypher.etl.message_types import EndOfData
from pycypher.util.config import (  # pylint: disable=no-name-in-module
    INNER_QUEUE_TIMEOUT,
    OUTER_QUEUE_TIMEOUT,
)
from pycypher.util.logger import LOGGER


def ensure_uri(uri: str | ParseResult | Path) -> ParseResult:
    """
    Ensure that the URI is parsed.

    Args:
        uri: The URI to ensure is parsed

    Returns:
        The URI as a ``ParseResult``
    """
    if isinstance(uri, ParseResult):
        pass
    elif isinstance(uri, str):
        uri = urlparse(uri)
    elif isinstance(uri, Path):
        uri = urlparse(uri.as_uri())
    else:
        raise ValueError(
            f"URI must be a string or ParseResult, not {type(uri)}"
        )
    LOGGER.debug("URI converted: %s", uri)
    return uri


class QueueGenerator:  # pylint: disable=too-few-public-methods,too-many-instance-attributes
    """A queue that also generates items."""

    def __init__(
        self,
        *args,
        inner_queue_timeout: Optional[int] = INNER_QUEUE_TIMEOUT,
        end_of_queue_cls: Optional[Type] = EndOfData,
        outer_queue_timeout: Optional[int] = OUTER_QUEUE_TIMEOUT,
        name: Optional[str] = uuid.uuid4().hex,
        goldberg: Optional["Goldberg"] = None,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.queue = queue.Queue()
        self.inner_queue_timeout = inner_queue_timeout
        self.end_of_queue_cls = end_of_queue_cls
        self.counter: int = 0
        self.outer_queue_timeout = outer_queue_timeout
        self.no_more_items = False  # ever
        self.exit_code = None
        self.name = name
        self.goldberg = goldberg

        if self.goldberg:
            self.goldberg.queue_list.append(self)

    def yield_items(self) -> Generator[Any, None, None]:
        """Generate items."""
        last_time = datetime.datetime.now()
        running = True
        exit_code = 0
        while running:
            while True:
                if (
                    datetime.datetime.now() - last_time
                ).total_seconds() > self.outer_queue_timeout:
                    running = False
                    exit_code = 1
                    break

                try:
                    item = self.get(timeout=self.inner_queue_timeout)
                except queue.Empty:
                    break
                if isinstance(item, self.end_of_queue_cls):
                    running = False
                    break
                self.counter += 1
                last_time = datetime.datetime.now()
                yield item
        self.no_more_items = True
        if exit_code == 1:
            LOGGER.warning("Exiting generator due to timeout")
        elif exit_code == 0:
            LOGGER.warning("Exiting generator normally")
        self.exit_code = exit_code

    @property
    def completed(self) -> bool:
        """Is the queue completed? Has ``EndOfData`` been received?"""
        return self.no_more_items

    def empty(self) -> bool:
        """Is the queue empty?"""
        return self.queue.empty

    def get(self, **kwargs) -> Any:
        """Get an item from the queue."""
        return self.queue.get(**kwargs)

    def put(self, item: Any) -> None:
        """Put an item on the queue."""
        self.queue.put(item)
