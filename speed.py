import speedtest

test = speedtest.Speedtest()

down_speed = test.download()
up_speed = test.upload()

print ("Download : " , down_speed / 1000000 , "mb" )
print ("Upload : " , up_speed / 1000000 , "mb")