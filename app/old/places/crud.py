from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.infrastructure.models.places import (
    Organization, Place, GoogleReviews,
    YandexReviews, Category, Label,
    Image, Video, Service, MenuItem,
    MenuCategory, PlaceHours
)
from app.places.schemas import (
    OrganizationCreate, PlaceCreate, GoogleReviewsCreate,
    YandexReviewsCreate, CategoryCreate, LabelCreate,
    ImageCreate, VideoCreate, ServiceCreate,
    MenuItemCreate, MenuCategoryCreate, PlaceHoursCreate
)



# CRUD operations for Organization
async def create_organization(db: AsyncSession, organization: OrganizationCreate):
    db_organization = Organization(**organization.model_dump())
    db.add(db_organization)
    await db.commit()
    await db.refresh(db_organization)
    return db_organization

async def get_organization(db: AsyncSession, organization_id: int):
    return await db.get(Organization, organization_id)

async def get_organizations(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Organization).offset(skip).limit(limit))
    return result.scalars().all()

async def update_organization(db: AsyncSession, organization_id: int, organization: OrganizationCreate):
    db_organization = await get_organization(db, organization_id)
    if db_organization:
        for key, value in organization.model_dump().items():
            setattr(db_organization, key, value)
        await db.commit()
        await db.refresh(db_organization)
    return db_organization

async def delete_organization(db: AsyncSession, organization_id: int):
    db_organization = await get_organization(db, organization_id)
    if db_organization:
        await db.delete(db_organization)
        await db.commit()
    return db_organization



# CRUD operations for Place
async def create_place(db: AsyncSession, place: PlaceCreate):
    db_place = Place(**place.model_dump())
    db.add(db_place)
    await db.commit()
    await db.refresh(db_place)
    return db_place

async def get_place(db: AsyncSession, place_id: int):
    return await db.get(Place, place_id)

async def get_places(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Place).offset(skip).limit(limit))
    return result.scalars().all()

async def update_place(db: AsyncSession, place_id: int, place: PlaceCreate):
    db_place = await get_place(db, place_id)
    if db_place:
        for key, value in place.model_dump().items():
            setattr(db_place, key, value)
        await db.commit()
        await db.refresh(db_place)
    return db_place

async def delete_place(db: AsyncSession, place_id: int):
    db_place = await get_place(db, place_id)
    if db_place:
        await db.delete(db_place)
        await db.commit()
    return db_place



# CRUD operations for GoogleReviews
async def create_google_review(db: AsyncSession, review: GoogleReviewsCreate):
    db_review = GoogleReviews(**review.model_dump())
    db.add(db_review)
    await db.commit()
    await db.refresh(db_review)
    return db_review

async def get_google_reviews(db: AsyncSession, place_id: int, skip: int = 0, limit: int = 10):
    result = await db.execute(select(GoogleReviews).where(GoogleReviews.place_id == place_id).offset(skip).limit(limit))
    return result.scalars().all()

async def update_google_review(db: AsyncSession, review_id: int, review: GoogleReviewsCreate):
    db_review = await db.get(GoogleReviews, review_id)
    if db_review:
        for key, value in review.model_dump().items():
            setattr(db_review, key, value)
        await db.commit()
        await db.refresh(db_review)
    return db_review

async def delete_google_review(db: AsyncSession, review_id: int):
    db_review = await db.get(GoogleReviews, review_id)
    if db_review:
        await db.delete(db_review)
        await db.commit()
    return db_review



# CRUD operations for GoogleReviews
async def create_google_review(db: AsyncSession, review: GoogleReviewsCreate):
    db_review = GoogleReviews(**review.model_dump())
    db.add(db_review)
    await db.commit()
    await db.refresh(db_review)
    return db_review

async def get_google_review(db: AsyncSession, review_id: int):
    return await db.get(GoogleReviews, review_id)

async def get_google_reviews(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(GoogleReviews).offset(skip).limit(limit))
    return result.scalars().all()

async def update_google_review(db: AsyncSession, review_id: int, review: GoogleReviewsCreate):
    db_review = await get_google_review(db, review_id)
    if db_review:
        for key, value in review.model_dump().items():
            setattr(db_review, key, value)
        await db.commit()
        await db.refresh(db_review)
    return db_review

