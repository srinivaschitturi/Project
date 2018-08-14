for x in range(1,100):
    if (x%2==0) & (x%3==0):
        print("pingpong", end=" ")
    elif x%2==0:
        print("ping",end=" ")
    elif x%3==0:
        print("pong",end=" ")
    else:
        print(x)