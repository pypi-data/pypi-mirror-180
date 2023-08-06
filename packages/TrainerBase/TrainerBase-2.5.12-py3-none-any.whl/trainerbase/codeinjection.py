import uuid

import typing
import trainerbase.memory


class CodeInjection:
    DPG_TAG_PREFIX = "injection__"

    def __init__(
        self,
        address: typing.Union[trainerbase.memory.Address, int],
        code_to_inject: bytes,
    ):
        self.address = trainerbase.memory.make_address(address)
        self.code_to_inject = code_to_inject
        self.original_code = trainerbase.memory.pm.read_bytes(self.address.resolve(), len(self.code_to_inject))
        self.dpg_tag = f"{CodeInjection.DPG_TAG_PREFIX}{uuid.uuid4()}"

    def inject(self):
        trainerbase.memory.pm.write_bytes(self.address.resolve(), self.code_to_inject, len(self.code_to_inject))

    def eject(self):
        trainerbase.memory.pm.write_bytes(self.address.resolve(), self.original_code, len(self.original_code))
