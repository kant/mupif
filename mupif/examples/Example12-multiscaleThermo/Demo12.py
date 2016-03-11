import sys
sys.path.append('../../..')
from mupif import *
from mupif import logger
#Import module Example10/demoapp.py
sys.path.append('../Example10')
import demoapp

#Read geometry and boundary condition for the microscale
thermalMicro = demoapp.thermal('thermalMicro.in','')
logger.info(thermalMicro.getApplicationSignature())
#Solve the microscale problem
thermalMicro.solveStep(None)
#Get effective conductivity from the microscale
effConductivity = thermalMicro.getProperty(PropertyID.PID_effective_conductivity,0.0)
logger.info('Computed effective conductivity from microscale: %f' % effConductivity.value)

#Dump microscale results to VTK files
thermalMicroField = thermalMicro.getField(FieldID.FID_Material_number, 0.0)
thermalMicroField.field2VTKData().tofile('thermalMicroMaterial')
thermalMicroField = thermalMicro.getField(FieldID.FID_Temperature, 0.0)
thermalMicroField.field2VTKData().tofile('thermalMicroT')

#Read geometry and boundary condition for the macroscale
thermalMacro = demoapp.thermal('thermalMacro.in','')
#Assign effective conductivity for the whole macroscale domain
thermalMacro.setProperty(effConductivity)
thermalMacro.solveStep(None)
thermalMacroField = thermalMacro.getField(FieldID.FID_Temperature, 0.0)

#Dump macroscale results to VTK files
thermalMacroField.field2VTKData().tofile('thermalMacroT')