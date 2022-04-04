from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.kyc import Kyc
from app.models.schema.kyc import KycSchemaBase, KycSchema, InKycSchema


class KycRepository(BaseRepository[KycSchemaBase, KycSchema, Kyc]):
    @property
    def _in_schema(self) -> Type[KycSchemaBase]:
        return InKycSchema

    @property
    def _schema(self) -> Type[KycSchema]:
        return KycSchema

    @property
    def _table(self) -> Type[Kyc]:
        return Kyc
