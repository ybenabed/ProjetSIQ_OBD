import subprocess


def getSSID():
    ps = subprocess.Popen(['iwgetid'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    try:
        output = subprocess.check_output(('grep', 'ESSID'), stdin=ps.stdout)
        output = str(output)
        output = output.split('\n')[0]
        output = output.split('ESSID:"')[1].split('"')[0]
        return(output)
    except subprocess.CalledProcessError:
        return("")