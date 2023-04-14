import cv2
import numpy as np
kernel = np.ones((5, 5), np.uint8)


####################################
def cepianyizhi1(img,roix=750,roiy=400,roix2=100,roiy2=400):  #要求灰度图片格式 #高，宽

    img = cv2.resize(img, (int(img.shape[1] / 3), int(img.shape[0] / 3)))
    print(img.shape)

    # create roi0
    x, y, w, h = roix, roiy, 200, 200
    roi1 = img[x:x + h, y:y + w]
    ########################roi1########################
    #gray = cv2.cvtColor(roi1, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur( roi1, (5, 5), 0)
    ret, binary = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY)
    # cv2.circle(roi1,(40,60),10,(0,133,0),-1)  #前面为横坐标，后面为纵坐标

    for j in range(190, 0, -1):
        # print(gray[j, 50])
        if binary[j, 50] == 0:  # 0黑色，255为白色

            cv2.circle(roi1, (50, j), 4, (66, 111, 0), -1)
            cv2.line(roi1, (50, j), (50, j - 30), (255, 255, 0), 8)  # y
            cv2.line(roi1, (50, j), (50 + 30, j), (255, 255, 0), 8)  # x
            
            print(j)
            break

    x2,y2,w,h =roix2,roiy2,200,200
    roi2 = img[x2:x2+h,y2:y2+w]
    #gray2 = cv2.cvtColor(roi2,cv2.COLOR_BGR2GRAY)
    gray2 = cv2.GaussianBlur(roi2,(5,5),0)
    ret2,binary2 = cv2.threshold(gray2,100,255,cv2.THRESH_BINARY)
    for k in range(190, 0, -1):
        #print(gray[j, 50])
        if binary2[k,50] ==0:   #0黑色，255为白色

            cv2.circle(roi2,(50,k),4,(66,111,0),-1)
            cv2.line(roi2,(50,k) ,(50,k-30), (255,255,0), 4)#y
            cv2.line(roi2, (50,k) , (50+30,k ),  (255, 255, 0), 4)#x
            
            print(k)
            break

    distance = roix+j-(roix2+k)
    print("distance is: ", distance)

    cv2.rectangle(roi1, (0, 0), (w, h), (255, 255, 0), 8)  #
    cv2.rectangle(roi2, (0, 0), (w, h), (122, 122, 0), 4)  #
    return distance,img



##################################大水封
def measure_distance(img,roi1x=150,roi1y=250,roi2x=600,roi2y=970):#传入灰度图
    img = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))
    #print(img.shape)
    kernel = np.ones((5, 5), np.uint8)

    ########################roi1########################
    x, y, w, h = roi1x, roi1y, 200, 200
    roi1 = img[x:x + h, y:y + w]
    x2, y2, w, h = roi2x,roi2y, 200, 200
    roi2 = img[x2:x2 + h, y2:y2 + w]
    #gray = cv2.cvtColor(roi1, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur( roi1, (5, 5), 0)
    ret, binary = cv2.threshold(gray,220, 255, cv2.THRESH_BINARY)
    #gray2 = cv2.cvtColor(roi2, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.GaussianBlur(roi2, (5, 5), 0)
    ret, binary2 = cv2.threshold(gray2,90, 255, cv2.THRESH_BINARY)
    for j in range(0, 199, 1):
        #print(binary[50, j])
        if binary[50, j] == 0:  # 0黑色，255为白色

            cv2.circle(roi1, (j, 50), 4, (0, 255, 0), -1)
            cv2.line(roi1, (j, 50), (j, 50 - 30), (122, 122, 0), 8)  # y
            cv2.line(roi1, (j, 50), (j + 30, 50), (122, 122, 0), 8)  # x
            
            print(j)
            break
    cv2.rectangle(roi1, (0, 0), (w, h), (122, 122, 0), 8)  #
    distance = j + y
    for j in range(0, 176, 1):
        #print("binary2[50,j]  ",binary2[50, j])
        try:
            if binary2[50, j] == 255:  # 0黑色，255为白色

                cv2.circle(roi2, (j, 50), 4, (0, 255, 0), -1)
                cv2.line(roi2, (j, 50), (j, 50 - 30), (0, 255, 0), 4)  # y
                cv2.line(roi2, (j, 50), (j + 30, 50), (0, 255, 0), 4)  # x
                cv2.rectangle(roi2, (0, 0), (w, h), (122, 122, 0), 4)  #
                print(j)
                break
        except:
            pass
    distance2 = j + y2
    #print(distance2)
    gap = distance2 - distance
    return gap,img
