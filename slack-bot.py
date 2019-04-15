from slackclient import SlackClient
import local_settings

slack_token = local_settings.bot_auth
sc = SlackClient(slack_token)

sc.api_call(
  "chat.postMessage",
  channel="testagain",
  text="Hello from Python! :tada:"
)
