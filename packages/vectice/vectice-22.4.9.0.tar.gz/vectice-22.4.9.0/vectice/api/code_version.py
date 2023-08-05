from __future__ import annotations

from typing import Optional, Union, List
from urllib.parse import urlencode

from .rest_api import RestApi, HttpError
from .code import CodeApi
from .json import Page, PagedResponse, CodeVersionOutput
from .project import ProjectApi
from .http_error_handlers import InvalidReferenceError, MissingReferenceError


class CodeVersionApi(RestApi):
    def get_code_version(
        self,
        version: Union[str, int],
        project: Optional[Union[str, int]] = None,
        workspace: Optional[Union[str, int]] = None,
    ) -> CodeVersionOutput:
        if not isinstance(version, int) and not isinstance(version, str):
            raise ValueError("The code version reference is invalid. Please check the entered value.")
        if isinstance(version, int):
            try:
                url = f"/metadata/codeversion/{version}"
                response = self.get(url)
                return CodeVersionOutput(**response)
            except HttpError as e:
                raise self._httpErrorHandler.handle_get_http_error(e, "code version", version)
            except IndexError:
                raise ValueError("The code version is invalid. Please check the entered value.")
        elif isinstance(version, str):
            if project is None:
                raise MissingReferenceError("project", project)
            code_version_list = self.list_code_versions(project, workspace, version)
            if len(code_version_list) == 1:
                return code_version_list[0]
            else:
                raise ValueError("The code version is invalid. Please check the entered value.")

    def list_code_versions(
        self,
        project: Optional[Union[str, int]] = None,
        workspace: Optional[Union[str, int]] = None,
        search: Optional[str] = None,
        page_index=Page.index,
        page_size=Page.size,
    ) -> List[CodeVersionOutput]:
        if project is None:
            raise InvalidReferenceError("project", project)
        project_output = ProjectApi(self.auth).get_project(project, workspace)
        if search is not None:
            code_list = CodeApi(self.auth).list_codes(project, workspace).list
            for code in code_list:
                url = f"/metadata/project/{project_output.id}/code/{code.id}/version"
                queries = {"index": page_index, "size": page_size}
                if search:
                    queries["search"] = search
                response = self.get(f"{url}?{urlencode(queries)}")
                result = PagedResponse(
                    item_cls=CodeVersionOutput, total=response["total"], page=response["page"], items=response["items"]
                )
                if len(result.list) >= 1:
                    return result.list
            else:
                raise ValueError("The code version was not found.")
        elif search is None:
            results = []
            code_list = CodeApi(self.auth).list_codes(project, workspace).list
            for code in code_list:
                url = f"/metadata/project/{project_output.id}/code/{code.id}/version"
                queries = {"index": page_index, "size": page_size}
                if search:
                    queries["search"] = search
                response = self.get(f"{url}?{urlencode(queries)}")
                result = PagedResponse(
                    item_cls=CodeVersionOutput, total=response["total"], page=response["page"], items=response["items"]
                )
                if len(result.list) >= 1:
                    results += result.list
            return results
