from pydantic import BaseModel, constr


class UserInfo(BaseModel):
    user_id: constr(strict=True, min_length=1)
    tenant_name: constr(strict=True, min_length=1)
    tenant_id: constr(strict=True, min_length=1)
