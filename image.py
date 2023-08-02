import cv2
import matplotlib.pyplot as plt
import numpy as np

width, height =800,800
myimage = np.ones((height, width, 3), dtype=np.uint8) * 255

#row 1

myimage[1:100,101:200] = [0,0,0]
myimage[1:100,301:400] = [0,0,0]
myimage[1:100,501:600] = [0,0,0]
myimage[1:100,701:800] = [0,0,0]

#row 2
myimage[101:200,1:100] = [0,0,0]
myimage[101:200,201:300] = [0,0,0]
myimage[101:200,401:500] = [0,0,0]
myimage[101:200,601:700] = [0,0,0]

#row 3

myimage[201:300,101:200] = [0,0,0]
myimage[201:300,301:400] = [0,0,0]
myimage[201:300,501:600] = [0,0,0]
myimage[201:300,701:800] = [0,0,0]

#row 4

myimage[301:400,1:100] = [0,0,0]
myimage[301:400,201:300] = [0,0,0]
myimage[301:400,401:500] = [0,0,0]
myimage[301:400,601:700] = [0,0,0]

#row 5

myimage[401:500,101:200] = [0,0,0]
myimage[401:500,301:400] = [0,0,0]
myimage[401:500,501:600] = [0,0,0]
myimage[401:500,701:800] = [0,0,0]

#row 6

myimage[501:600,1:100] = [0,0,0]
myimage[501:600,201:300] = [0,0,0]
myimage[501:600,401:500] = [0,0,0]
myimage[501:600,601:700] = [0,0,0]

#row 7

myimage[601:700,101:200] = [0,0,0]
myimage[601:700,301:400] = [0,0,0]
myimage[601:700,501:600] = [0,0,0]
myimage[601:700,701:800] = [0,0,0]

#row 8 

myimage[701:800,1:100] = [0,0,0]
myimage[701:800,201:300] = [0,0,0]
myimage[701:800,401:500] = [0,0,0]
myimage[701:800,601:700] = [0,0,0]



cv2.imshow("myimage",myimage)
cv2.waitKey()
cv2.destroyAllWindows()
