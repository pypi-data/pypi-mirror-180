from myst.client import Client
from myst.openapi.models.model_fit_policy_get import ModelFitPolicyGet


def request_sync(client: Client, project_uuid: str, model_uuid: str, uuid: str) -> ModelFitPolicyGet:
    """Deletes a model fit policy."""

    return client.request(
        method="delete",
        path=f"/projects/{project_uuid}/models/{model_uuid}/fit_policies/{uuid}",
        response_class=ModelFitPolicyGet,
    )
