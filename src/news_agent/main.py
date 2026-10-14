import logging

from news_agent.config import get_settings
from news_agent.log import setup_logging

logger = logging.getLogger(__name__)


def main() -> None:
    settings = get_settings()
    setup_logging(settings.log_level)

    logger.info("Starting news agent")
    logger.info("Curator model: %s", settings.curator_model)
    logger.debug("Max stories: %s", settings.max_stories)
