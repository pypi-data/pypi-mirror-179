# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .container import *
from .get_logs import *
from .get_network import *
from .get_plugin import *
from .get_registry_image import *
from .get_remote_image import *
from .image import *
from .network import *
from .plugin import *
from .provider import *
from .registry_image import *
from .remote_image import *
from .secret import *
from .service import *
from .service_config import *
from .tag import *
from .volume import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_docker.config as __config
    config = __config
else:
    config = _utilities.lazy_import('pulumi_docker.config')

_utilities.register(
    resource_modules="""
[
 {
  "pkg": "docker",
  "mod": "index/container",
  "fqn": "pulumi_docker",
  "classes": {
   "docker:index/container:Container": "Container"
  }
 },
 {
  "pkg": "docker",
  "mod": "index/image",
  "fqn": "pulumi_docker",
  "classes": {
   "docker:index/image:Image": "Image"
  }
 },
 {
  "pkg": "docker",
  "mod": "index/network",
  "fqn": "pulumi_docker",
  "classes": {
   "docker:index/network:Network": "Network"
  }
 },
 {
  "pkg": "docker",
  "mod": "index/plugin",
  "fqn": "pulumi_docker",
  "classes": {
   "docker:index/plugin:Plugin": "Plugin"
  }
 },
 {
  "pkg": "docker",
  "mod": "index/registryImage",
  "fqn": "pulumi_docker",
  "classes": {
   "docker:index/registryImage:RegistryImage": "RegistryImage"
  }
 },
 {
  "pkg": "docker",
  "mod": "index/remoteImage",
  "fqn": "pulumi_docker",
  "classes": {
   "docker:index/remoteImage:RemoteImage": "RemoteImage"
  }
 },
 {
  "pkg": "docker",
  "mod": "index/secret",
  "fqn": "pulumi_docker",
  "classes": {
   "docker:index/secret:Secret": "Secret"
  }
 },
 {
  "pkg": "docker",
  "mod": "index/service",
  "fqn": "pulumi_docker",
  "classes": {
   "docker:index/service:Service": "Service"
  }
 },
 {
  "pkg": "docker",
  "mod": "index/serviceConfig",
  "fqn": "pulumi_docker",
  "classes": {
   "docker:index/serviceConfig:ServiceConfig": "ServiceConfig"
  }
 },
 {
  "pkg": "docker",
  "mod": "index/tag",
  "fqn": "pulumi_docker",
  "classes": {
   "docker:index/tag:Tag": "Tag"
  }
 },
 {
  "pkg": "docker",
  "mod": "index/volume",
  "fqn": "pulumi_docker",
  "classes": {
   "docker:index/volume:Volume": "Volume"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "docker",
  "token": "pulumi:providers:docker",
  "fqn": "pulumi_docker",
  "class": "Provider"
 }
]
"""
)
