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


def monitor_health(agents: list) -> None:
    """Continuously monitor agent health."""
    import time
    while True:
        for agent in agents:
            try:
                status = fetch_work(agent["id"])
                logger.info("agent health: %s status: %s", agent, status)
            except Exception as exc:
                logger.error("health check failed for agent %s: %s", agent, exc)
                logger.error("agent dump: %s", agent)
        time.sleep(5)
