def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]+'\n'
    except ValueError:
        return ""

def fun1():
    f = open('Pair_6_B_traceroute.txt','r').readlines()
    f_date = open('Pair_6_B_hops.csv', 'w')
    start = 'Date: '
    end = ' (MM/DD/YYYY),'
    count =0;
    matching ='*'
    #f_date.write("Date,Min,Avg,Max,Standard_Deviation\n")
    for i,line in enumerate(f):
        #f_date.write(find_between(line, "Date: ", " (MM/DD/YYYY), Time:"))
        if matching in line:
         count = count + 1
         f_date.write(line[:2]+'\n')
    print count



if __name__ == '__main__':
    fun1()

