from dataclasses import dataclass, field, fields
from typing import Union, Optional, List, Tuple


from pymodaq_utils.enums import BaseEnum, enum_checker
from pymodaq_data import Q_


class LaserType(BaseEnum):
    Continuous = 0
    Pulsed = 1


@dataclass
class Laser:
    """Class for describing a laser and its properties."""

    name: str
    laser_type: Optional[LaserType] = None
    pulse_duration: Optional[Union[Q_, str]] = field(default_factory=Q_)
    wavelength: Optional[Union[Q_, str]] = field(default_factory=Q_)

    field_titles: Tuple[str] = field(default=('Name', 'Laser type', 'Pulse Duration', 'Wavelength'),
                                    init=False, repr=False)

    def __post_init__(self):
        self.laser_type = enum_checker(LaserType, self.laser_type)
        self.pulse_duration = Q_(self.pulse_duration)
        self.wavelength = Q_(self.wavelength)


if __name__ == '__main__':

    laser = Laser('my big laser', laser_type=LaserType.Continuous,
                  pulse_duration='100fs', wavelength='515nm')

    pass
