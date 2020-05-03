import os
import cv2

ROOT_DIR = r'C:\Users\smitr\Desktop\Prohibitory Item Detection\imgs\Test'
all_img_list = os.listdir(ROOT_DIR)

i = 1

for img_name in all_img_list:
    
    img_path = os.path.join(ROOT_DIR, img_name)
    orig = cv2.imread(img_path)
    
    if orig is None:
        continue
    
    fname = img_name.split('.')[0]
    
    flip_x = cv2.flip(orig, 1)
    flip_y = cv2.flip(orig, 0)
    flip_xy = cv2.flip(orig, -1)
    
    new_img_nm = fname + '_flipX.png'
    cv2.imwrite(os.path.join(ROOT_DIR, new_img_nm), flip_x)
    
    new_img_nm = fname + '_flipY.png'
    cv2.imwrite(os.path.join(ROOT_DIR, new_img_nm), flip_y)
    
    new_img_nm = fname + '_flipXY.png'
    cv2.imwrite(os.path.join(ROOT_DIR, new_img_nm), flip_xy)
    
    if i % 5 == 0:
        print("{} images done".format(i))
        
    i += 1
        
print("Completed !!!")
