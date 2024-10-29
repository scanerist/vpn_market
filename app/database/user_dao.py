from .base import connection
from app.shared.logger import setup_logger
from .models import User
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError


logger = setup_logger(__name__)


@connection
async def set_user(session, user_id: int, number_of_buys: int, number_of_active_keys: int):
    try:
        user = await session.scalar(select(User).filter_by(id=user_id))

        if not user:
            new_user = User(id=user_id, number_of_buys=number_of_buys, number_of_active_keys=number_of_active_keys)
            session.add(new_user)
            await session.commit()
            logger.info(f"User {user_id} created")
        else:
            logger.info(f"User {user_id} was found")
            user.number_of_buys = number_of_buys
            user.number_of_active_keys = number_of_active_keys
        await session.commit()
    except SQLAlchemyError as e:
        logger.error("Error while creating user", exc_info=e)
        await session.rollback()
@connection
async def get_user_by_id(session, user_id: int):
    try:
        user = await session.scalar(select(User).filter_by(id=user_id))
        if not user:
            logger.info(f"User {user_id} not found")
        else:
            logger.info(f"User {user_id} found")
        return user
    except SQLAlchemyError as e:
        logger.error("Error while getting user", exc_info=e)

async def get_all_users(session):
    try:
        users = await session.scalars(select(User))
        return users
    except SQLAlchemyError as e:
        logger.error("Error while getting users", exc_info=e)


async def update_user(session, user_id: int, number_of_buys: int, number_of_active_keys: int):
    try:
        user = await session.scalar(select(User).filter_by(id=user_id))
        if not user:
            logger.info(f"User {user_id} not found")
        else:
            logger.info(f"User {user_id} updated")
            user.number_of_buys = number_of_buys
            user.number_of_active_keys = number_of_active_keys
        session.commit()
    except SQLAlchemyError as e:
        logger.error("Error while updating user", exc_info=e)
        await session.rollback()

async def delete_user(session, user_id: int):
    try:
        user = await session.scalar(select(User).filter_by(id=user_id))
        if not user:
            logger.info(f"User {user_id} not found")
        else:
            logger.info(f"User {user_id} deleted")
            session.delete(user)
        session.commit()
    except SQLAlchemyError as e:
        logger.error("Error while deleting user", exc_info=e)
        await session.rollback()