# create or get a handle to an OpenCV service
opencv = Runtime.create("opencv","OpenCV")
opencv.startService()
# reduce the size - face tracking doesn't need much detail
# the smaller the faster
opencv.addFilter("PyramidDown1", "PyramidDown")
# add the face detect filter
opencv.addFilter("FaceDetect1", "FaceDetect")

# ----------------------------------
# input
# ----------------------------------
# the "input" method is where Messages are sent to
# from other Services. The data from these messages can
# be accessed on based on these rules:
# Details of a Message structure can be found here
# http://myrobotlab.org/doc/org/myrobotlab/framework/Message.html 
# When a message comes in - the input function will be called
# the name of the message will be msg_+<sending service name>+_+<sending method name>
# In this particular case when the service named "opencv" finds a face it will publish
# a CvPoint.  The CvPoint can be access by msg_opencv_publish.data[0]
def input(data):

    #print 'found face at (x,y) ', msg_opencv_publishOpenCVData.data[0].x(), msg_opencv_publish.data[0].y()
    if (data.getBoundingBoxArray().size() > 0) :
    	rect = data.getBoundingBoxArray().get(0)
    	print 'face found in box ', rect.x, rect.y, rect.width, rect.height
    	print 'hello!'
    	return object

# create a message route from opencv to python so we can see the coordinate locations
opencv.addListener("publishOpenCVData", python.name, "input");

# set the input source to the first camera
opencv.capture()
