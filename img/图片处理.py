from skimage import io,data

img=io.imread("e:/yefang/img/1.jpg")
bdata = img[:,:,2]
io.imshow(bdata) # 绘图
io.show() # 显示图片
io.imsave('e:/yefang/img/%s1.jpg' % "Y",img) # 保存图片
print(type(img), "显示类型")
print(img.shape,  "显示尺寸")
print(img.shape[0],  '图片宽度')
print(img.shape[1],  '图片高度')
print(img.shape[2],  '图片通道数')
print(img.size  , '显示总像素个数')
print(img.max() , '最大像素值')
print(img.min()  ,'最小像素值')
print(img.mean() ,'像素平均值')
