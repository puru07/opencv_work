/**
*       @file main.cpp
*       @brief OpenCV Stereo Webcam.
*       @author Martin Peris (http://www.martinperis.com)
*       @date 21/08/2011
*/

/*
        main.cpp - Implement a simple stereo webcam with OpenCV and C++
        Copyright (c) 2011 Martin Peris (http://www.martinperis.com).
        All right reserved.
        
        This application is free software; you can redistribute it and/or
        modify it under the terms of the GNU Lesser General Public
        License as published by the Free Software Foundation; either
        version 2.1 of the License, or (at your option) any later version.
        
        This application is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
        Lesser General Public License for more details.
        
        You should have received a copy of the GNU Lesser General Public
        License along with this application; if not, write to the Free Software
        Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
*/


//This works for me on OpenCV 2.0 with 2 Logicool webcams.
/*
#include "cv.h"
#include "highgui.h"
#include <iostream>
#include <sstream>
*/
#include <iostream>
#include <cv.h>
#include <highgui.h>
#include <sstream>
//Maybe in OpenCV2.2 the correct include statement would be:
//#include "opencv2/opencv.hpp"

using namespace std;
char key;
int main(int, char**)
{
    //CvCapture* capLeft = cvCaptureFromCAM(2); // open the Left camera
    CvCapture* capCam = cvCaptureFromCAM(1); // open the Right camera

    
    cv::namedWindow("Camera",1);
    

    int i = 1; //iter for number of captures
    string ImgName = "/data/image";
    
    string filetype = ".jpg";
    
    for(;;)
    {
        
        
        //cv::Mat frameCam;
        //cv::Mat frameRight;

          
          IplImage* frameCam = cvQueryFrame(capCam); 
          cvShowImage("Camera", frameCam); 
                   
            //lets capture images

            key = cvWaitKey(10); //capturing the kwyboard stroke
            if (char(key) == 32)
            {            
                i += 1;
                // saving left capture
                ostringstream oss;
                oss << ImgName << i << filetype;
                string file = oss.str();
                const char * cfile = file.c_str();
                oss.str("");
                cvSaveImage(cfile, frameCam);
            
            }

            
        
        if(char(key) == 27) break;
    }
    // the camera will be deinitialized automatically in VideoCapture destructor
    
    cvReleaseCapture(&capCam); //Release capture.
    
    cvDestroyWindow("Camera"); //Destroy Window
    
    
    return 0;
}
