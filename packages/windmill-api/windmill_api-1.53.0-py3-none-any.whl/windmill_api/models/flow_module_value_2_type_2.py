from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.flow_module_value_2_type_2_iterator_type_0 import FlowModuleValue2Type2IteratorType0
from ..models.flow_module_value_2_type_2_iterator_type_1 import FlowModuleValue2Type2IteratorType1
from ..models.flow_module_value_2_type_2_modules_item import FlowModuleValue2Type2ModulesItem
from ..models.flow_module_value_2_type_2_type import FlowModuleValue2Type2Type
from ..types import UNSET, Unset

T = TypeVar("T", bound="FlowModuleValue2Type2")


@attr.s(auto_attribs=True)
class FlowModuleValue2Type2:
    """
    Attributes:
        modules (List[FlowModuleValue2Type2ModulesItem]):
        iterator (Union[FlowModuleValue2Type2IteratorType0, FlowModuleValue2Type2IteratorType1]):
        skip_failures (bool):
        type (FlowModuleValue2Type2Type):
        parallel (Union[Unset, bool]):
    """

    modules: List[FlowModuleValue2Type2ModulesItem]
    iterator: Union[FlowModuleValue2Type2IteratorType0, FlowModuleValue2Type2IteratorType1]
    skip_failures: bool
    type: FlowModuleValue2Type2Type
    parallel: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        modules = []
        for modules_item_data in self.modules:
            modules_item = modules_item_data.to_dict()

            modules.append(modules_item)

        iterator: Dict[str, Any]

        if isinstance(self.iterator, FlowModuleValue2Type2IteratorType0):
            iterator = self.iterator.to_dict()

        else:
            iterator = self.iterator.to_dict()

        skip_failures = self.skip_failures
        type = self.type.value

        parallel = self.parallel

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "modules": modules,
                "iterator": iterator,
                "skip_failures": skip_failures,
                "type": type,
            }
        )
        if parallel is not UNSET:
            field_dict["parallel"] = parallel

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        modules = []
        _modules = d.pop("modules")
        for modules_item_data in _modules:
            modules_item = FlowModuleValue2Type2ModulesItem.from_dict(modules_item_data)

            modules.append(modules_item)

        def _parse_iterator(
            data: object,
        ) -> Union[FlowModuleValue2Type2IteratorType0, FlowModuleValue2Type2IteratorType1]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                iterator_type_0 = FlowModuleValue2Type2IteratorType0.from_dict(data)

                return iterator_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            iterator_type_1 = FlowModuleValue2Type2IteratorType1.from_dict(data)

            return iterator_type_1

        iterator = _parse_iterator(d.pop("iterator"))

        skip_failures = d.pop("skip_failures")

        type = FlowModuleValue2Type2Type(d.pop("type"))

        parallel = d.pop("parallel", UNSET)

        flow_module_value_2_type_2 = cls(
            modules=modules,
            iterator=iterator,
            skip_failures=skip_failures,
            type=type,
            parallel=parallel,
        )

        flow_module_value_2_type_2.additional_properties = d
        return flow_module_value_2_type_2

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
