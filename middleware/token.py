import jwt
from datetime import datetime, timedelta
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from fastapi import Request, HTTPException, FastAPI


SECRECT_KEY = 'HEHUAISEN'
ALGORITHM = 'HS256'
expires_delta = timedelta(minutes=15)

def create_access_token(data: dict, expires_delta: timedelta = expires_delta) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({'exp': expire.isoformat()})
    encoded_jwt = jwt.encode(to_encode, SECRECT_KEY, algorithm=ALGORITHM)
    return encoded_jwt

class TokenMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI, skip_paths: list[str]=None):
        super().__init__(app)
        self.secret_key = SECRECT_KEY
        self.algorithm = ALGORITHM
        self.skip_paths = skip_paths or []
    async def dispatch(self, request: Request, call_next):
        if any(request.url.path.startswith(prefix) for prefix in self.skip_paths): # 对应前缀的路径跳过该中间件
            return await call_next(request)

        token = request.headers.get('Authorization')
        if not token:
            raise HTTPException(status_code=401,  detail="Authorization header missing")
        try:
            payload = self.verify_token(token)
            request.state.user = payload
        except Exception as e:
            raise HTTPException(status_code=401, detail="Invalid Token")

        response = await call_next(request)
        return response

    def verify_token(self, token: str) -> bool:
        if token.startswith('Bearer '):
            token = token[7:]
        return jwt.decode(token, self.secret_key, self.algorithm)
