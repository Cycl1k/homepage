def bInGbConvert(sourceByte):
    return ("{:.2f}".format(sourceByte/1024/1024/1024))

def bInMbConvert(sourceByte):
    return ("{:.0f}".format(sourceByte/1024/1024))

def percentConvert(percentSource):
    return ("{:.2f}".format(percentSource*100))
