buy_list = [" "]

while True:
    i = 0
    buy_list[i] = input("Enter a word or write 'stop': ")
    i += 1
    if buy_list[-1] == "stop":
        break

for i in buy_list:
            
            print(i + ".", buy_list)
        
        