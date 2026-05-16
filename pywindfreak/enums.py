import enum


class ReferenceMode(enum.IntEnum):
    EXTERNAL = 0
    INTERNAL_27MHZ = 1
    INTERNAL_10MHZ = 2