async def delete_google_review(db: AsyncSession, review_id: int):
    db_review = await get_google_review(db, review_id)
    if db_review:
        await db.delete(db_review)
        await db.commit()
    return db_review



# CRUD operations for YandexReviews
async def create_yandex_review(db: AsyncSession, review: YandexReviewsCreate):
    db_review = YandexReviews(**review.model_dump())
    db.add(db_review)
    await db.commit()
    await db.refresh(db_review)
    return db_review

async def get_yandex_review(db: AsyncSession, review_id: int):
    return await db.get(YandexReviews, review_id)

async def get_yandex_reviews(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(YandexReviews).offset(skip).limit(limit))
    return result.scalars().all()

async def update_yandex_review(db: AsyncSession, review_id: int, review: YandexReviewsCreate):
    db_review = await get_yandex_review(db, review_id)
    if db_review:
        for key, value in review.model_dump().items():
            setattr(db_review, key, value)
        await db.commit()
        await db.refresh(db_review)
    return db_review

async def delete_yandex_review(db: AsyncSession, review_id: int):
    db_review = await get_yandex_review(db, review_id)
    if db_review:
        await db.delete(db_review)
        await db.commit()
    return db_review



# CRUD operations for Category
async def create_category(db: AsyncSession, category: CategoryCreate):
    db_category = Category(**category.model_dump())
    db.add(db_category)
    await db.commit()
    await db.refresh(db_category)
    return db_category

async def get_category(db: AsyncSession, category_id: int):
    return await db.get(Category, category_id)

async def get_categories(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Category).offset(skip).limit(limit))
    return result.scalars().all()

async def update_category(db: AsyncSession, category_id: int, category: CategoryCreate):
    db_category = await get_category(db, category_id)
    if db_category:
        for key, value in category.model_dump().items():
            setattr(db_category, key, value)
        await db.commit()
        await db.refresh(db_category)
    return db_category

async def delete_category(db: AsyncSession, category_id: int):
    db_category = await get_category(db, category_id)
    if db_category:
        await db.delete(db_category)
        await db.commit()
    return db_category



# CRUD operations for Label
async def create_label(db: AsyncSession, label: LabelCreate):
    db_label = Label(**label.model_dump())
    db.add(db_label)
    await db.commit()
    await db.refresh(db_label)
    return db_label

async def get_label(db: AsyncSession, label_id: int):
    return await db.get(Label, label_id)

async def get_labels(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Label).offset(skip).limit(limit))
    return result.scalars().all()

async def update_label(db: AsyncSession, label_id: int, label: LabelCreate):
    db_label = await get_label(db, label_id)
    if db_label:
        for key, value in label.model_dump().items():
            setattr(db_label, key, value)
        await db.commit()
        await db.refresh(db_label)
    return db_label

async def delete_label(db: AsyncSession, label_id: int):
    db_label = await get_label(db, label_id)
    if db_label:
        await db.delete(db_label)
        await db.commit()
    return db_label



# CRUD operations for Image
async def create_image(db: AsyncSession, image: ImageCreate):
    db_image = Image(**image.model_dump())
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
        for key, value in image.model_dump().items():
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



# CRUD operations for Video
async def create_video(db: AsyncSession, video: VideoCreate):
    db_video = Video(**video.model_dump())
    db.add(db_video)
    await db.commit()
    await db.refresh(db_video)
    return db_video

async def get_video(db: AsyncSession, video_id: int):
    return await db.get(Video, video_id)

async def get_videos(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Video).offset(skip).limit(limit))
    return result.scalars().all()

async def update_video(db: AsyncSession, video_id: int, video: VideoCreate):
    db_video = await get_video(db, video_id)
    if db_video:
        for key, value in video.model_dump().items():
            setattr(db_video, key, value)
        await db.commit()
        await db.refresh(db_video)
    return db_video

async def delete_video(db: AsyncSession, video_id: int):
    db_video = await get_video(db, video_id)
    if db_video:
        await db.delete(db_video)
        await db.commit()
    return db_video



# CRUD operations for Service
async def create_service(db: AsyncSession, service: ServiceCreate):
    db_service = Service(**service.model_dump())
    db.add(db_service)
    await db.commit()
    await db.refresh(db_service)
    return db_service

