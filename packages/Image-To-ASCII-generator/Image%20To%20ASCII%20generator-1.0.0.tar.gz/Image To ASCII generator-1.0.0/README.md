This is a quick library I wrote which allows users to transform any image into an ASCII text file string image by just calling one method 
".convertImageToASCII(image)" whereby image opened using the pillow library is passed as parameter "image". A string of lenght W*H is returned
(with appropiate "\n" to get a new line/row), where W is image width and H is image height. The string when written to a text file will look
just like the input image but each pixel replaced by a corresponding ASCII character depending on the pixel's brightness.

This library is written by Omar Maaouane at 12:00 11/12/2022 (DD/MM/YYYY)