from dataclasses import dataclass
from typing import Callable

from elasticai.creator.resource_utils import read_text
from elasticai.creator.vhdl.language import Code
from elasticai.creator.vhdl.number_representations import (
    FixedPoint,
    fixed_point_params_from_factory,
)
from elasticai.creator.vhdl.templates.utils import expand_template


@dataclass
class FPReLUComponent:
    layer_id: str  # used to distinguish layers in the same model
    fixed_point_factory: Callable[[float], FixedPoint]

    def __post_init__(self) -> None:
        self.data_width, self.frac_width = fixed_point_params_from_factory(
            self.fixed_point_factory
        )

    @property
    def file_name(self) -> str:
        return f"fp_relu_{self.layer_id}.vhd"

    def __call__(self) -> Code:
        template = read_text("elasticai.creator.vhdl.templates", "fp_relu.tpl.vhd")

        code = expand_template(
            template.splitlines(),
            layer_name=self.layer_id,
            data_width=self.data_width,
            clock_option="false",
        )

        yield from code
