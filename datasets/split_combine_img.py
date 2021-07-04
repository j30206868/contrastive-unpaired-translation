import glob
import cv2
import os
img_folders = ['./cityscapes/train/*.jpg', './cityscapes/val/*.jpg']

def splitImgToTwoFolder(img_search_rule):
    is_folder_init = False
    for img_name in glob.glob(img_search_rule):
        img = cv2.imread(img_name)
        width = img.shape[1]
        left = img[:, 0:width//2, ...]
        right= img[:, width//2:, ...]
        save_dir = 'test' if 'val' in img_name else 'train'
        # print(left.shape)
        # print(right.shape)
        # cv2.imshow('left', left)
        # cv2.imshow('right', right)
        # cv2.waitKey(0)
        # print(img_name)
        img_basename = os.path.basename(img_name)
        left_path = img_name.replace(img_basename, '%sA/%s' % (save_dir, img_basename))
        right_path = img_name.replace(img_basename, '%sB/%s' % (save_dir, img_basename))
        
        if not is_folder_init:
            img_dir = os.path.dirname(img_name)
            trainA_folder = os.path.join(img_dir, '%sA' % save_dir)
            trainB_folder = os.path.join(img_dir, '%sB' % save_dir)
            if not os.path.exists(trainA_folder):
                os.mkdir(trainA_folder)
            if not os.path.exists(trainB_folder):
                os.mkdir(trainB_folder)
            is_folder_init = True

        cv2.imwrite(left_path, left)
        cv2.imwrite(right_path, right)
        print('split %s' % img_name)

for img_folder in img_folders:
    splitImgToTwoFolder(img_folder)