from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-801935946960-801935947120-801964022276-884e96f5a9ce6ed0e131fd7ad3b123b1', #app verification token
							'xoxb-801935946960-804637476854-iOm7cLWmMEZ4k3NyDNz2bgpL', # bot verification token
							'3RnCM4JCn5dHYac2eSGEabG7', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))