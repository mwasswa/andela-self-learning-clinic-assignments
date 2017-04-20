from random import randrange
class Mobile(object):
    def __init__(self):
        self.is_dual_sim = False
        self.imei_code = None
        self.brand = None
        self.model = None
        self.dialed_numbers = []
        self.received_calls = []
        self.sent_messages = []
        self.received_messages = []
        self.airtime_balance = 0
        self._call_log = "" #Private property that should not be accessed from outside this class --encapsulation
        self.received_sms = ""
        self.sent_sms = ""

    def set_mobile_parameters(self,imei_code,brand,model,is_dual_sim):
        self.imei_code = imei_code
        self.brand = brand
        self.model = model
        self.is_dual_sim = is_dual_sim

    def load_airtime(self,amount):
        self.airtime_balance += amount

    def get_model(self):
        return self.model

    def get_brand(self):
        return  self.brand

    def get_imei_code(self):
        return self.imei_code

    def dial_number(self,called_number):
        if self.airtime_balance < 200:
            self.dialed_numbers.append(called_number)
            return "Account balance is too low to complete this call\n\n"
        else:
            print("Calling " + called_number + " ----\n")
            self.airtime_balance -= 200
            self.dialed_numbers.append(called_number)
            return "Call Ended. Call cost: 200. New balance: " + str(self.airtime_balance) + "\n\n"

    def receive_incoming_call(self):
        calling_number = str(randrange(1000000,10000000,5))
        print("Incoming call from " + calling_number + ".....\n\n")
        self.received_calls.append(calling_number)
        return "Call ended\n\n"

    def send_text_message(self,message,receipient_number):
        if self.airtime_balance < 100:
            return "Message sending failed. Insufficient account balance\n\n"
        else:
            self.airtime_balance -= 100
            self.sent_messages.append(str(receipient_number) + " : "+ message)
            return "Message to " + str(receipient_number) + " sent successfully. Amount charged: 100. New airtime balance: " + str(self.airtime_balance) + "\n\n"

    def incoming_text_message(self):
        suffix = randrange(100,1000,2)
        from_number =  "+2547123" + str(suffix)
        message = "Andela bootcamp is awesome\n\n"
        self.received_messages.append(from_number + " : " + message)
        return from_number + " : " + message

    def clear_call_log(self):
        self.dialed_numbers = []
        self.received_calls = []
        return "Call log cleared successfully\n"

    def display_call_log(self):
        if len(self.dialed_numbers) > 0:
            self._call_log = "Dialed Numbers Log\n"
            for number in self.dialed_numbers:
                self._call_log += "----------------------\n" + number + "\n -------------------------- \n"

        if len(self.received_calls) > 0:
            self._call_log = "Received Calls Log\n"
            for number in self.received_calls:
                self._call_log += "----------------------\n" + number + "\n -------------------------- \n"

        if self.dialed_numbers == [] and self.received_calls == []:
            return "No call log entries at the moment\n\n"
        else:
            return self._call_log

    def display_sent_messages(self):
        if self.sent_messages == []:
            return "No sent messages available at the moment\n\n"
        else:
            self.sent_sms = "Sent SMS Log\n"
            for message in self.sent_messages:
                self.sent_sms += "---------------------------------------\n" + message + "\n------------------------------------\n"
            return self.sent_sms

    def display_received_messages(self):
        if self.received_messages == []:
            return "No sent messages available at the moment\n\n"
        else:
            self.received_sms = "Received SMS Log\n"
            for message in self.received_messages:
                self.received_sms += "---------------------------------------\n" + message + "\n------------------------------------\n"
            return self.received_sms

    def clear_message_inbox(self):
        self.received_messages = []
        return "All received messages successfully deleted\n"

    def clear_sent_messages(self):
        self.sent_messages = []
        return "All sent messages successfully deleted\n"

    #Private method not to be accessed from outside this class --encapsulation/abstraction
    def _compute_airtime_balance(self):
        return str(self.airtime_balance)

    def check_airtime_balance(self):
        return "Your airtime balance is: " + self._compute_airtime_balance() + "\n\n"


class Samsung(Mobile):
    def browse_the_internet(self):
        if self.airtime_balance < 500:
            return "You need a minimum balance of at least 500 to browse the internet\n\n"
        else:
            self.airtime_balance -= 500
            return "Internet browsing session in started and you've been charged 500 ......\n" \
                   "Your new airtime balance is " + self.check_airtime_balance()

    #Runtime Polymorphism -- another implementation of the recieve_incoming_call
    def receive_incoming_call(self):
        self.received_calls.append("Samsung")
        return "Incoming call from Samsung...."

    def open_camera(self, camera_mode = "default"):
        return "Camera has been opened in " + camera_mode + "mode"


