def zero(*value):
    if value:
        return int(eval('0'+value[0]))
    else:
        return '0'
def one(*value):
    if value:
        return int(eval('1' + value[0]))
    else:
        return '1'
def two(*value):
    if value:
        return int(eval('2' + value[0]))
    else:
        return '2'
def three(*value):
    if value:
        return int(eval('3' + value[0]))
    else:
        return '3'
def four(*value):
    if value:
        return int(eval('4' + value[0]))
    else:
        return '4'
def five(*value):
    if value:
        return int(eval('5' + value[0]))
    else:
        return '5'
def six(*value):
    if value:
        return int(eval('6' + value[0]))
    else:
        return '6'
def seven(*value):
    if value:
        return int(eval('7' + value[0]))
    else:
        return '7'
def eight(*value):
    if value:
        return int(eval('8' + value[0]))
    else:
        return '8'
def nine(*value):
    if value:
        return int(eval('9' + value[0]))
    else:
        return '9'

def plus(value):
    sign = '+'
    return sign+value
def minus(value):
    sign = '-'
    return sign+value
def times(value):
    sign = '*'
    return sign+value
def divided_by(value):
    sign = '/'
    return sign+value