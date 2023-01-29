PS C:\Users\daran\Documents\PYTHON\C107> & C:/Users/daran/AppData/Local/Programs/Python/Python39/python.exe -m pip install -U autopep8
Collecting autopep8
  Downloading autopep8-2.0.0-py2.py3-none-any.whl (45 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 45.4/45.4 kB 1.1 MB/s eta 0:00:00
Collecting pycodestyle>=2.9.1
  Downloading pycodestyle-2.10.0-py2.py3-none-any.whl (41 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 41.3/41.3 kB 2.1 MB/s eta 0:00:00
Collecting tomli
  Downloading tomli-2.0.1-py3-none-any.whl (12 kB)
Installing collected packages: tomli, pycodestyle, autopep8
Successfully installed autopep8-2.0.0 pycodestyle-2.10.0 tomli-2.0.1
PS C:\Users\daran\Documents\PYTHON\C107> & C:/Users/daran/AppData/Local/Programs/Python/Python39/python.exe c:/Users/daran/Documents/PYTHON/C107/object_tracking.py
Traceback (most recent call last):
  File "c:\Users\daran\Documents\PYTHON\C107\object_tracking.py", line 14, in <module>
    tracker = cv2.TrackerCSRT_create()
AttributeError: module 'cv2' has no attribute 'TrackerCSRT_create'
PS C:\Users\daran\Documents\PYTHON\C107> python -m pip install opencv-contrib-python
Collecting opencv-contrib-python
  Downloading opencv_contrib_python-4.6.0.66-cp36-abi3-win_amd64.whl (42.5 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 42.5/42.5 MB 8.2 MB/s eta 0:00:00
Requirement already satisfied: numpy>=1.17.3 in c:\users\daran\appdata\local\programs\python\python39\lib\site-packages (from opencv-contrib-python) (1.23.5)
Installing collected packages: opencv-contrib-python
Successfully installed opencv-contrib-python-4.6.0.66
PS C:\Users\daran\Documents\PYTHON\C107> pip show opencv
WARNING: Package(s) not found: opencv
PS C:\Users\daran\Documents\PYTHON\C107> pip show opencv-
WARNING: Package(s) not found: opencv-
PS C:\Users\daran\Documents\PYTHON\C107> pip show opencv-python
Name: opencv-python
Version: 4.6.0.66
Summary: Wrapper package for OpenCV python bindings.
Home-page: https://github.com/skvark/opencv-python
Author:
Author-email:
License: MIT
Location: c:\users\daran\appdata\local\programs\python\python39\lib\site-packages
Requires: numpy, numpy, numpy
Required-by:
PS C:\Users\daran\Documents\PYTHON\C107> & C:/Users/daran/AppData/Local/Programs/Python/Python39/python.exe c:/Users/daran/Documents/PYTHON/C107/object_tracking.py
Select a ROI and then press SPACE or ENTER button!
Cancel the selection process by pressing c button!
Traceback (most recent call last):
  File "c:\Users\daran\Documents\PYTHON\C107\object_tracking.py", line 23, in <module>
    tracker.init(img, bbox)
cv2.error: OpenCV(4.6.0) D:\a\opencv-python\opencv-python\opencv\modules\core\src\matrix.cpp:809: error: (-215:Assertion failed) 0 <= roi.x && 0 <= roi.width && roi.x + roi.width <= m.cols && 0 <= roi.y && 0 <= roi.height && roi.y + roi.height <= m.rows in function 'cv::Mat::Mat'

PS C:\Users\daran\Documents\PYTHON\C107>
PS C:\Users\daran\Documents\PYTHON\C107> & C:/Users/daran/AppData/Local/Programs/Python/Python39/python.exe c:/Users/daran/Documents/PYTHON/C107/object_tracking.py
Select a ROI and then press SPACE or ENTER button!
Cancel the selection process by pressing c button!
Traceback (most recent call last):
  File "c:\Users\daran\Documents\PYTHON\C107\object_tracking.py", line 26, in <module>
    if (bbox.x >= 0 and bbox.y >= 0 and (bbox.width + bbox.x < video.cols) and bbox.height + bbox.y < video.rows):
AttributeError: 'tuple' object has no attribute 'x'
PS C:\Users\daran\Documents\PYTHON\C107> & C:/Users/daran/AppData/Local/Programs/Python/Python39/python.exe c:/Users/daran/Documents/PYTHON/C107/object_tracking.py
Select a ROI and then press SPACE or ENTER button!
Cancel the selection process by pressing c button!
Traceback (most recent call last):
  File "c:\Users\daran\Documents\PYTHON\C107\object_tracking.py", line 26, in <module>
    if (img.x >= 0 and img.y >= 0 and (img.width + img.x < video.cols) and img.height + img.y < video.rows):
AttributeError: 'numpy.ndarray' object has no attribute 'x'
PS C:\Users\daran\Documents\PYTHON\C107>