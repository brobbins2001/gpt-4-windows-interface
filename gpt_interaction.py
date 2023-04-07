import openai
import os
import json
import textwrap
import time


class GptCom:
    """
    my class
    """

    def __init__(self, model="gpt-4", temperature=0.7, max_tokens=512, session_id=None):
        # Load API key from environment variable
        self.summarized_history = None
        openai.api_key = "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"

        # Load prompt from 'prompt.txt'
        with open("prompt.txt", "r") as file:
            self.system_prompt = file.read()

        self.temperature = temperature
        self.max_tokens = max_tokens
        self.model = model
        self.cost_per_input_token = .03 / 1000
        self.cost_per_output_token = .12 / 1000
        self.session_id = session_id or str(time.time())  # Default to a timestamp if not provided

        # Update system message with additional user context
        self.system_message = {"role": "system", "content": self.system_prompt}
        self.messages = [self.system_message]

        # Create instance-specific directory if it doesn't exist
        self.instance_directory = os.path.join("instances", self.session_id)
        if not os.path.exists(self.instance_directory):
            os.makedirs(self.instance_directory)

    def get_relevant_messages(self):
        if len(self.messages) < 3:
            return [self.system_message] + self.messages[-len(self.messages) + 1:]
        else:
            return [self.system_message] + self.messages[3:]

    def generate_response(self, user_input):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=self.get_relevant_messages(),
            max_tokens=self.max_tokens,
            n=1,
            stop=None,
            temperature=self.temperature,
        )
        return response.choices[0]

    def get_interaction(self, user_input):
        self.messages.append({"role": "user", "content": user_input})

        gpt_response = self.generate_response(user_input)

        self.messages.append({"role": "assistant", "content": gpt_response})

        # Save history
        with open(os.path.join(self.instance_directory, "history.json"), "w") as file:
            json.dump(self.messages, file, indent=2)

        return gpt_response