class CustomerSupport:
    def respond(self):
        print("Our customer support will respond shortly.")

class ChatSupport(CustomerSupport):
    def respond(self):
        print("Chat support is typing a response...")

class EmailSupport(CustomerSupport):
    def respond(self):
        print("An email response will be sent to you within 24 hours.")

class PrioritySupport(CustomerSupport):
    def respond(self):
        print("Priority support is responding immediately!")

chat = ChatSupport()
email = EmailSupport()
priority = PrioritySupport()

chat.respond()      
email.respond()    
priority.respond()  
