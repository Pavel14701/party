from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.infrastructure.models.chats import Chat, Group, Message, History, Image
from app.chats.schemas import (
    ChatCreate, ChatRead,
    GroupCreate, GroupRead,
    MessageCreate, MessageReadFull,
    HistoryCreate, HistoryReadFull,
    ImageCreate, ImageReadFull
)

# CRUD operations for Chat
async def create_chat(db: AsyncSession, chat: ChatCreate):
    db_chat = Chat(**chat.dict())
    db.add(db_chat)
    await db.commit()
    await db.refresh(db_chat)
    return db_chat

async def get_chat(db: AsyncSession, chat_id: int):
    return await db.get(Chat, chat_id)

async def get_chats(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Chat).offset(skip).limit(limit))
    return result.scalars().all()

async def update_chat(db: AsyncSession, chat_id: int, chat: ChatCreate):
    db_chat = await get_chat(db, chat_id)
    if db_chat:
        for key, value in chat.dict().items():
            setattr(db_chat, key, value)
        await db.commit()
        await db.refresh(db_chat)
    return db_chat

async def delete_chat(db: AsyncSession, chat_id: int):
    db_chat = await get_chat(db, chat_id)
    if db_chat:
        await db.delete(db_chat)
        await db.commit()
    return db_chat

# CRUD operations for Group
async def create_group(db: AsyncSession, group: GroupCreate):
    db_group = Group(**group.dict())
    db.add(db_group)
    await db.commit()
    await db.refresh(db_group)
    return db_group

async def get_group(db: AsyncSession, group_id: int):
    return await db.get(Group, group_id)

async def get_groups(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Group).offset(skip).limit(limit))
    return result.scalars().all()

async def update_group(db: AsyncSession, group_id: int, group: GroupCreate):
    db_group = await get_group(db, group_id)
    if db_group:
        for key, value in group.dict().items():
            setattr(db_group, key, value)
        await db.commit()
        await db.refresh(db_group)
    return db_group

async def delete_group(db: AsyncSession, group_id: int):
    db_group = await get_group(db, group_id)
    if db_group:
        await db.delete(db_group)
        await db.commit()
    return db_group

# CRUD operations for Message
async def create_message(db: AsyncSession, message: MessageCreate):
    db_message = Message(**message.dict())
    db.add(db_message)
    await db.commit()
    await db.refresh(db_message)
    return db_message

async def get_message(db: AsyncSession, message_id: int):
    return await db.get(Message, message_id)

async def get_messages(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Message).offset(skip).limit(limit))
    return result.scalars().all()

async def update_message(db: AsyncSession, message_id: int, message: MessageCreate):
    db_message = await get_message(db, message_id)
    if db_message:
        for key, value in message.dict().items():
            setattr(db_message, key, value)
        await db.commit()
        await db.refresh(db_message)
    return db_message

async def delete_message(db: AsyncSession, message_id: int):
    db_message = await get_message(db, message_id)
    if db_message:
        await db.delete(db_message)
        await db.commit()
    return db_message

# CRUD operations for History
async def create_history(db: AsyncSession, history: HistoryCreate):
    db_history = History(**history.dict())
    db.add(db_history)
    await db.commit()
    await db.refresh(db_history)
    return db_history

async def get_history(db: AsyncSession, history_id: int):
    return await db.get(History, history_id)

async def get_histories(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(History).offset(skip).limit(limit))
    return result.scalars().all()

async def update_history(db: AsyncSession, history_id: int, history: HistoryCreate):
    db_history = await get_history(db, history_id)
    if db_history:
        for key, value in history.dict().items():
            setattr(db_history, key, value)
        await db.commit()
        await db.refresh(db_history)
    return db_history

async def delete_history(db: AsyncSession, history_id: int):
    db_history = await get_history(db, history_id)
    if db_history:
        await db.delete(db_history)
        await db.commit()
    return db_history

# CRUD operations for Image
async def create_image(db: AsyncSession, image: ImageCreate):
    db_image = Image(**image.dict())
    db.add(db_image)
    await db.commit()
    await db.refresh(db_image)
    return db_image

async def get_image(db: AsyncSession, image_id: int):
    return await db.get(Image, image_id)

async def get_images(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Image).offset(skip).limit(limit))
    return result.scalars().all()

async def update_image(db: AsyncSession, image_id: int, image: ImageCreate):
    db_image = await get_image(db, image_id)
    if db_image:
        for key, value in image.dict().items():
            setattr(db_image, key, value)
        await db.commit()
        await db.refresh(db_image)
    return db_image

async def delete_image(db: AsyncSession, image_id: int):
    db_image = await get_image(db, image_id)
    if db_image:
        await db.delete(db_image)
        await db.commit()
    return db_image
