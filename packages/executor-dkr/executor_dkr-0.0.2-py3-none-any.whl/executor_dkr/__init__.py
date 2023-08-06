import logging
from pkg_resources import get_distribution, DistributionNotFound
from executor_dkr._config import DAG_NAME, DAG_VERSION
try:
    __version__ = get_distribution("executor-dkr").version
except DistributionNotFound:
    __version__ = 'local'


logger = logging.getLogger(__name__)


def build(dag, resource):
    fn = dag.load(DAG_NAME, DAG_VERSION)
    return fn(resource)
