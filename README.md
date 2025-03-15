<div align="left">

[简体中文](https://github.com/EtherealLunaria/Seam-Carving/blob/main/README.md) | [English](https://github.com/EtherealLunaria/Seam-Carving/blob/main/README_en.md)

</div>

# Seam Carving
基于内容的图像缩放算法

## 算法概览
1. 计算图像的能量图
2. 通过能量图计算代价图以及路径图
3. 通过代价图以及路径图寻找能量最低的seam
4. 重复上述步骤
5. 旋转图片对高进行缩放

## 结果展示
<div>
  <br/>
  <b>实例图(466*700)</b>
  <br/>
  <br/>
  <kbd><img src="./example.png"></kbd>
  <br/>
  <br/>
  <b>缩放至400*650</b>
  <br/>
  <br/>
  <kbd><img src="./example_400_650.png"></kbd>
  <br/>
  <br/>
  <b>缩放至250*400</b>
  <br/>
  <br/>
  <kbd><img src="./example_250_400.png"></kbd>
  <br/>
</div>

## 运行条件
- scipy
- numpy
- imageio
- matplotlib