### GOPH547_Lab00_ZM_w2026
Introductory lab to ensure proper setup (part A) and beginner exercises (part B)

#GOPH 547
*semester:* w2026
*instructor:* Brandon Karchewski
*author:* Zoe Mitchell (student)

**i) instructions on how to download/clone the repository, set up a virtual environment, and install
the package:**<br>
First, use you machine terminal to navigate into where you want to save the project. You can then clone the repository
using HTTPS by taking [github]https://github.com/Zcmitchell04/GOPH547-w2026-lab00-stZM.git and
using the command 'git clone [github]https://github.com/Zcmitchell04/GOPH547-w2026-lab00-stZM.git' in your machine terminal. 
Once that is completed, you can open the project in your preferred IDLE and navigate to it in your terminal using the
command 'cd GOPH547-w2026-lab00-stZM'.<br>

In the machine terminal, after navigating to the project directory, activate the virtual environment using the following
commands: <br>
1) python -m virtualenv .venv
2) .\.venv\Scripts\activate # on Windows
source ./.venv/bin/activate # on Mac/Linux<br>

You can install the package using the command 'pip install -e' and (if there is one) you can install the 
requirements text using 'pip install -r requirements.txt'<br>

**ii) a brief description of what the driver.py script does:**
The driver script of this project produces a number of arrays varying in shape and content. It takes the sum of any
given vector along with element-wise multiplication, matrix multiplication and cross product of matrices A and B.
Additionally, using the driver script one can load in an image as an array and modfy it's colour scheme, size, etc.

**iii) instructions on how to run the code and what to expect for output:**

Before running the code, make sure you have loaded in a jpg/png image from you own device. You can modify the 
commands to tailor to your own parameters but if the imports to not connect to your own personal directories the 
code will not work. Once you run the code, you can expect to see labelled matrices printed in the terminal, along with
pop-up tabs of the images you loaded in and modified.