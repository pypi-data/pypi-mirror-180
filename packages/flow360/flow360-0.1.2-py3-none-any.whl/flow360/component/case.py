"""
Case component
"""
import math

from pydantic import BaseModel, Extra, Field
from typing import Optional


from flow360.cloud.http_util import http
from flow360.component.flow360_base_model import Flow360BaseModel, Flow360Resource, before_submit_only
from flow360.component.flow360_solver_params import Flow360Params
from flow360.cloud.s3_utils import S3TransferType



class CaseMeta(Flow360BaseModel, extra=Extra.allow):
    """
    Case component
    """

    id: str = Field(alias="caseId")
    case_mesh_id: str = Field(alias="caseMeshId")
    status: str = Field(alias="caseStatus")
    parent_id: str = Field(alias="parentId")



class Case(Flow360Resource):
    """
    Case component
    """

    def __init__(self, id: str = None):
        super().__init__(resource_type="Case",
                         INFO_TYPE_CLASS=CaseMeta,
                         S3_TRANSFER_METHOD=S3TransferType.CASE, 
                         endpoint="cases", id=id)
        if id is not None:
            self.get_info()


    def __str__(self):
        if self._info is not None:
            return self.info.__str__()
        else:
            return 'Case is not yet submitted'

    @before_submit_only
    def submit(self):
        assert self.case_name
        assert self.volume_mesh_id
        assert self.params
        resp = self.post(
            json={
                "name": self.case_name,
                "meshId": self.volume_mesh_id,
                "runtimeParams": self.params.json(),
                "tags": self.tags,
                "parentId": self.parent_id,
            },
            path=f"volumemeshes/{self.volume_mesh_id}/case"
        )
        self._info = CaseMeta(**resp)
        self.init_id(self._info.id)

    @classmethod
    def from_cloud(cls, id: str):
        return cls(id)

    # pylint: disable=too-many-arguments
    @classmethod
    def new(
        cls,
        case_name: str,
        volume_mesh_id: str,
        params: Flow360Params,
        tags: [str] = None,
        parent_id=None,
    ):
        """
        Create case from volume mesh
        :param case_name:
        :param volume_mesh_id:
        :param params:
        :param tags:
        :param parent_id:
        :return:
        """

        assert case_name
        assert volume_mesh_id
        assert params


        new_case = cls()
        new_case.case_name = case_name
        new_case.volume_mesh_id = volume_mesh_id
        new_case.params = params
        new_case.tags = tags
        new_case.parent_id = parent_id

        return new_case

    # pylint: disable=too-many-arguments
    @classmethod
    def submit_multiple_phases(
        cls,
        case_name: str,
        volume_mesh_id: str,
        params: Flow360Params,
        tags: [str] = None,
        phase_steps=1,
    ):
        """
        Create multiple cases from volume mesh
        :param case_name:
        :param volume_mesh_id:
        :param params:
        :param tags:
        :param parent_id:
        :param phase_steps:
        :return:
        """

        assert case_name
        assert volume_mesh_id
        assert params
        assert phase_steps >= 1

        result = []

        total_steps = (
            params.time_stepping.max_physical_steps
            if params.time_stepping and params.time_stepping.max_physical_steps
            else 1
        )

        num_cases = math.ceil(total_steps / phase_steps)
        for i in range(1, num_cases + 1):
            parent_id = result[-1].case_id if result else None
            case = http.post(
                f"volumemeshes/{volume_mesh_id}/case",
                json={
                    "name": f"{case_name}_{i}",
                    "meshId": volume_mesh_id,
                    "runtimeParams": params.json(),
                    "tags": tags,
                    "parentId": parent_id,
                },
            )

            result.append(cls(**case))

        return result
