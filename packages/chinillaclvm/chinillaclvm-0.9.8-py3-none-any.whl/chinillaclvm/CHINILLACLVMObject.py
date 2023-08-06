import typing


class CHINILLACLVMObject:
    """
    This class implements the CHINILLACLVM Object protocol in the simplest possible way,
    by just having an "atom" and a "pair" field
    """

    atom: typing.Optional[bytes]

    # this is always a 2-tuple of an object implementing the CHINILLACLVM object
    # protocol.
    pair: typing.Optional[typing.Tuple[typing.Any, typing.Any]]
    __slots__ = ["atom", "pair"]

    def __new__(class_, v):
        if isinstance(v, CHINILLACLVMObject):
            return v
        self = super(CHINILLACLVMObject, class_).__new__(class_)
        if isinstance(v, tuple):
            if len(v) != 2:
                raise ValueError("tuples must be of size 2, cannot create CHINILLACLVMObject from: %s" % str(v))
            self.pair = v
            self.atom = None
        else:
            self.atom = v
            self.pair = None
        return self
