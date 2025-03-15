<div align="left">

[简体中文](https://github.com/EtherealLunaria/SeamCarving/blob/master/README.md) | [English](https://github.com/EtherealLunaria/SeamCarving/blob/master/README_en.md)

</div>

# Seam Carving
Seam Carving for Content Aware Image Reduction

## Algorithm Overview
1. Calculate energy map
2. Build accumulated cost matrix using forward energy:
3. Find and remove minimum seam from top to bottom edge: 
4. Repeat step 1 - 3 until achieving targeting width 
5. Rotate image and repeat step 1 - 4 for vertical resizing: 
>Rotating image 90 degree counter-clockwise and repeat the same steps to remove rows.

## Result
<div>
  <br/>
  <b>Example image(466*700)</b>
  <br/>
  <br/>
  <kbd><img src="./example.png"></kbd>
  <br/>
  <br/>
  <b>Crop to 400*650</b>
  <br/>
  <br/>
  <kbd><img src="./example_400_650.png"></kbd>
  <br/>
  <br/>
  <b>Crop to 250*400</b>
  <br/>
  <br/>
  <kbd><img src="./example_250_400.png"></kbd>
  <br/>
</div>
