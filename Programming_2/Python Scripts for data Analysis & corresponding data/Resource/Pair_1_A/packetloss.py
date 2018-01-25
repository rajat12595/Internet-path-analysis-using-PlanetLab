def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]+'\n'
    except ValueError:
        return ""

def fun1():
    f = open('Pair_1_A_traceroute.txt','r').readlines()
    f_date = open('Pair_1_A_hops.csv', 'w')
    start = 'Date: '
    end = ' (MM/DD/YYYY),'
    matching ='*'
    f_date.write('Pair_1_A'+'\n')
    #f_date.write("Date,Min,Avg,Max,Standard_Deviation\n")
    for i,line in enumerate(f):
        #f_date.write(find_between(line, "Date: ", " (MM/DD/YYYY), Time:"))
        if matching in line:
         f_date.write(line[:2]+'\n')




if __name__ == '__main__':
    fun1()

