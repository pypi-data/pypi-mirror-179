from __future__ import annotations

import logging
from gql import gql
from typing import List, Optional

from vectice.api.gql_api import GqlApi, Parser
from vectice.api.json.iteration import IterationInput, IterationOutput
from gql.transport.exceptions import TransportQueryError

_logger = logging.getLogger(__name__)

_RETURNS = """id
            index
            status
            phase {
                    id
                    name
                    alias
                    status
                    __typename
              }
            __typename
            """


class IterationApi(GqlApi):
    def list_iterations(self, parent_id: int) -> List[IterationOutput]:
        alias_filter = {"phaseId": parent_id, "search": ""}
        returns = f"""items{{
                                    {_RETURNS}
                        }}"""
        variable_types = "$filters:IterationFiltersInput!"
        kw = "filters:$filters"
        variables = {"filters": alias_filter}
        query = GqlApi.build_query(
            gql_query="getIterationList",
            variable_types=variable_types,
            returns=returns,
            keyword_arguments=kw,
            query=True,
        )
        query_built = gql(query)
        try:
            response = self.execute(query_built, variables)
            iterations_output: List[IterationOutput] = Parser().parse_list(response["getIterationList"]["items"])
            return iterations_output
        except TransportQueryError as e:
            raise self._error_handler.handle_post_gql_error(e, "iteration", "list")

    def get_or_create_iteration(self, phase_id: Optional[int] = None) -> IterationOutput:
        gql_query = "getActiveIterationOrCreateOne"
        variable_types = "$phaseId:Float!"
        variables = {"phaseId": phase_id}
        kw = "phaseId:$phaseId"
        query = GqlApi.build_query(
            gql_query=gql_query, variable_types=variable_types, returns=_RETURNS, keyword_arguments=kw, query=True
        )
        query_built = gql(query)
        try:
            response = self.execute(query_built, variables)
            iteration_output: IterationOutput = Parser().parse_item(response[gql_query])
            return iteration_output
        except TransportQueryError as e:
            raise self._error_handler.handle_post_gql_error(e, "iteration", "get_or_create")

    def get_iteration(self, iteration_id: int) -> IterationOutput:
        gql_query = "getIterationById"
        variable_types = "$id:Float!"
        variables = {"id": iteration_id}
        kw = "id:$id"
        query = GqlApi.build_query(
            gql_query=gql_query, variable_types=variable_types, returns=_RETURNS, keyword_arguments=kw, query=True
        )
        query_built = gql(query)
        try:
            response = self.execute(query_built, variables)
            iteration_output: IterationOutput = Parser().parse_item(response[gql_query])
            return iteration_output
        except TransportQueryError as e:
            raise self._error_handler.handle_get_gql_error(e, "iteration", iteration_id)

    def create_iteration(self, iteration: IterationInput, project_id: int) -> IterationOutput:
        variable_types = "$parentId:Float!,$createModel:iterationInput!"
        kw = "parentId:$parentId,createModel:$createModel"
        variables = {"parentId": project_id, "createModel": iteration}
        query = GqlApi.build_query(
            gql_query="createIteration",
            variable_types=variable_types,
            returns=_RETURNS,
            keyword_arguments=kw,
            query=False,
        )
        query_built = gql(query)
        try:
            response = self.execute(query_built, variables)
            iteration_output: IterationOutput = Parser().parse_item(response["createIteration"])
            return iteration_output
        except TransportQueryError as e:
            raise self._error_handler.handle_post_gql_error(e, "iteration")

    def update_iteration(self, iteration: IterationInput, iteration_id: int) -> IterationOutput:
        variable_types = "$id:Float!,$data:IterationUpdateInput!"
        kw = "id:$id,data:$data"
        variables = {"id": iteration_id, "data": iteration}
        query = GqlApi.build_query(
            gql_query="updateIteration",
            variable_types=variable_types,
            returns=_RETURNS,
            keyword_arguments=kw,
            query=False,
        )
        query_built = gql(query)
        try:
            response = self.execute(query_built, variables)
            iteration_output: IterationOutput = Parser().parse_item(response["updateIteration"])
            return iteration_output
        except TransportQueryError as e:
            raise self._error_handler.handle_post_gql_error(e, "iteration", "put")

    def delete_iteration(self, iteration_id: int) -> None:
        query = gql(
            f"""
            mutation removeIteration {{
                removeIteration(
                    id: {iteration_id}
                )
            }}
            """
        )
        self.execute(query)
