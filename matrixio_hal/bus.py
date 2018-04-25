from . import matrixio_cpp_hal
import struct
import signal
import sys

debug = False

# handle SIGTERM as normal sys.exit()
# e.g. docker stop send SIGTERM by default
def sigterm_handler(signal, frame):
    sys.exit()

signal.signal(signal.SIGTERM, sigterm_handler)

bus = matrixio_cpp_hal.PyMatrixIOBus()
bus.Init()

# set some infos about the MCU and FPGA
mcu_data = matrixio_cpp_hal.PyMCUData()
mcu = matrixio_cpp_hal.PyMCUFirmware()
mcu.Setup(bus)
mcu.Read(mcu_data)
MCU_IDENTIFY, MCU_FIRMWARE_VERSION = ['{:x}'.format(d) for d in [mcu_data.ID, mcu_data.version]]
del mcu_data
del mcu

FPGA_IDENTIFY = '{:x}'.format(bus.MatrixName())
FPGA_FIRMWARE_VERSION = '{:x}'.format(bus.MatrixVersion())

MATRIX_DEVICE = 'unknown'
if FPGA_IDENTIFY == '5c344e8':
    MATRIX_DEVICE = 'creator'
elif FPGA_IDENTIFY == '6032bad2':
    MATRIX_DEVICE = 'voice'

# set FPGA_FREQUENCY
FPGA_FREQUENCY = bus.FPGAClock()

