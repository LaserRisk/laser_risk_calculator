from collections import namedtuple


LaserCoeffs = namedtuple('LaserCoeffs', ['C0', 'C1', 'C2'])


continuous_laser_coeffs = LaserCoeffs(1, 2, 3)
