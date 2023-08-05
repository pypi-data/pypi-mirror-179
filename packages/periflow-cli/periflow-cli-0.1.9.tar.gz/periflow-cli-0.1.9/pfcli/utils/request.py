# Copyright (c) 2022-present, FriendliAI Inc. All rights reserved.

"""PeriFlow CLI API Request Utilities"""

from typing import Callable, List, Optional

from requests.exceptions import HTTPError
from requests.models import Response

from pfcli.utils.url import periflow_discuss_url


def decode_http_err(exc: HTTPError) -> str:
    try:
        if exc.response.status_code == 500:
            error_str = f"Internal Server Error: Please contact to system admin via {periflow_discuss_url}"
        elif exc.response.status_code == 404:
            error_str = (
                "Not Found: The requested resource is not found. Please check it again. "
                f"If you cannot find out why this error occurs, please visit {periflow_discuss_url}."
            )
        else:
            response = exc.response
            detail_json = response.json()
            if "detail" in detail_json:
                error_str = f"Error Code: {response.status_code}\nDetail: {detail_json['detail']}"
            elif "error_description" in detail_json:
                error_str = f"Error Code: {response.status_code}\nDetail: {detail_json['error_description']}"
            else:
                error_str = f"Error Code: {response.status_code}"
    except ValueError:
        error_str = exc.response.content.decode()

    return error_str


def paginated_get(
    response_getter: Callable[..., Response], path: Optional[str] = None, **params
) -> List[dict]:
    """Pagination listing"""
    response_dict = response_getter(path=path, params={**params}).json()
    items = response_dict["results"]
    next_cursor = response_dict["next_cursor"]

    while next_cursor is not None:
        response_dict = response_getter(
            path=path, params={**params, "cursor": next_cursor}
        ).json()
        items.extend(response_dict["results"])
        next_cursor = response_dict["next_cursor"]

    return items
