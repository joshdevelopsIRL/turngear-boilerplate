from django.contrib.auth import login, logout, authenticate
from django.http import HttpRequest, HttpResponse
from ninja import NinjaAPI, Schema
from ninja.security import django_auth
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie


api = NinjaAPI(csrf=True)


class LoginUser(Schema):
    username: str
    password: str


class UserSchema(Schema):
    username: str
    is_authenticated: bool
    email: str | None
    first_name: str | None
    last_name: str | None


class Error(Schema):
    message: str


@api.post("/login", response={200: UserSchema, 403: Error})
def login_user(request: HttpRequest, payload: LoginUser):
    user = authenticate(request, **{
        "username": payload.username,
        "password": payload.password,
    })
    if user is not None:
        login(request, user)
        return user
    return 403, {"message": "invalid credentials"}


@api.post("/logout", auth=django_auth)
def logout_user(request: HttpRequest):
    logout(request)
    return {"success": True}


@api.post("/get-csrf-token")
@ensure_csrf_cookie
@csrf_exempt
def get_csrf_token(request: HttpRequest):
    return HttpResponse()


@api.get("/hello", auth=django_auth)
def hello(request: HttpRequest):
    return {"data": "Hello World", "user": request.user.username}
