# Image to dice converter

RGB is 3 bytes each letter having here has 1 byte value
1 byte is 8 bits, 8 true or false. 2 different possibilities on 8 bits are 2^8 = 256
So, in RGB you can produce 256 * 256 * 256 =~ 16 million different colors
Grayscale is just 1 byte. So, there are only values between 0-255 (256 different values)
By a formula, a RGB color can be converted to Grayscale
And here is the magic: the numbers are grouped into numbers from 0 to 6
If Grayscale number (0 is black, 255 is white, between are "256 shades of gray :P ") is close to white, it gets 0, if close to black it gets 6...
Basically divide number by 42.5 (255/6)
So, basically we changed Grayscale to Dicescale :P (I made up this name right now), instead of 0 to 255 we have 0 to 6
But instead of different colors for each number, there are just die 🎲
In each "pixel" (boxes which you can see if you zoom), the bigger the dice number, the denser white dots which give an illusion of "this is lighter / this is darker"

## Usage

Run `main.py` in a directory with an image named `input.png`, when it is done it will output a file called `output.png`. Alternatively, you can type the file path as an argument and output will be in the same folder as the input path.

