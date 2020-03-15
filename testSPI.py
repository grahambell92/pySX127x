
from   time import sleep
import spidev

spiPort0 = spidev.SpiDev()
spiPort0.open(0,0)
spiPort0.max_speed_hz = 100000

def spiSendRecvOneByte(spiPort, sendByte):
    sendByteArray = [sendByte]
    recvByteArray = spiPort.xfer(sendByteArray)
    return recvByteArray

def repeatSendOneByte(spiPort, sendByte, pauseTimeBetweenBytes, repeatCount):
    print('\nBegin repeatSendByte(),....')
    for i in range(repeatCount):
        spiSendRecvOneByte(spiPort, sendByte)
        sleep(pauseTimeBetweenBytes)
    print('End   repeatSendByte().')
    return

def loopBackOneByte(spiPort, sendByte):
    recvByteArray     = spiSendRecvOneByte(spiPort, sendByte)
    recvByte          = recvByteArray[0]

    print('\nBegin testLoopbackOneByte(),....')
    #print('')
    print('      sendByte  = ', hex(sendByte))
    print('      recvByte  = ', hex(recvByte))
    #print('')
    print('End   testLoopbackOneByte(),....')
    return

def testRepeatSendOneByte():
    repeatSendOneByte(spiPort0, 0x5b, 0.0001, 20000000)
    return

def testLoopbackOneByte():
    loopBackOneByte(spiPort0, 0x5b)
    return

# testRepeatSendOneByte()
testLoopbackOneByte()

''' Smple output tlfong 01 2019apr07hkt2047
Begin testLoopbackOneByte(),....
      sendByte  =  0x5b
      recvByte  =  0x5b
End   testLoopbackOneByte(),....
'''

# *** End ***