# Color_Analyzer

### Introduction to sklearn, Kmeans, matplotlib and OpenCV

**Scikit-learn** (Sklearn) is the most useful and robust library for machine learning in Python. It provides a selection of efficient tools for machine learning and statistical modeling including classification, regression, clustering and dimensionality reduction via a consistence interface in Python.<br>
For more information - https://scikit-learn.org/stable/user_guide.html

**Kmeans** algorithm is an iterative algorithm that tries to partition the dataset into Kpre-defined distinct non-overlapping subgroups (clusters) where each data point belongs to only one group. It tries to make the intra-cluster data points as similar as possible while also keeping the clusters as different (far) as possible. It assigns data points to a cluster such that the sum of the squared distance between the data points and the cluster’s centroid (arithmetic mean of all the data points that belong to that cluster) is at the minimum. The less variation we have within clusters, the more homogeneous (similar) the data points are within the same cluster.<br>
For more information - https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html

**Matplotlib** is a comprehensive plotting library for creating static, animated, and interactive visualizations in Python and its numerical mathematics extension NumPy. It provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits like Tkinter, wxPython, Qt, or GTK. <br>
For more information - https://matplotlib.org/stable/contents.html

**OpenCV** is an open-source computer vision library that provides privileges to play with different images and video streams and also helps in end-to-end projects like object detection, face detection, object tracking, etc.<br>
For more information - https://docs.opencv.org/4.5.2/

### Code Explanation
The code is written in as a command line argument format, with the arguments being filename, --s where adding --s specifies that only the color scheme is required.<br>
![image](https://user-images.githubusercontent.com/50414959/125035982-1a988080-e0b0-11eb-85e6-2cf4fb0a4354.png)


### Sample Input Image used
![resized](https://user-images.githubusercontent.com/50414959/125033649-38b0b180-e0ad-11eb-9d20-b492eb64cd7e.jpg)



### Output Obtained

The image along with the color schema
![color_analysis_report](https://user-images.githubusercontent.com/50414959/125033834-76add580-e0ad-11eb-8217-e421810809e1.png)


The color schema only
![color_analysis_report](https://user-images.githubusercontent.com/50414959/125032395-875d4c00-e0ab-11eb-8e7e-90f23b58706d.png)
