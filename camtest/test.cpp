#include <iostream>
#include <cv.h>
#include <highgui.h>
#include <sstream>

using namespace std;
char key;
int main()
{
    int i = 1;
    string filename = "img_data/image";
    string filetype = ".jpg";

    cvNamedWindow("Camera_Output", CV_CAP_XIAPI);    //Create window
    CvCapture* capture = cvCaptureFromCAM(0);    //(CV_CAP_ANY);  //Capture using any camera connected to your system
    while(1){ //Create infinte loop for live streaming
 
        IplImage* frame = cvQueryFrame(capture); //Create image frames from capture
        cvShowImage("Camera_Output", frame);   //Show image frames on created window
        key = cvWaitKey(10);     //Capture Keyboard stroke
        if (char(key) == 27){
            break;      //If you hit ESC key loop will break.
        }
        if (char(key) == 32)
        {            
            i += 1;
            ostringstream oss;
            oss << filename << i << filetype;
            string file = oss.str();
            const char * cfile = file.c_str();
            oss.str("");
            cvSaveImage(cfile, frame);
        }

    }
    cvReleaseCapture(&capture); //Release capture.
    cvDestroyWindow("Camera_Output"); //Destroy Window
    return 0;
}