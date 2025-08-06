from typing import Annotated

import torch
from typing_extensions import Generic, TypeVarTuple

T = TypeVarTuple("T")


class Tensor(Generic[*T], torch.Tensor):  # type: ignore
    pass


N = Annotated[int, "n"]
D = Annotated[int, "d"]

