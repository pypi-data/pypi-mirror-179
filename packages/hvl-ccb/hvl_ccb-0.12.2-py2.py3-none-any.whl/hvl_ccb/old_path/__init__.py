import logging
import warnings

logger = logging.getLogger(__name__)

msg = "Do not use this old thing! It will be removed!!"
warnings.warn(msg)
logger.error(msg)

from hvl_ccb.new_path import MyCustomClass  # noqa: F401, E402
