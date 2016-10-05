#include <iostream>
#include <cv.h>
#include <highgui.h>
using namespace std;

int main()
{
    IplImage* img = cvLoadImage("sample.jpg",1);
    cvNamedWindow("Example1", CV_WINDOW_AUTOSIZE);
    cvShowImage("Example1", img);
    cvWaitKey(0);
    cvReleaseImage(&img);
    cvDestroyWindow("Example1");
    return 0;
}