def measure_gear_gap(img,roi1x=290,roi1y=200,roi1xend = 350,roi1yend = 300,roi2x=600,roi2y=970,roi2xend = 700,roi2yend =1000,thresh0=200,thresh1=90):#传入灰度图
    img = cv2.resize(img, (int(img.shape[1]), int(img.shape[0])))
    #print(img.shape)
    kernel = np.ones((5, 5), np.uint8)
    h = abs(roi1x-roi1xend)
    w = abs(roi1yend-roi1y)

    ########################roi1########################
    x, y, = roi1x, roi1y
    roi1 = img[x:x + h, y:y + w]
    h2 = abs(roi2x-roi2xend)
    w2 = abs(roi2yend - roi2y)
    x2, y2,= roi2x,roi2y
    roi2 = img[x2:x2 + h2, y2:y2 + w2]
    #gray = cv2.cvtColor(roi1,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(roi1,(5,5),0)
    ret,binary = cv2.threshold(gray,thresh0,255,cv2.THRESH_BINARY)
    #size = roi1.shape
    #print(size)

    #cv2.imshow("roi",roi1)
    #cv2.imshow("binary",binary)

    #gray2 = cv2.cvtColor(roi2,cv2.COLOR_BGR2GRAY)
    gray2 = cv2.GaussianBlur(roi2,(5,5),0)
    ret,binary2 = cv2.threshold(gray2,thresh1,255,cv2.THRESH_BINARY)
    #cv2.imshow("bina",binary2)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    #cv2.imshow("roi",roi2)
    #cv2.imshow("binary",binary2)
    #cv2.waitKey(0)
    #cv2.circle(roi1,(40,60),10,(0,133,0),-1)  #前面为横坐标，后面为纵坐标
    for j in range(1, w, 1):
        #print(gray[j, 50])
        if binary[5,j] ==255:   #0黑色，255为白色
            print(j)
            break

    distance = j+y
    print(distance)
    for k in range(1, w2, 1):
        #print(gray[j, 50])
        if binary2[5,k] ==255:   #0黑色，255为白色
            print(k)
            break

    distance2 = k+y2
    print(distance2)
    gap = distance2-distance
    print("distance is : ",gap)
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    #x,y,w,h = roi1x,roi1y,200,200
    roi1 = img[x:x+h,y:y+w]
    #x2,y2,w,h = roi2x,roi2y,200,200
    roi2 = img[x2:x2+h2,y2:y2+w2]
    #ROI1
    cv2.circle(roi1, (j, 5), 4, (0, 255, 0), -1)
    cv2.line(roi1, (j, 5), (j, 5 - 30), (0,0, 255), 4)  # y
    cv2.line(roi1, (j, 5), (j + 30, 5), (0, 0, 255), 4)  # x
    #ROI2
    cv2.circle(roi2, (k, 5), 4, (0, 255, 0), -1)
    cv2.line(roi2, (k ,5), (k, 5 - 30), (0, 0, 255), 4)  # y
    cv2.line(roi2, (k, 5), (k + 30, 5), (0, 0, 255), 4)  # x
    cv2.rectangle(roi1, (0, 0), (w, h), (255, 255, 0), 7)  #
    cv2.rectangle(roi2, (0, 0), (w2, h2), (255, 255, 0), 7)  #
    return gap,img
