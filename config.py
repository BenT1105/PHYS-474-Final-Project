import astropy.units as u
import astropy.constants as const
from astropy.cosmology import FlatLambdaCDM

# Cosmology
COSMO = FlatLambdaCDM(H0 = 70, Om0 = 0.3)
C_KMS = const.c.to_value(u.km / u.s)

# Sample cuts
Z_MIN, Z_MAX = 0.002, 0.35
NQ_MIN = 3
LOGM_MIN, LOGM_MAX = 8.0, 10.0

# Pair criteria
RP_MIN, RP_MAX = 5.0, 100.0     # kpc
DV_MAX = 300.0      # km/s
MU_MIN = 0.25

# Control matching
N_CTRL = 5
DZ_TOL = 0.01
DLOGM_TOL = 0.3

# H-alpha
EW_C = 2.5      # Angstrom
LAMBDA_HA = 6564.1     # Angstrom
SN_MIN = 3.0

# sSFR bins
N_BINS = 5