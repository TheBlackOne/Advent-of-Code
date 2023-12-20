from os import path

input = """broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a"""

dir = path.dirname(__file__)
input_path = path.join(dir, "input.txt")
# with open(input_path) as f:
#    input = f.read()

modules = {}
signals_sent = {0: 0, 1: 0}

process_queue = []


class Module:
    def __init__(self, name, destination_modules):
        self.name = name
        self.output_modules = destination_modules
        self.signal_to_send = None

    def print_line(self, destinaton_module_key):
        signal_name = "low"
        if self.signal_to_send == 1:
            signal_name = "high"
        # print(f"{self.name} -{signal_name}-> {destinaton_module_key}")

    def send(self, destination_module_key):
        global signals_sent

        self.print_line(destination_module_key)
        signals_sent[self.signal_to_send] += 1

        if destination_module_key in modules.keys():
            module = modules[destination_module_key]
            # module.receive(self.signal_to_send, self.name)
            process_queue.append(
                (destination_module_key, self.signal_to_send, self.name)
            )

    def process(self):
        global signals_sent

        if self.signal_to_send != None:
            for destinaton_module_key in self.output_modules:
                self.send(destinaton_module_key)

        self.signal_to_send = None


class Flipflop(Module):
    def __init__(self, name, output_modules):
        self.on = False
        super().__init__(name, output_modules)

    def receive(self, signal, _):
        if signal == 0:
            if not self.on:
                self.on = True
                self.signal_to_send = 1
            else:
                self.on = False
                self.signal_to_send = 0


class Conjunction(Module):
    def __init__(self, name, output_modules):
        self.input_signals = {}
        self.signal_to_send = None
        super().__init__(name, output_modules)

    def add_input(self, module_key):
        self.input_signals[module_key] = 0

    def receive(self, signal, sender):
        self.input_signals[sender] = signal

        if all([s == 1 for s in self.input_signals.values()]):
            self.signal_to_send = 0
        else:
            self.signal_to_send = 1


class Broadcaster(Module):
    def receive(self, signal, _):
        self.signal_to_send = signal


if __name__ == "__main__":
    sender_receiver = []

    for line in input.splitlines():
        new_module = None
        module_key, receivers = line.split(" -> ")
        receivers = receivers.split(", ")
        if module_key == "broadcaster":
            new_module = Broadcaster(module_key, receivers)
        else:
            module_type = module_key[0]
            module_key = module_key[1:]
            if module_type == "%":
                new_module = Flipflop(module_key, receivers)
            elif module_type == "&":
                new_module = Conjunction(module_key, receivers)

        modules[module_key] = new_module

        for receiver in receivers:
            sender_receiver.append((module_key, receiver))

    for module_key, module in modules.items():
        if type(module) == Conjunction:
            for sender, receiver in sender_receiver:
                if receiver == module_key:
                    module.add_input(sender)

    for _ in range(1000):
        button_module = Broadcaster("button", ["broadcaster"])
        button_module.receive(0, "button")
        button_module.process()

        while process_queue:
            module_key, signal_to_send, sender_name = process_queue.pop(0)
            module = modules[module_key]
            module.receive(signal_to_send, sender_name)
            module.process()

        # print("========================")

    result = signals_sent[0] * signals_sent[1]
    print(result)
