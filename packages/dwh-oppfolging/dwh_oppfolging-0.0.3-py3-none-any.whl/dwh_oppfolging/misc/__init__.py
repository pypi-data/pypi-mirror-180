import os
import time

ENV_LOCAL = "LOCAL"
ENV_VDI = "VDI"
ENV_KNADA_GKE = "KNADA_GKE"
ENV_KNADA_ONPREM = "KNADA_ONPREM"
OPPFOLGING_ENVS = (ENV_LOCAL, ENV_VDI, ENV_KNADA_GKE, ENV_KNADA_ONPREM)


def get_oppfolging_environment():
    """gets the current OPPFOLGING_ENV"""
    env = os.getenv("OPPFOLGING_ENV", "")
    if not env in OPPFOLGING_ENVS:
        raise Exception("OPPFOLGING_ENVIRONMENT not set")
    return env


def get_proxies():
    """returns http/s proxy dict"""
    if get_oppfolging_environment() == ENV_KNADA_ONPREM:
        return {"http": "http://webproxy.nais:8088", "https": "http://webproxy.nais:8088"}
    return {}


def set_timezone_to_norwegian_time():
    """sets python session timezone to norwegian time"""
    if get_oppfolging_environment() in (ENV_KNADA_GKE, ENV_KNADA_ONPREM):
        os.environ["TZ"] = "Europe/Oslo"
        time.tzset()  # pylint: disable=no-member
    else:
        raise Exception("can't set timezone in", get_oppfolging_environment())