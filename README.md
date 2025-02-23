Intelware
-
Remote System Interaction via Discord
(Educational Use Only)



:warning: Disclaimer
-

This project is intended for educational and research purposes only. It is designed to help cybersecurity students and professionals understand remote system interactions and potential security vulnerabilities. Unauthorized use of this code on any system without explicit permission is illegal and violates ethical hacking principles. The authors assume no responsibility for any misuse.



:book: About the Project
-
Intelware demonstrates how a Python bot can interact with a remote system via Discord, executing commands, capturing screenshots, and accessing the webcam. The purpose of this project is to help cybersecurity students analyze remote access techniques and improve defense mechanisms against them.




:rocket: Features




🖥️ Execute system commands remotely (with limitations)
📸 Capture and send screenshots
📷 Access and send webcam feed
💬 Receive real-time command responses




:shield: Ethical Use Cases
This project helps in:
Understanding the risks associated with remote access tools (RATs)
Learning how attackers exploit such techniques for defensive security research
Developing countermeasures to detect and prevent unauthorized access




:wrench: Installation & Setup

Requirements

Python 3.x
discord.py - Python library for interacting with Discord
OpenCV (cv2) - For camera access
pyautogui - For screen capture
Installation Steps
Clone this repository:

git clone https://github.com/anantarajkhanal/intelware
cd intelware


Install dependencies:

pip install -r requirements.txt
Create a Discord bot and obtain a bot token.



Update the script:
-
Open the script in a text editor and replace BotToken with your own bot token.

Run the bot in the target machine:
-
python intelware.py

How to control the machine:

go to your discord where the bot is deployed and use these commands:

- camera on: start the camera 

- camera off: turn off the camera

- $: send command to cmd 

- screen on: start the screenshot

- screen off: turn off the screenshot

- \help: show all instructions


:scroll: Legal & Ethical Guidelines

Only use this tool on devices you own or have explicit permission to test.
Do not deploy this on someone else's system without consent.
This tool is NOT for illegal activities—misuse can result in severe legal consequences.
If using this for penetration testing, follow responsible disclosure policies.
:bulb: How to Contribute
If you're interested in contributing, you can:

Improve security features
-
Develop methods to detect and prevent unauthorized remote access
Help enhance ethical cybersecurity education
Feel free to open an issue or submit a pull request on GitHub.

:mailbox_with_mail: Contact

For questions or contributions related to cybersecurity awareness, open an issue or submit a pull request on GitHub.

This project serves as an educational cybersecurity tool to promote awareness and ethical hacking practices. Stay ethical and responsible!

Happy Hacking! :computer: :lock:
