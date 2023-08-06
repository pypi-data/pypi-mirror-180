# fastcmap: a fast colormap library

https://github.com/FallnJump/fastcmap

## Overview

a lightweight library that outputs the main colormaps that can be displayed by imshow in matplotlib.pyplot in numpy format at high speed. it may be more accurate to say that it is instantly usable rather than fast.

Take the case of converting from a 2D array to a colormap of the same size, still in numpy format.
Matplotlib.pyplot would be one of the best choices to display this.

    import numpy as np
    import matplotlib.pyplot as plt
    
    im=np.linspace(0,1,256)[None,:].repeat(256, axis=0)
    plt.imshow(im, cmap="jet")
    plt.show()


<img src=imgs/sample1.png>

A beautiful gradation appeared.
Now, if you want to get this as a numpy array of the same size as the original, it would be as follows.

- Erase the axis display and extra space.
- Adjust inch and dpi settings to achieve the original save size. save to BytesIO with savefig.
- Read image from BytesIO with something cv2.imread.

The purpose of this library was to provide a fast and easy alternative to the above.

For example, using this library, it is easy to create a composite of the original image and the heatmap as shown below (although matplotlib is used for display).

<img src="imgs/sampledbl.png">



### Requirements

numpy, pillow

* This library does not depends on matplotlib.

### How to Install

    pip install fastcmap


### Get start

    import numpy as np
    import fastcmap
    
    cmap=fastcmap.ColorMap()
    im=np.linspace(0,1,256)[None,:].repeat(256, axis=0)
    im=cmap.getColorMap(im, cmap="jet")
    import cv2
    cv2.imwrite("sample2.png", im)

Result)

<img src="imgs/sample2.png">


### Examples

(1) Output image with specified size and orientation for color scale

    from fastcmap import ColorMap
    cm=ColorMap()
    im256=cm.createColormap("jet")
    im256v=cm.createColormap("jet",t=0)
    im512=cm.createColormap("jet",(512,512))
    import matplotlib.pyplot as plt
    plt.subplot(131).imshow(im256)
    plt.subplot(132).imshow(im256v)
    plt.subplot(133).imshow(im512)
    plt.show()

Result)

<img src="imgs/splts3.png">

(2) Composite image and something like an Attention Map

    # im is image(0~1.0), att is attention(1ch 0~1.0).
    cm=ColorMap()
    heatmap=cm.getColormap(att, cmap="jet")
    heatmap=heatmap.astype(float)/255
    imheat=(im+heatmap)/2
    
    import matplotlib.pyplot as plt
    plt.imshow(imheat)
    plt.show()


Result)

<img src="imgs/sampledbl.png">



(3) Colormap generation with custom curves

    cm=ColorMap()
    jet=cm.createColormap("jet")
    biri=cm.createColormap("viridis")
    
    # if we make a custom colormap such as:
    jetbiri=jet/2+biri/2
    # make 1-d parameters
    jetbiri_rgb_data=jetbiri[0]
    # axis-0 must be (r,g,b).
    jetbiri_rgb_data=jetbiri_rgb_data.transpose(1,0)
    print(jetbiri_rgb_data.shape)
    # register new colormap as "jetbiri".
    cm.registerCustomCmap_fromPlot("jetbiri" , jetbiri_rgb_data)

