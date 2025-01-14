from http import HTTPStatus

from dishka.integrations.base import FromDishka as Depends
from dishka.integrations.fastapi import inject
from fastapi import APIRouter, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from app.applications.auth.interactors import AuthentificatorInteractor, CreateAccessTokenInteractor
from app.controllers.schemas import TokenSchema, RefreshTokenSchema

class HttpAuthController:
    router = APIRouter(prefix='/auth')

    @router.post("/token", response_model=TokenSchema)
    @inject
    async def auth(self, form_data: Depends[OAuth2PasswordRequestForm], login_interactor: Depends[AuthentificatorInteractor],):
        user_dm = await login_interactor(form_data.username, form_data.password)
        if not user_dm:
            raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, detail="Incorrect username or password")
        access_token = await login_interactor({"sub": user_dm.username})
        return {"access_token": access_token, "token_type": "bearer"}

    @router.post("/refresh", response_model=RefreshTokenSchema)
    @inject
    async def refresh_token(
        self,
        refresh_token: str,
        token_interactor: Depends[CreateAccessTokenInteractor],
    ):
        if new_token := token_interactor(refresh_token):
            return {"access_token": new_token, "token_type": "bearer"}
        else:
            raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, detail="Invalid or expired refresh token")
