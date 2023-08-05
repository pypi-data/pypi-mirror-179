from __future__ import annotations

import urllib
from typing import Optional, Union, Dict, Any, List
from urllib.parse import urlencode

from .rest_api import RestApi, HttpError
from ._utils import read_nodejs_date
from .dataset import DatasetApi
from .json import DatasetVersionOutput, DatasetVersionInput, Page, PagedResponse, FileMetadata
from .json.property import PropertyOutput
from .http_error_handlers import MissingReferenceError


class DatasetVersionApi(RestApi):
    def get_dataset_version(
        self,
        version: Union[str, int],
        dataset: Optional[Union[str, int]] = None,
        project: Optional[Union[str, int]] = None,
        workspace: Optional[Union[str, int]] = None,
    ) -> DatasetVersionOutput:
        if not isinstance(version, int) and not isinstance(version, str):
            raise ValueError("The dataset version reference is invalid. Please check the entered value.")
        if isinstance(version, int):
            url = f"/metadata/datasetversion/{version}"
        else:
            if dataset is None:
                raise MissingReferenceError("dataset version", "dataset")
            parent_dataset = DatasetApi(self.auth).get_dataset(dataset, project, workspace)
            url = f"/metadata/project/{parent_dataset.project.id}/dataset/{parent_dataset.id}/version/name/{urllib.parse.quote(version)}"
        try:
            response = self.get(url)
            return DatasetVersionOutput(**response)
        except HttpError as e:
            raise self._httpErrorHandler.handle_get_http_error(e, "dataset version", version)
        except IndexError:
            raise ValueError("The dataset version is invalid. Please check the entered value.")

    def create_dataset_version(
        self,
        data: DatasetVersionInput,
        dataset: Union[str, int],
        project: Optional[Union[str, int]] = None,
        workspace: Optional[Union[str, int]] = None,
    ) -> DatasetVersionOutput:
        parent_dataset = DatasetApi(self.auth).get_dataset(dataset, project, workspace)
        try:
            data["datasetId"] = parent_dataset.id
            url = "/metadata/datasetversion"
            if "autoVersion" in data and data["autoVersion"]:
                url += "?autoVersion=true"
            response = self.post(url, data)
            return DatasetVersionOutput(**response["version"], reusedVersion=response["reusedVersion"])
        except HttpError as e:
            raise self._httpErrorHandler.handle_post_http_error(e, "dataset version")
        except IndexError:
            raise ValueError("The dataset version is invalid. Please check the entered value.")

    def update_dataset_version(
        self,
        data: DatasetVersionOutput,
        version: Union[str, int],
        dataset: Optional[Union[str, int]] = None,
        project: Optional[Union[str, int]] = None,
        workspace: Optional[Union[str, int]] = None,
    ) -> DatasetVersionOutput:
        dataset_version_object = self.get_dataset_version(version, dataset, project, workspace)
        url = f"/metadata/datasetversion/{dataset_version_object.id}"
        try:
            response = self.put(url, data)
            return DatasetVersionOutput(**response)
        except HttpError as e:
            raise self._httpErrorHandler.handle_put_http_error(e, "dataset version", version)
        except IndexError:
            raise ValueError("The dataset version is invalid. Please check the entered value.")

    def list_dataset_versions(
        self,
        dataset: Union[str, int],
        workspace: Optional[Union[str, int]] = None,
        project: Optional[Union[str, int]] = None,
        search: Optional[str] = None,
        page_index=Page.index,
        page_size=Page.size,
    ) -> PagedResponse[DatasetVersionOutput]:
        parent_dataset = DatasetApi(self.auth).get_dataset(dataset, project, workspace)
        url = f"/metadata/project/{parent_dataset.project.id}/dataset/{parent_dataset.id}/version"
        queries = {"index": page_index, "size": page_size}
        if search:
            queries["search"] = search
        dataset_versions = self.get(url + "?" + urlencode(queries))
        return PagedResponse(
            item_cls=DatasetVersionOutput,
            total=dataset_versions["total"],
            page=dataset_versions["page"],
            items=dataset_versions["items"],
        )

    def delete_dataset_version(
        self,
        version: Union[str, int],
        dataset: Optional[Union[str, int]] = None,
        project: Optional[Union[str, int]] = None,
        workspace: Optional[Union[str, int]] = None,
    ):
        try:
            dataset_version = self.get_dataset_version(version, dataset, project, workspace)
            self.delete(f"/metadata/datasetversion/{dataset_version.id}")
        except HttpError as e:
            raise self._httpErrorHandler.handle_get_http_error(e, "dataset version", version)

    def list_files_metadata(
        self,
        version: Union[str, int],
        dataset: Optional[Union[str, int]] = None,
        project: Optional[Union[str, int]] = None,
        workspace: Optional[Union[str, int]] = None,
    ) -> List[FileMetadata]:
        try:
            dataset_version = self.get_dataset_version(version, dataset, project, workspace)
            response = self.get(
                f"/metadata/project/{dataset_version.dataset['project']['id']}/dataset/{dataset_version.dataset_id}/version/{dataset_version.id}/versionFolder"
            )
            return [
                FileMetadata(
                    name=item["name"],
                    id=item["id"],
                    path=item["path"]["path"],
                    type=item["type"],
                    isFolder=item["path"]["isFolder"],
                    children=[] if "children" not in item else item["children"],
                    size=int(item["size"]),
                    uri=item["uri"],
                    itemCreatedDate=read_nodejs_date(item["itemCreatedDate"]),
                    itemUpdatedDate=item["itemUpdatedDate"],
                )
                for item in response["files"]
            ]
        except HttpError as e:
            raise self._httpErrorHandler.handle_get_http_error(e, "version folder", "dataset version " + str(version))

    def create_dataset_version_properties(
        self,
        version: Union[str, int],
        properties: Dict[str, Any],
        dataset: Optional[Union[str, int]] = None,
        project: Optional[Union[str, int]] = None,
        workspace: Optional[Union[str, int]] = None,
    ):
        dataset_version = self.get_dataset_version(version, dataset, project, workspace)
        url = f"/metadata/project/{dataset_version.dataset.project.id}/dataset/{dataset_version.dataset.id}/version/{dataset_version.id}"
        if isinstance(properties, dict):
            self.post(f"{url}/entityProperty/", properties)
        parent_dataset_version = self.get_dataset_version(version, dataset, project, workspace)
        return parent_dataset_version

    def update_dataset_version_properties(
        self,
        version: Union[str, int],
        property_id: int,
        properties: Dict[str, Any],
        dataset: Optional[Union[str, int]] = None,
        project: Optional[Union[str, int]] = None,
        workspace: Optional[Union[str, int]] = None,
    ):
        dataset_version = self.get_dataset_version(version, dataset, project, workspace)
        url = f"/metadata/project/{dataset_version.dataset.project.id}/dataset/{dataset_version.dataset.id}/version/{dataset_version.id}"
        self.put(url + f"/entityProperty/{property_id}", properties)

    def list_dataset_version_properties(
        self,
        version: Union[str, int],
        dataset: Optional[Union[str, int]] = None,
        project: Optional[Union[str, int]] = None,
        workspace: Optional[Union[str, int]] = None,
        page_index=Page.index,
        page_size=Page.size,
    ) -> PagedResponse[PropertyOutput]:
        dataset_version = self.get_dataset_version(version, dataset, project, workspace)
        url = f"/metadata/project/{dataset_version.dataset.project.id}/dataset/{dataset_version.dataset.id}/version/{dataset_version.id}"
        queries = {"index": page_index, "size": page_size}
        model_version_properties = self.get(url + "/entityProperty?" + urlencode(queries))
        properties = [PropertyOutput.from_dict(property).as_dict() for property in model_version_properties["items"]]
        return PagedResponse(
            item_cls=PropertyOutput,
            total=model_version_properties["total"],
            page=model_version_properties["page"],
            items=properties,
        )
