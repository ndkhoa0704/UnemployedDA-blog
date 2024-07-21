from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi.requests import Request


class OAuth2PasswordCookie(OAuth2PasswordBearer):
    """OAuth2 password flow with token in a httpOnly cookie."""

    def __init__(self, *args, token_name: str = None, **kwargs):
        super().__init__(*args, **kwargs)
        self._token_name = token_name or "client-token"

    @property
    def token_name(self) -> str:
        """Get the name of the token's cookie."""
        return self._token_name

    async def __call__(self, request: Request) -> str:
        """Extract and return a JWT from the request cookies.

        Raises:
            HTTPException: 403 error if no token cookie is present.
        """
        token = request.cookies.get(self._token_name)
        print(token)
        if not token:
            raise HTTPException(status_code=403, detail="Not authenticated")
        return token


oauth2_scheme = OAuth2PasswordCookie(
    tokenUrl="token",
    scopes={"article:create": "create article", "article:read": "read article"},
)