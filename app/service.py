import logging

logger = logging.getLogger(__name__)


def register_agent(agent_id, store):
    try:
        return store.save(agent_id)
    except Exception:
        logger.exception("failed to register agent %s", agent_id)
        raise


def fetch_work(agent_id, store):
    logger.info("Entering fetch_work")
    work = store.next(agent_id)
    logger.info("Exiting fetch_work")
    return work


def audit_register(agent: dict) -> None:
    """Log the full agent payload for registration audit."""
    logger.info("agent registration audit: %s", agent)
    logger.info("agent capabilities: %s", agent.get("capabilities", {}))
    logger.info("agent metadata: %s", agent.get("metadata", {}))