However, this alone does not tell us if the "jetbiri" colormap is really newly registered, so let's check how the "jetbiri" looks like.

    # create colormap using the cmap we just registered. 
    jetbiri_gen=cm.createColormap("jetbiri")
    # make lines to plot later
    gen_data=jetbiri_gen[0].transpose(1,0)
    # merge the two into one image for comparison.
    dual_im=np.zeros(jetbiri.shape, dtype=np.uint8)+255
    h=dual_im.shape[0]//2-5
    dual_im[:h]=jetbiri[:h]
    dual_im[-h:]=jetbiri_gen[:h]
    
    import matplotlib.pyplot as plt
    rgb="rgb"
    for line, c in     zip(jetbiri_rgb_data, rgb):
    	plt.subplot(211).plot(line, color=c)
    cmy="kkk"
    for line, c in zip(gen_data, cmy):
    	plt.subplot(211).plot(line, color=c, linestyle="dashed")
    plt.subplot(212).imshow(dual_im)
    
    rgbprops=cm.dict["jetbiri"]
    s="("
    for p in rgbprops:
    	s+=str(len(p))+","
    s=s[:-1]+")"
    plt.text(0,235,s,fontsize=28)
    plt.show()


Result)

<img src="imgs/samplereg.png">

The solid colored line in the plot is the profile data to be color-mapped.
The black dashed line, which almost overlaps, is the "jetbiri" profile.
(4,5,5) is the number of curves to represent the colormap, corresponding to rgb.
The fewer the number, the faster the colormap generation (default registered colormaps are generally 1 to 5).
The number of other colormaps is described below.
The time required to generate a colormap for "jetbiri" is about the same as for "jet".

Registration of a custom colormap is only valid for that instance (equivalent to `cm` in the code).
If you want to apply it to another instance, use saveAs to output to a file and then load it in another instance.

A function to register a custom colormap by directly specifying line-profile is also provided, but it is not likely to be used often, so it is omitted.

(3) (addtional)Generating confusion matrix

The following code can also create a confusion matrix.
It may be a little slow because it does not take high speed processing into account.

    cm=ColorMap()
    map=np.random.uniform(size=(6,6))
    classes=["Alice","Bob","Charol","Dave","Ellen","Frank"]
    im=cm.makeConfuseMatrix(map, classes=classes)
    plt.imshow(im)
    plt.show()

Result)

<img src="imgs/samplemtx.png">
　
The default background color of each cell is gray, but it can be changed as follows.

    # im=cm.makeConfuseMatrix(map, classes=classes)
    im=cm.makeConfuseMatrix(map, classes=classes, cmap=plasma)

Result)

<img src="imgs/samplemtx2.png">

There is a limitation that font size, etc. cannot be adjusted.

### Comparison with matplotlib

The following legend is available.

<img src=imgs/cbarlist.png>

The two color bars of the same color are divided into upper and lower bars. The upper bar is the output by matplotlib, and the lower bar is the output by fastcmap.

The time taken to create each color bar in the output table is shown below.

|Library|time(s)|
|---|---|
|matplotlib|14.00|
|fastcmap|0.30|

Speed ratio of about 40 times.

The speed of map generation slows down in proportion to the sum of the numbers in parentheses under the name of each color bar.
The numbers in parentheses are the number of generating formulas required to generate the colors r, g, and b, respectively.

<img src=imgs/cbarlist2.png>


256x256(unit: s)

|cmap|cool|jet|viridis|gist_ncar|flag|
|---|---|---|---|---|---|
|matplotlib|0.32|0.32|0.32|0.30|0.54*|
|fastcmap|0.01|0.02|0.02|0.04|0.09|




512x512(unit: s)

|cmap|cool|jet|viridis|gist_ncar|flag|
|---|---|---|---|---|---|
|matplotlib|0.48|0.43|0.43|0.44|0.44|
|fastcmap|0.08|0.11|0.09|0.16|0.37|


1024x1024(unit: s)

|cmap|cool|jet|viridis|gist_ncar|flag|
|---|---|---|---|---|---|
|matplotlib|0.83|0.85|0.84|0.85|0.83|
|fastcmap|0.28|0.41|0.35|0.60|1.38|


1600x1600(unit: s)

|cmap|cool|jet|viridis|gist_ncar|flag|
|---|---|---|---|---|---|
|matplotlib|1.66|1.69|1.66|1.67|1.66|
|fastcmap|0.70|1.08|0.89|1.67|4.01|


