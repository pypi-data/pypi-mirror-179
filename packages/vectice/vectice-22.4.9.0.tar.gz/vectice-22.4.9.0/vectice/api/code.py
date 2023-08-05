from __future__ import annotations

import urllib
from typing import Optional, Union
from urllib.parse import urlencode

from .rest_api import RestApi, HttpError
from .json import CodeOutput, Page, PagedResponse
from .project import ProjectApi
from .http_error_handlers import InvalidReferenceError, MissingReferenceError


class CodeApi(RestApi):
    def get_code(
        self,
        code: Union[str, int],
        project: Optional[Union[str, int]] = None,
        workspace: Optional[Union[str, int]] = None,
    ) -> CodeOutput:
        if not isinstance(code, int) and not isinstance(code, str):
            raise InvalidReferenceError("code", code)
        if project is None:
            raise MissingReferenceError("code", "project")
        parent_project = ProjectApi(self.auth).get_project(project, workspace)
        if isinstance(code, int):
            url = f"/metadata/project/{parent_project.id}/code/{code}"
        else:
            url = f"/metadata/project/{parent_project.id}/code/name/{urllib.parse.quote(code)}"
        try:
            response = self.get(url)
            return CodeOutput(response)
        except HttpError as e:
            raise self._httpErrorHandler.handle_get_http_error(e, "code", code)
        except IndexError:
            raise ValueError("The code is invalid. Please check the entered value.")

    # There is No route in the backend to list code
    # Waiting for BE implementation : https://app.shortcut.com/vectice/story/23415/list-code-rest-api
    def list_codes(
        self,
        project: Union[str, int],
        workspace: Optional[Union[str, int]] = None,
        search: Optional[str] = None,
        page_index=Page.index,
        page_size=Page.size,
    ) -> PagedResponse[CodeOutput]:
        if isinstance(project, int):
            url = f"/metadata/project/{project}/code"
        elif isinstance(project, str):
            parent_project = ProjectApi(self.auth).get_project(project, workspace)
            url = f"/metadata/project/{parent_project.id}/code"
        else:
            raise InvalidReferenceError("project", project)
        try:
            queries = {"index": page_index, "size": page_size}
            if search:
                queries["search"] = search
            response = self.get(f"{url}?{urlencode(queries)}")
            result = PagedResponse(
                item_cls=CodeOutput, total=response["total"], page=response["page"], items=response["items"]
            )
            return result
        except HttpError as e:
            raise self._httpErrorHandler.handle_get_http_error(e, "project", project)
