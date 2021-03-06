# Hacky Point Cloud Annotation with pptk
Hacky annotation tool for point cloud using pptk.

1) Clone the repository
2) Set up conda environment with Python 3.7
3) Install requirements:
```
  pip install -r requirements.txt
```  
4) Run pptk with sample data in 'data' folder:
```
python pptk_annotator.py data/2020-20-07-gazebo-data-0.npy    (On Linux)
python pptk_annotator.py data\2020-20-07-gazebo-data-0.npy    (On Windows)
```

## Annotation point cloud

1) Navigate the point cloud viewer:\
  Click + Drag: Rotate\
  Scroll wheel: Zoom in and out\
  Shift + Click + Drag: Pan\
  Ctrl + Click + Drag: Select a region of point clouds\
  Right Click: Deselect all points\
  
![Viewer](/imgs/instruction01.JPG)

2) After selecting the required points, select the viewer window and press ENTER

![Selecting points](/imgs/instruction02.JPG)

3) Return to the command line. A prompt should appear asking for a label. Enter the appropriate label.

![cmd line prompt](/imgs/instruction03.JPG)

  Notice that the labels for the hill have changed.

![changed points](/imgs/instruction04.JPG)

4) Repeats Step 1 to Step 3 until label annotation is complete.

5) To finish annotations, don't select anything in the viewer and press ENTER. The viewer will close and the new labels saved. 

  
