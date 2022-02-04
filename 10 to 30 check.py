#If entered no. lies between 10to30 then print :
# 1) If n is divible by 3 print "Sacred"
# 2) If n is divible by 7 print "Heart"
# 3) If n is divible by 3 and 7 both  print "Sacred Heart"
n = int(input("Enter the number : "))

for i in range(10,31):
    if n%3==0 and n%7==0:
        print("Sacred Heart")
    elif n%3==0:
        print("Sacred")
    
    elif n%7==0 :
        print("Heart")
        
    
    break    
    
  