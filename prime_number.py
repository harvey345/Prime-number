num=int(input("請輸入數字：　\n"))
if num==2:
    print(num,"是質數")
else:
    for i in range(2,num):
        if num%i==0:
            print(num,"不是質數")
            break
    else:
        print(num,"是質數")
            
        