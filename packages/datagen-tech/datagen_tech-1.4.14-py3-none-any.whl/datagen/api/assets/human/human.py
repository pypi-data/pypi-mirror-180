from pydantic import Field

from datagen.api.assets.base import DatapointRequestAsset
from datagen.api.assets.human.head import Head


class Human(DatapointRequestAsset):
    id: str = Field(title="Human ID", description="Alphanumeric ID of the human")
    head: Head
