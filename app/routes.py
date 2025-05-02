import logging

from fastapi import APIRouter

from app import service

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/agents")
def create_agent(request, store):
    logger.info("create agent request: %s", request)
    try:
        return service.register_agent(request.agent_id, store)
    except Exception as e:
        logger.exception("create agent failed: %s", e)
        raise


@router.get("/agents/{agent_id}/work")
def get_work(agent_id, store):
    return service.fetch_work(agent_id, store)
