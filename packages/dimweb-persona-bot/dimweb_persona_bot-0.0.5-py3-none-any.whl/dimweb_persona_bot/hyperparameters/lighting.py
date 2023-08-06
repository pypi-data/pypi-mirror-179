from dataclasses import dataclass
from typing import Optional, List


@dataclass
class H1LightingHyperparametersV1:
    precision: int = 32
    accumulate_grad_batches: int = 1
    gradient_clip_val: float = 1.0
    auto_scale_batch_size: Optional[str] = None
    # profiler: str = "simple"
    deterministic: bool = True
    max_epochs: int = 1
    devices: List = None
