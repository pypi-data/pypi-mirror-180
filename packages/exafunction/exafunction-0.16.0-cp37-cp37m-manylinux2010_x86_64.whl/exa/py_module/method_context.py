# Copyright Exafunction, Inc.

import pickle
from typing import Sequence

import numpy as np

import exa._C as _C
from exa.common_pb.common_pb2 import ValueMetadata
from exa.py_value.value import Value
from exa.types import Picklable
from exa.types import ValueLike


class MethodContext:
    def __init__(self, c: _C.MethodContext):
        self._c = c

    def module_context(self):
        return self._c.module_context()

    def _allocate_value(
        self,
        is_cuda: bool,
        metadata: ValueMetadata,
    ) -> Value:
        ser_metadata = b""
        if metadata is not None:
            ser_metadata = metadata.SerializeToString()
        c_val = self._c.allocate_value(is_cuda, ser_metadata)
        return Value(c_val)

    def from_bytes(self, val: bytes) -> Value:
        metadata = ValueMetadata()
        metadata.size = len(val)
        metadata.bytes.SetInParent()
        v = self._allocate_value(False, metadata)
        v.set_bytes(val)
        return v

    def _allocate_numpy(
        self,
        dtype: np.dtype,
        shape: Sequence[int],
    ) -> Value:
        metadata = Value._get_tensor_metadata(dtype, shape)
        v = self._allocate_value(False, metadata)
        return v

    def from_numpy(self, val: np.ndarray) -> Value:
        v = self._allocate_numpy(val.dtype, val.shape)
        v.numpy()[:] = val
        return v

    def from_picklable(self, val: Picklable) -> Value:
        pickled_val = pickle.dumps(val)
        metadata = ValueMetadata()
        metadata.size = len(pickled_val)
        metadata.picklable.SetInParent()
        v = self._allocate_value(False, metadata)
        v.set_bytes(pickled_val)
        return v

    def convert_to_value(self, val: ValueLike) -> Value:
        if isinstance(val, Value):
            return val
        if isinstance(val, np.ndarray):
            return self.from_numpy(val)
        if isinstance(val, bytes):
            return self.from_bytes(val)
        try:
            return self.from_picklable(val)
        except pickle.PicklingError as e:
            raise ValueError(f"Cannot convert {type(val)} to Value") from e