async def get_service(db: AsyncSession, service_id: int):
    return await db.get(Service, service_id)

async def get_services(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Service).offset(skip).limit(limit))
    return result.scalars().all()

async def update_service(db: AsyncSession, service_id: int, service: ServiceCreate):
    db_service = await get_service(db, service_id)
    if db_service:
        for key, value in service.model_dump().items():
            setattr(db_service, key, value)
        await db.commit()
        await db.refresh(db_service)
    return db_service

async def delete_service(db: AsyncSession, service_id: int):
    db_service = await get_service(db, service_id)
    if db_service:
        await db.delete(db_service)
        await db.commit()
    return db_service



# CRUD operations for MenuItem
async def create_menu_item(db: AsyncSession, menu_item: MenuItemCreate):
    db_menu_item = MenuItem(**menu_item.model_dump())
    db.add(db_menu_item)
    await db.commit()
    await db.refresh(db_menu_item)
    return db_menu_item

async def get_menu_item(db: AsyncSession, menu_item_id: int):
    return await db.get(MenuItem, menu_item_id)

async def get_menu_items(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(MenuItem).offset(skip).limit(limit))
    return result.scalars().all()

async def update_menu_item(db: AsyncSession, menu_item_id: int, menu_item: MenuItemCreate):
    db_menu_item = await get_menu_item(db, menu_item_id)
    if db_menu_item:
        for key, value in menu_item.model_dump().items():
            setattr(db_menu_item, key, value)
        await db.commit()
        await db.refresh(db_menu_item)
    return db_menu_item

async def delete_menu_item(db: AsyncSession, menu_item_id: int):
    db_menu_item = await get_menu_item(db, menu_item_id)
    if db_menu_item:
        await db.delete(db_menu_item)
        await db.commit()
    return db_menu_item



# CRUD operations for MenuCategory
async def create_menu_category(db: AsyncSession, category: MenuCategoryCreate):
    db_category = MenuCategory(**category.model_dump())
    db.add(db_category)
    await db.commit()
    await db.refresh(db_category)
    return db_category

async def get_menu_category(db: AsyncSession, category_id: int):
    return await db.get(MenuCategory, category_id)

async def get_menu_categories(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(MenuCategory).offset(skip).limit(limit))
    return result.scalars().all()

async def update_menu_category(db: AsyncSession, category_id: int, category: MenuCategoryCreate):
    db_category = await get_menu_category(db, category_id)
    if db_category:
        for key, value in category.model_dump().items():
            setattr(db_category, key, value)
        await db.commit()
        await db.refresh(db_category)
    return db_category

async def delete_menu_category(db: AsyncSession, category_id: int):
    db_category = await get_menu_category(db, category_id)
    if db_category:
        await db.delete(db_category)
        await db.commit()
    return db_category



# CRUD operations for PlaceHours
async def create_place_hours(db: AsyncSession, place_hours: PlaceHoursCreate):
    db_place_hours = PlaceHours(**place_hours.model_dump())
    db.add(db_place_hours)
    await db.commit()
    await db.refresh(db_place_hours)
    return db_place_hours

async def get_place_hours(db: AsyncSession, place_hours_id: int):
    return await db.get(PlaceHours, place_hours_id)

async def get_place_hours_list(db: AsyncSession, business_id: int, skip: int = 0, limit: int = 10):
    result = await db.execute(select(PlaceHours).where(PlaceHours.business_id == business_id).offset(skip).limit(limit))
    return result.scalars().all()

async def update_place_hours(db: AsyncSession, place_hours_id: int, place_hours: PlaceHoursCreate):
    db_place_hours = await get_place_hours(db, place_hours_id)
    if db_place_hours:
        for key, value in place_hours.model_dump().items():
            setattr(db_place_hours, key, value)
        await db.commit()
        await db.refresh(db_place_hours)
    return db_place_hours

async def delete_place_hours(db: AsyncSession, place_hours_id: int):
    db_place_hours = await get_place_hours(db, place_hours_id)
    if db_place_hours:
        await db.delete(db_place_hours)
        await db.commit()
    return db_place_hours