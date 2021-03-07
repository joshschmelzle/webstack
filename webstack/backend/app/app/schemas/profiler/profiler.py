from typing import List, Union

from pydantic import BaseModel, Field


class Profile(BaseModel):
    mac: str = Field(example="fe-7b-4b-69-26-bb")
    is_laa: bool = Field(example=True)
    manuf: Union[str, None] = Field(example=None)
    band: int = Field(example=5)
    channel: int = Field(example=36)
    dot11k: int = Field(example=1)
    dot11r: int = Field(example=0)
    dot11v: int = Field(example=1)
    dot11w: int = Field(example=1)
    dot11n: int = Field(example=1)
    dot11n_ss: int = Field(example=2)
    dot11ac: int = Field(example=1)
    dot11ac_ss: int = Field(example=2)
    dot11ac_su_bf: int = Field(example=0)
    dot11ac_mu_bf: int = Field(example=0)
    dot11ax: int = Field(example=1)
    dot11ax_ss: int = Field(example=2)
    dot11ax_su_bf: int = Field(example=0)
    max_power: int = Field(example=14)
    min_power: int = Field(example=0)
    supported_channels: List = Field(
        example=[
            36,
            40,
            44,
            48,
            149,
            153,
            157,
            161,
            165,
        ]
    )


class Profiles(BaseModel):
    profiles: List[Profile]
