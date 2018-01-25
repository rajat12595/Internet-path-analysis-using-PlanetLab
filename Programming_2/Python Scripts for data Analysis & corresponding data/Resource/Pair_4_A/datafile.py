import csv

from reportlab.graphics.shapes import String


def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]+','
    except ValueError:
        return ""

def find_between2( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        str=s[start:end]
        str2=str.replace("/", ",")
        return str2+'\n'
    except ValueError:
        return ""
def fun1():
    f = open('Pair_4_A.txt','r').readlines()
    f_date = open('Pair_4_A_new.csv', 'w')
    start = 'Date: '
    end = ' (MM/DD/YYYY),'
    f_date.write("Date,Packet Loss,Min,Avg,Max,Standard_Deviation\n")
    for i,line in enumerate(f):
        f_date.write(find_between(line,"Date: "," (MM/DD/YYYY), Time:")+find_between(line,"received, "," packet loss, time")+find_between2(line,"rtt min/avg/max/mdev = "," ms"))




if __name__ == '__main__':
    fun1()

