from .base import connection
from app.shared.logger import setup_logger
from .models import Key
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError


logger = setup_logger(__name__)


@connection
async def set_key(session, key: str, status: str, user_id: int):
    try:
        new_key = Key(key=key, status=status, user_id=user_id)
        session.add(new_key)
        await session.commit()
        logger.info(f"Key {key} created")
    except SQLAlchemyError as e:
        logger.error("Error while creating key", exc_info=e)
        await session.rollback()


@connection
async def get_key(session, key: str):
    try:
        key = await session.scalar(select(Key).filter_by(key=key))
        if not key:
            logger.info(f"Key {key} not found")
        else:
            logger.info(f"Key {key} found")
        return key
    except SQLAlchemyError as e:
        logger.error("Error while getting key", exc_info=e)


@connection
async def get_all_keys(session):
    try:
        keys = await session.scalars(select(Key))
        return keys
    except SQLAlchemyError as e:
        logger.error("Error while getting keys", exc_info=e)


@connection
async def get_keys_by_user_id(session, user_id: int):
    try:
        keys = await session.scalars(select(Key).filter_by(user_id=user_id))
        return keys
    except SQLAlchemyError as e:
        logger.error("Error while getting keys", exc_info=e)


@connection
async def get_keys_by_status(session, status: str):
    try:
        keys = await session.scalars(select(Key).filter_by(status=status))
        return keys
    except SQLAlchemyError as e:
        logger.error("Error while getting keys", exc_info=e)


@connection
async def delete_key(session, key: str):
    try:
        key = await session.scalar(select(Key).filter_by(key=key))
        if not key:
            logger.info(f"Key {key} not found")
        else:
            logger.info(f"Key {key} was found")
            session.delete(key)
            await session.commit()
    except SQLAlchemyError as e:
        logger.error("Error while deleting key", exc_info=e)
        await session.rollback()