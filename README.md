# BasisAttendance
A Python script that automatically does your Basis online attendance



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
* [Usage](#usage)
* [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## About The Project
I was sick and tired of filling out my attendance every day between classes. It meant my already short 5 minute break was essentially cut into a 4 and a half minute break, ruined my workflow between classes, and when I forgot to click a little join button, my parents were notified. The worst part? Teachers are required to take roll in online class, which means I have to essentially fill out two attendances per class! 

I'd had enough, so I wrote this script so that I never have to do attendance before class again. The script opens up my school's webpage, clicks on the schedule, and clicks the join button at the start of all my classes. It is worth noting that the script only works for Basis students using spork (our school's website) as it is dependent on the UI of spork.school. 


### Built With
* [Python](https://www.python.org/)
* [Selenium](https://www.selenium.dev/)
* [PyautoGui](https://pyautogui.readthedocs.io/en/latest/)



<!-- GETTING STARTED -->
## Getting Started

1. Clone or download this repository and open up the file `loginCredentials.txt`.

2. Inside the file replace the placeholder username and password for your spork username and password.

3. Install Selenium and PyAutoGUI by doing 
`pip install selenium` 
and
`pip install pyautogui`
in the command prompt. (on unix an

4. Open up your attendance page on spork and locate the placement of your first join button.

5. Now run `positionFinder.py` and immediately hover your mouse over the place where your join button is (you only have a 5 second window before the program measures your mouse's position). Make sure you are hovering your mouse on one of the green pixels and not the white "join" part, as this script is dependent on finding a green pixel.

6. Copy the x and y values and replace the default values of 2930 and 575 (it is possible these values work on your monitor, but just in case check the position of your join button).

7. You are now ready to run the script! Now just run it at the beginning of all your classes using your favorite task scheduler (I personally recommend cron if you are on linux), and you will never need to click that accursed button again! You can also run the script on a raspberri pi so that it takes up none of your RAM while running, but you will need to switch your chromedriver to a firefox (or whatever browser you use) driver.



<!-- USAGE EXAMPLES -->
## Usage
A Youtube demonstration of the script: https://youtu.be/TZuQcU0-w28





<!-- TroubleShooting -->
## TroubleShooting

If the program fails to open up a Chrome webpage upon running, it is possible your computer is not running the latest version of Chrome. try redownloading the chromedriver and replacing the one in this project's folder with that one. 

If you are getting a raise WindowsError("windll.user32.ReleaseDC failed : return 0") or any similar error, try downgrading your python to 3.7. This is a known error that has to do with PyScreeze (one of the dependencies of PyAutoGUI) not being fully compatible with Python 3.8 and 3.9.



<!-- CONTACT -->
## Contact
Made by Mostafa Afr

Project Link: [https://github.com/Mostafaafr/BasisAttendance]




