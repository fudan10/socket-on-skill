from mycroft import MycroftSkill, intent_file_handler


class SocketOn(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('on.socket.intent')
    def handle_on_socket(self, message):
        self.speak_dialog('on.socket')


def create_skill():
    return SocketOn()

