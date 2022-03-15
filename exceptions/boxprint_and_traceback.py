import traceback

def boxprint(symbol, height, width):

    if len(symbol)!=1:
        raise Exception('Symbol is not a single character')
    if width<=2:
        raise Exception('The width of the box must be more than 2')
    if height<=2:
        raise Exception('the height should be more than 2')
    print(symbol*width)
    for i in range(height-2):
        print(symbol+ (' '*(width-2)) +symbol)
    print(symbol*width)


for sym, height, width in (('*', 4,4), ('0',20,30),('x',12,1),('name',11,23)):
        try:
            boxprint(sym,height,width)
        except Exception as err:
            print('An exception occured  '+str(err))
            report=open('error_log.txt','a')
            report.write(traceback.format_exc())
            report.close()
            print('The exception has been written to except file')