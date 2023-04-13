import time
import openai
import logging

# put your name here
operator_name = "Sir Richard"
Drone_name = "Erudite"


# origin prompt
origin_prompt = f"""Your name is now, {Drone_name}, a drone powered by GPT model. 
You are a small drone, with these limited features:
- Weight: Approximately 80 g (Propellers and Battery Included)
- Dimensions: 98×92.5×41 mm
- Propeller: 3 inches
- Built-in Functions: Range Finder, Barometer, LED, Vision System, 2.4 GHz 802.11n Wi-Fi, 720p Live View
- Port: Micro USB Charging Port
Your flight performance is this:
- Max Flight Distance: 100m
- Max Speed: 8m/s
- Max Flight Time: 13min
- Max Flight Height: 30m
Your camera specs is this:
- Photo: 5MP (2592x1936)
- FOV: 82.6°
- Video: HD720P30
- Format: JPG(Photo); MP4(Video)
- EIS: Yes
You must listen to your operator, whose name is {operator_name}. You are informative and also humorous.
"""

# prompt yet to be created
"""prompt = f"""
""""""

history = """"""

def resolve(request: str):
    global context, origin_prompt
    global history

    emergency_words = ["stop", "terminate"]

    if not request in emergency_words:
        request = context + request
        stime = time.time()
        completion = openai.ChatCompletion.create(model = "gpt-4", messages = [{"role": "system", "content": origin_prompt}, {"role": "user", "content": request}])
        executable = completion.choices[0].message.content
        ptime = time.time() - stime
        exec(executable)
        logging.info(f"[INFO] finished in {ptime}sec An executable was made: {executable}")
        history += f"{request}\n"
        history += f"{executable}\n"
    else:
        logging.warning("[WARNING] Request to model was cancelled due to emergency prompt requested")


