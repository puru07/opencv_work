#include <iostream>
#include <cv.h>
#include <highgui.h>
using namespace std;

int main(int argc, char** argv)
{

    cvNamedWindow("Example1", CV_WINDOW_AUTOSIZE);
    CvCapture* capture = cvCreateFileCapture(argv[1]);
    IplImage* frame;
    while(1){
    frame = cvQueryFrame(capture);
    if(!frame) break;
    cvShowImage("Example1", frame);
    char c = cvWaitKey(33);
    if(c == 27) break;
    }

    cvReleaseCapture(&capture);
    cvDestroyWindow("Example1");
    return 0;
}
