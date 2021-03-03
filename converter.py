import numpy as np
import sys

# Constants
rho_c=1.8
rho_si=3.01
# Inputs
fcM=np.float(sys.argv[1])
porosity=np.float(sys.argv[2])


# Derived quantities
fsiM=1-fcM
fcV=(1-rho_c/rho_si*(1-fcM**-1))**-1
fsiV=1-fcV



# Converting to ProDiMo quantities
FsiV=(1-porosity)*((fcV/fsiV+1)**-1)
FcV=(fcV/fsiV)*FsiV

print(FsiV,FcV)
print(FsiV+FcV+porosity)
print(fcV/fsiV)
print(FcV/FsiV)



