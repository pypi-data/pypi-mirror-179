from enum import Enum


class FlowModuleValue2Type2IteratorType1Type(str, Enum):
    JAVASCRIPT = "javascript"

    def __str__(self) -> str:
        return str(self.value)
