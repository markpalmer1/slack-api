from slackclient import SlackClient
import os
import environment

slack_token = environment.bot_auth
sc = SlackClient(slack_token)

sc.api_call(
  "chat.postMessage",
  channel="testagain",
  text="Hello from Python! :tada:"
)