def cepianyizhi(img,roi1x=290,roi1y=200,roi1xend = 350,roi1yend = 300,roi2x=600,roi2y=970,roi2xend = 700,roi2yend =1000,thresh0=200,thresh1=90):  # 这是偏移值制动臂750  要求灰度图片格式 #高，宽
    img = cv2.resize(img, (int(img.shape[1] / 3), int(img.shape[0] / 3)))
    #print(img.shape)
    h = abs(roi1x-roi1xend)
    w = abs(roi1yend-roi1y)

    ########################roi1########################
    x, y, = roi1x, roi1y
    roi1 = img[x:x + h, y:y + w]
    h2 = abs(roi2x-roi2xend)
    w2 = abs(roi2yend - roi2y)
    x2, y2,= roi2x,roi2y
    roi2 = img[x2:x2 + h2, y2:y2 + w2]
    ########################roi1########################
    #gray = cv2.cvtColor(roi1, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur( roi1, (5, 5), 0)
    ret, binary = cv2.threshold(gray, thresh0, 255, cv2.THRESH_BINARY)
    # cv2.circle(roi1,(40,60),10,(0,133,0),-1)  #前面为横坐标，后面为纵坐标
    
    for j in range(1,h,1):
        # print(gray[j, 50])
        if binary[j, 5] == 255:  # 0黑色，255为白色
            print(j)
            break

    #cv2.imshow("roi1",roi1)
    #cv2.waitKey(0)
    
    #gray2 = cv2.cvtColor(roi2,cv2.COLOR_BGR2GRAY)
    gray2 = cv2.GaussianBlur(roi2,(5,5),0)
    ret2,binary2 = cv2.threshold(gray2,thresh1,255,cv2.THRESH_BINARY)
    for k in range(1, h2, 1):
        #print(gray[j, 50])
        if binary2[k,5] ==0:   #0黑色，255为白色
            print(k)
            break
    print("run here1")
    distance = (roi2x+k)-(roi1x+j)
    print("distance is: ", distance)
    print("run here2")
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    
    roi1 = img[x:x + h, y:y + w]
    
    roi2 = img[x2:x2+h2,y2:y2+w2]
    #ROI1
    
    cv2.circle(roi1, (5, j), 4, (66, 111, 0), -1)
    cv2.line(roi1, (5, j), (5, j+30), (0, 255, 0), 8)  # y
    cv2.line(roi1, (5, j), (5 + 30, j), (0, 255, 0), 8)  # x
    #ROI2
    
    cv2.circle(roi2, (5, k), 4, (66, 111, 0), -1)
    cv2.line(roi2, (5, k), (5, k + 30), (0, 255, 0), 4)  # y
    cv2.line(roi2, (5, k), (5 + 30, k), (0, 255, 0), 4)  # x
    print("run here3")
    cv2.rectangle(roi1, (0, 0), (w, h), (255, 255, 0), 8)  #
    cv2.rectangle(roi2, (0, 0), (w2, h2), (255, 255, 0), 4)  #

    return distance,img


##################################
def measure_tuoshuizhou_distance(img,roi1x=290,roi1y=200,roi1xend = 350,roi1yend = 300,roi2x=600,roi2y=970,roi2xend = 700,roi2yend =1000,thresh0=200,thresh1=90):#传入灰度图
    print("run here")
    img = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))
    #print(img.shape)
    kernel = np.ones((5, 5), np.uint8)
    h = abs(roi1x-roi1xend)
    w = abs(roi1yend-roi1y)

    ########################roi1########################
    x, y, = roi1x, roi1y
    roi1 = img[x:x + h, y:y + w]
    h2 = abs(roi2x-roi2xend)
    w2 = abs(roi2yend - roi2y)
    x2, y2,= roi2x,roi2y
    roi2 = img[x2:x2 + h2, y2:y2 + w2]
    #gray = cv2.cvtColor(roi1, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur( roi1, (5, 5), 0)
    ret, binary = cv2.threshold(gray,thresh0, 255, cv2.THRESH_BINARY)
    #gray2 = cv2.cvtColor(roi2, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.GaussianBlur(roi2, (5, 5), 0)
    ret, binary2 = cv2.threshold(gray2,thresh1, 255, cv2.THRESH_BINARY)

    for j in range(1, w, 1):
        #print(binary[50, j])
        if binary[5, j] == 0:  # 0黑色，255为白色



            print(j)
            break

    distance = j + y
    
    for k in range(1,w2, 1):
        #print("binary2[50,j]  ",binary2[50, j])
        try:
            if binary2[5, k] == 255:  # 0黑色，255为白色


                print(k)
                break
        except:
            pass
    distance2 = k + y2
    #print(distance2)
    gap = distance2 - distance
    img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    #roi1
    #x, y, w, h = roi1x, roi1y, 200, 200
    roi1 = img[x:x + h, y:y + w]
    #x2, y2, w, h = roi2x,roi2y, 200, 200
    roi2 = img[x2:x2 + h2, y2:y2 + w2]
    cv2.circle(roi1, (j, 5), 4, (0, 255, 0), -1)
    cv2.line(roi1, (j, 5), (j, 5+ 30), (0, 0, 255), 4)  # y
    cv2.line(roi1, (j, 5), (j + 30, 5), (0, 0, 255), 4)  # x
    #roi2
    cv2.circle(roi2, (k, 5), 4, (0, 255, 0), -1)
    cv2.line(roi2, (k, 5), (k, 5 + 30), (0, 0, 255), 4)  # y
    cv2.line(roi2, (k, 5), (k + 30, 5), (0, 0, 255), 4)  # x

    cv2.rectangle(roi1, (0, 0), (w, h), (255, 255, 0), 4)  #
    cv2.rectangle(roi2, (0, 0), (w2, h2), (255, 255, 0), 4)  #
    #cv2.imshow("roi1",img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    return gap,img
