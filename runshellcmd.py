'''run shell cmd'''
def run_cmd(cmd):
    print 'cmd:'
    print cmd
    sp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = sp.communicate()
    print output
    if output is not None:
        output = output.strip()
    # print error
    if sp.returncode != 0:
        print error
    #sys.exit(-1)
    return output
    
