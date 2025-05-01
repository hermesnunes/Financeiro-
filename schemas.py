from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import date, datetime

from models.models import StatusPagamento, StatusRecebimento, MeioPagamento

# --- Schemas Base --- 
class ContaBase(BaseModel):
    valor: float
    descricao: Optional[str] = None
    meio_pagamento: MeioPagamento
    comprovante: Optional[str] = None

# --- Schemas de Contas a Receber --- 
class ContaReceberBase(ContaBase):
    data_prevista: date
    origem: str
    cliente: str
    conta_recebimento: Optional[str] = None
    status: StatusRecebimento = StatusRecebimento.PENDENTE

class ContaReceberCreate(ContaReceberBase):
    pass

class ContaReceberUpdate(BaseModel):
    valor: Optional[float] = None
    data_prevista: Optional[date] = None
    data_recebimento: Optional[date] = None
    origem: Optional[str] = None
    cliente: Optional[str] = None
    descricao: Optional[str] = None
    meio_pagamento: Optional[MeioPagamento] = None
    conta_recebimento: Optional[str] = None
    status: Optional[StatusRecebimento] = None
    comprovante: Optional[str] = None

class ContaReceber(ContaReceberBase):
    id: int
    data_recebimento: Optional[date] = None
    data_criacao: datetime
    data_atualizacao: datetime

    class Config:
        from_attributes = True

# --- Schemas de Contas a Pagar --- 
class ContaPagarBase(ContaBase):
    data_vencimento: date
    destino: str
    conta_pagamento: Optional[str] = None
    status: StatusPagamento = StatusPagamento.PENDENTE

class ContaPagarCreate(ContaPagarBase):
    pass

class ContaPagarUpdate(BaseModel):
    valor: Optional[float] = None
    data_vencimento: Optional[date] = None
    data_pagamento: Optional[date] = None
    destino: Optional[str] = None
    descricao: Optional[str] = None
    meio_pagamento: Optional[MeioPagamento] = None
    conta_pagamento: Optional[str] = None
    status: Optional[StatusPagamento] = None
    comprovante: Optional[str] = None

class ContaPagar(ContaPagarBase):
    id: int
    data_pagamento: Optional[date] = None
    data_criacao: datetime
    data_atualizacao: datetime

    class Config:
        from_attributes = True

# --- Schemas de Autenticação --- 
class UserBase(BaseModel):
    username: str
    email: Optional[EmailStr] = None

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None

class User(UserBase):
    id: int
    is_active: bool
    data_criacao: datetime

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

