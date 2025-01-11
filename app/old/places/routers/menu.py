# Маршруты для MenuItem
@router.post("/menu_items/", response_model=MenuItem)
async def create_menu_item_endpoint(
    menu_item: MenuItemCreate,
    db: AsyncSession = Depends(get_session)
):
    return await create_menu_item(db, menu_item)

@router.get("/menu_items/{menu_item_id}", response_model=MenuItem)
async def read_menu_item(
    menu_item_id: int,
    db: AsyncSession = Depends(get_session)
):
    db_menu_item = await get_menu_item(db, menu_item_id)
    if db_menu_item is None:
        raise HTTPException(status_code=404, detail="MenuItem not found")
    return db_menu_item

@router.get("/menu_items/", response_model=List[MenuItem])
async def read_menu_items(
    skip: int = 0, limit: int = 10,
    db: AsyncSession = Depends(get_session)
):
    return await get_menu_items(db, skip, limit)

@router.put("/menu_items/{menu_item_id}", response_model=MenuItem)
async def update_menu_item_endpoint(
    menu_item_id: int, menu_item: MenuItemCreate,
    db: AsyncSession = Depends(get_session)
):
    db_menu_item = await update_menu_item(db, menu_item_id, menu_item)
    if db_menu_item is None:
        raise HTTPException(status_code=404, detail="MenuItem not found")
    return db_menu_item

@router.delete("/menu_items/{menu_item_id}", response_model=MenuItem)
async def delete_menu_item_endpoint(
    menu_item_id: int,
    db: AsyncSession = Depends(get_session)
):
    db_menu_item = await delete_menu_item(db, menu_item_id)
    if db_menu_item is None:
        raise HTTPException(status_code=404, detail="MenuItem not found")
    return db_menu_item



# Маршруты для MenuCategory
@router.post("/menu_categories/", response_model=MenuCategory)
async def create_menu_category_endpoint(
    category: MenuCategoryCreate,
    db: AsyncSession = Depends(get_session)
):
    return await create_menu_category(db, category)

@router.get("/menu_categories/{category_id}", response_model=MenuCategory)
async def read_menu_category(
    category_id: int,
    db: AsyncSession = Depends(get_session)
):
    db_category = await get_menu_category(db, category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="MenuCategory not found")
    return db_category

@router.get("/menu_categories/", response_model=List[MenuCategory])
async def read_menu_categories(
    skip: int = 0, limit: int = 10,
    db: AsyncSession = Depends(get_session)
):
    return await get_menu_categories(db, skip, limit)

@router.put("/menu_categories/{category_id}", response_model=MenuCategory)
async def update_menu_category_endpoint(
    category_id: int, category: MenuCategoryCreate,
    db: AsyncSession = Depends(get_session)
):
    db_category = await update_menu_category(db, category_id, category)
    if db_category is None:
        raise HTTPException(status_code=404, detail="MenuCategory not found")
    return db_category

@router.delete("/menu_categories/{category_id}", response_model=MenuCategory)
async def delete_menu_category_endpoint(
    category_id: int,
    db: AsyncSession = Depends(get_session)
):
    db_category = await delete_menu_category(db, category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="MenuCategory not found")
    return db_category
