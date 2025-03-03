import json
import logging
import os
import re
import time
from datetime import timedelta
from typing import Any

from dotenv import load_dotenv
from langchain_community.chat_message_histories import MomentoChatMessageHistory
from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.output_parsers import StrOutputParser
from langchain_core.outputs import LLMResult
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from slack_bolt import App
from slack_bolt.adapter.aws_lambda import SlackRequestHandler
from slack_bolt.adapter.socket_mode import SocketModeHandler

CHAT_UPDATE_INTERVAL_SEC = 1

load_dotenv()

# ボットトークンを使ってアプリを初期化します
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))
    
# ソケットモードハンドラーを使ってアプリを起動します
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()


@app.event("app_mention")
def handle_mention(event, say):
    user=event["user"]
    say(f"Hello <@{user}>!")    