import numpy as np


def adc2mV(bufferADC, range, maxADC):
    """ 
        adc2mc(
                c_short_Array           buffer
                int                     range
                c_int32                  maxADC
                )
               
        Takes a buffer of raw adc count values and converts it into milivolts 
    """

    channelInputRanges = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000]
    vRange = channelInputRanges[range]
    bufferV = [(x * vRange) / maxADC.value for x in bufferADC]

    return bufferV


def splitMSODataPort0(cmaxSamples, bufferMax):
    """
        splitMSODataPort0(
                        c_int32         cmaxSamples
                        c_int16 array   bufferMax
                        )
    """
    # Makes an array for each digital channel
    bufferMaxBinaryD0 = np.chararray(cmaxSamples.value, 1)
    bufferMaxBinaryD1 = np.chararray(cmaxSamples.value, 1)
    bufferMaxBinaryD2 = np.chararray(cmaxSamples.value, 1)
    bufferMaxBinaryD3 = np.chararray(cmaxSamples.value, 1)
    bufferMaxBinaryD4 = np.chararray(cmaxSamples.value, 1)
    bufferMaxBinaryD5 = np.chararray(cmaxSamples.value, 1)
    bufferMaxBinaryD6 = np.chararray(cmaxSamples.value, 1)
    bufferMaxBinaryD7 = np.chararray(cmaxSamples.value, 1)
    
    # Changes the data from int type to a binary type and then seperates the data for each digital channel
    for i in range(0, cmaxSamples.value):
        MSOData = bufferMax[i]
        binaryMSOData = bin(MSOData)
        binaryMSOData = binaryMSOData[2:]
        binaryMSOData=binaryMSOData.zfill(8)
        bufferMaxBinaryD0[i] = binaryMSOData[7]
        bufferMaxBinaryD1[i] = binaryMSOData[6]
        bufferMaxBinaryD2[i] = binaryMSOData[5]
        bufferMaxBinaryD3[i] = binaryMSOData[4]
        bufferMaxBinaryD4[i] = binaryMSOData[3]
        bufferMaxBinaryD5[i] = binaryMSOData[2]
        bufferMaxBinaryD6[i] = binaryMSOData[1]
        bufferMaxBinaryD7[i] = binaryMSOData[0]

    return bufferMaxBinaryD0, bufferMaxBinaryD1, bufferMaxBinaryD2, bufferMaxBinaryD3, bufferMaxBinaryD4, bufferMaxBinaryD5, bufferMaxBinaryD6, bufferMaxBinaryD7

def splitMSODataPort1(cmaxSamples, bufferMax):
    """
        splitMSODataPort1(
                        c_int32         cmaxSamples
                        c_int16 array   bufferMax
                        )
    """
    # Makes an array for each digital channel
    bufferMaxBinaryD8 = np.chararray(cmaxSamples.value, 1)
    bufferMaxBinaryD9 = np.chararray(cmaxSamples.value, 1)
    bufferMaxBinaryD10 = np.chararray(cmaxSamples.value, 1)
    bufferMaxBinaryD11 = np.chararray(cmaxSamples.value, 1)
    bufferMaxBinaryD12 = np.chararray(cmaxSamples.value, 1)
    bufferMaxBinaryD13 = np.chararray(cmaxSamples.value, 1)
    bufferMaxBinaryD14 = np.chararray(cmaxSamples.value, 1)
    bufferMaxBinaryD15 = np.chararray(cmaxSamples.value, 1)
    
    # Changes the data from int type to a binary type and then seperates the data for each digital channel
    for i in range(0, cmaxSamples.value):
        MSOData = bufferMax[i]
        binaryMSOData = bin(MSOData)
        binaryMSOData = binaryMSOData[2:]
        binaryMSOData=binaryMSOData.zfill(8)
        bufferMaxBinaryD8[i] = binaryMSOData[7]
        bufferMaxBinaryD9[i] = binaryMSOData[6]
        bufferMaxBinaryD10[i] = binaryMSOData[5]
        bufferMaxBinaryD11[i] = binaryMSOData[4]
        bufferMaxBinaryD12[i] = binaryMSOData[3]
        bufferMaxBinaryD13[i] = binaryMSOData[2]
        bufferMaxBinaryD14[i] = binaryMSOData[1]
        bufferMaxBinaryD15[i] = binaryMSOData[0]

    return bufferMaxBinaryD8, bufferAMaxBinaryD9, bufferAMaxBinaryD10, bufferAMaxBinaryD11, bufferAMaxBinaryD12, bufferAMaxBinaryD13, bufferAMaxBinaryD14, bufferAMaxBinaryD15