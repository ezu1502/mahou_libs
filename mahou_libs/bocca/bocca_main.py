import logging
from typing_extensions import Self
from ..colors import painted_string, COLORS
from typing import Any


class BoccaFiglia:
    def __new__(cls, name: str, color: str | COLORS = "#FAFAFA") -> Self:
        if BoccaDellaVerita.master_exists:
            instance = object.__new__(cls)
            return instance
        else:
            raise RuntimeError("Cannot make BoccaFiglia if there isn't a BoccaDellaVerita instance")

    def __init__(self, name: str, color: str | COLORS = "#FAFAFA"):
        self.logger = logging.getLogger(painted_string(name, color))

    def __getattr__(self, attr_name) -> Any:
        return getattr(self.logger, attr_name)

    def add_local_level(self, level_name: str, level_priority: int):
        return add_level(self, level_name, level_priority)

    
class BoccaDellaVerita:
    master_exists = False

    def __new__(cls) -> Self:
        if cls.master_exists:
            raise RuntimeError("There is already one instance of BoccaDellaVerita, only one allowed")
        else:
            instance = object.__new__(cls)
            return instance 

    def __init__(self):
        self.set_default_levels()
        BoccaDellaVerita.master_exists = True
        

    def configure(self):
        logging.basicConfig(
        level = logging.DEBUG, 
        format = "%(levelname)-5s |  %(message)-30s -> CAST BY: \033[96m%(name)s\033[0m"
        )


    def set_default_levels(self):
        self.TIMETRACKING = add_level(BoccaFiglia, "TIMETRACKING", 11)
        self.TRACE = add_level(BoccaFiglia, "TRACE", 5)

    def see_all_levels(self):
        levels_dict = logging.getLevelNamesMapping()
        return levels_dict


def add_level(target, level_name: str, level_priority: int):         
    upper_name = level_name.upper()
    method_name = level_name.lower()

    if hasattr(target, method_name):
        raise ValueError(f"Level {upper_name}, method {method_name} -  already exists!")

    logging.addLevelName(level_priority, upper_name)


    def class_log_at_level(daughter_instance, message: str, *args, **kwargs):
        if daughter_instance.logger.isEnabledFor(level_priority):
            daughter_instance.logger.log(
                level_priority,
                message,
                *args,
                **kwargs
            )

    def instance_log_at_level(message: str, *args, **kwargs):
        if target.logger.isEnabledFor(level_priority):
            target.logger.log(
                level_priority,
                message,
                *args,
                **kwargs
            )


    if isinstance(target, BoccaFiglia):    
        setattr(target, method_name, instance_log_at_level)
    elif target is BoccaFiglia:
        setattr(target, method_name, class_log_at_level)
    else:
        raise TypeError("Object should be BoccaFiglia or an instance of Boccafiglia")
    return level_priority

