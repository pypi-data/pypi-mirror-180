import os
import json
from google.cloud import secretmanager as _secretmanager
from dataverk_vault.api import read_secrets as _read_vault_secrets
from dwh_oppfolging.misc import get_oppfolging_environment, ENV_KNADA_GKE, ENV_KNADA_ONPREM, ENV_VDI


def _get_knada_gke_secrets() -> dict:
    "reads and returns knada gcp secrets as a dict"
    secrets = _secretmanager.SecretManagerServiceClient()
    resource_name = f"{os.environ['KNADA_TEAM_SECRET']}/versions/latest"
    secret = secrets.access_secret_version(name=resource_name)
    data = secret.payload.data.decode("UTF-8") # type: ignore
    return json.loads(data)


def _get_vault_secrets() -> dict:
    """reads and returns vault secrets"""
    data = _read_vault_secrets()
    return json.loads(data)


def _get_vdi_secrets() -> dict:
    """ reads and returns vault secrets"""
    return json.loads(os.environ["VDI_SECRETS"])


def get_secrets() -> dict:
    """reads secrets"""
    env = get_oppfolging_environment()
    if env == ENV_KNADA_GKE:
        return _get_knada_gke_secrets()
    if env == ENV_KNADA_ONPREM:
        return _get_vault_secrets()
    if env == ENV_VDI:
        return _get_vdi_secrets()
    raise Exception("Environment", env, "not supported")