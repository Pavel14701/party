from dishka import Provider, Scope
from dishka import make_container
from app.services.my_service import MyService

service_provider = Provider(scope=Scope.REQUEST)
service_provider.provide(MyService)

container = make_container(service_provider)
