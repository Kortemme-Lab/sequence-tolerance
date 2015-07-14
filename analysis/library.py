import time
import math
import sys

one_letter_codes={}
one_letter_codes['ALA']='A'
one_letter_codes['CYS']='C'
one_letter_codes['ASP']='D'
one_letter_codes['GLU']='E'
one_letter_codes['PHE']='F'
one_letter_codes['GLY']='G'
one_letter_codes['HIS']='H'
one_letter_codes['ILE']='I'
one_letter_codes['LYS']='K'
one_letter_codes['LEU']='L'
one_letter_codes['MET']='M'
one_letter_codes['ASN']='N'
one_letter_codes['PRO']='P'
one_letter_codes['GLN']='Q'
one_letter_codes['ARG']='R'
one_letter_codes['SER']='S'
one_letter_codes['THR']='T'
one_letter_codes['VAL']='V'
one_letter_codes['TRP']='W'
one_letter_codes['TYR']='Y'

one_letters = set()
for char in one_letter_codes.values():
    one_letters.add(char)

one_letters_list = [item for item in one_letters]
one_letters_list.sort()

three_letter_codes = {}
for key in one_letter_codes.keys():
    val = one_letter_codes[key]
    three_letter_codes[val] = key
three_letter_codes['M'] = 'MET'
three_letter_codes['C'] = 'CYS'
three_letter_codes['T'] = 'THR'

class Reporter:
    def __init__(self, task ,entries='files', print_output=True):
        self.print_output = print_output
        self.start = time.time()
        self.entries = entries
        self.lastreport = self.start
        self.task = task
        self.report_interval = 1 # Interval to print progress (seconds)
        self.n = 0
        self.completion_time = None
        if self.print_output:
            print '\nStarting ' + task
        self.total_count = None # Total tasks to be processed
    def set_total_count(self, x):
        self.total_count = x
    def report(self,n):
        self.n = n
        t = time.time()
        if self.print_output and self.lastreport < (t-self.report_interval):
            self.lastreport = t
            if self.total_count:
                percent_done = float(self.n) / float(self.total_count)
                time_now = time.time()
                est_total_time = (time_now-self.start) * (1.0/percent_done)
                time_remaining = est_total_time - (time_now-self.start)
                minutes_remaining = math.floor(time_remaining/60.0)
                seconds_remaining = int(time_remaining-(60*minutes_remaining))
                sys.stdout.write("  Processed: "+str(n)+" "+self.entries+" (%.1f%%) %02d:%02d\r"%(percent_done*100.0, minutes_remaining, seconds_remaining) )
            else:
                sys.stdout.write("  Processed: "+str(n)+" "+self.entries+"\r" )
            sys.stdout.flush()
    def increment_report(self):
        self.report(self.n+1)
    def increment_report_callback(self, return_value):
        self.report(self.n+1)
    def decrement_report(self):
        self.report(self.n-1)
    def add_to_report(self,x):
        self.report(self.n+x)
    def done(self):
        self.completion_time = time.time()
        if self.print_output:
            print 'Done %s, processed %d %s, took %.3f seconds\n' % (self.task,self.n,self.entries,self.completion_time-self.start)
    def elapsed_time(self):
        if self.completion_time:
            return self.completion_time - self.start
        else:
            return time.time() - self.start
