from enum import IntEnum

class MenuItems(IntEnum):
    NONE = -1
    VIEW_METADATA = 0
    UPDATE_METADATA = 1
    EXIT = 2

class MetadataMenuItems(IntEnum):
    COPYRIGHT = 0
    DATE = 1
    DEVICE_MODEL = 2
    ARTIST = 3
    DEVICE_MAKE = 4

class EditMenuItems(IntEnum):
    NONE =  -1
    ADD = 0
    REMOVE = 1
    EXIT = 2

class RemoveMenuItems(IntEnum):
    REMOVE_COPYRIGHT = 0
    REMOVE_ARTIST = 1
    REMOVE_MAKE = 2
    REMOVE_DATETIME = 3

class UpdateMetadata(IntEnum):
    UPDATE_COPYRIGHT = 0
    UPDATE_ARTIST = 1
    UPDATE_MAKE = 2
    UPDATE_DATETIME = 3