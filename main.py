from Picture import Picture
import imageio

if __name__=="__main__":
    path=input("Enter the path of the image(default:./example.png): ")
    path=path if path else './example.png'
    img=Picture(path)
    print("Original image size:%d*%d"%(img.height,img.width))
    height=int(input("Enter the height of the image: "))
    width=int(input("Enter the width of the image: "))
    path=input("Enter the path of the output image(default:./out.png): ")
    path=path if path else './out.png'
    img.crop_w(width)
    img.crop_h(height)
    img.show()
    imageio.imwrite(path, img.img)