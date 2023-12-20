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


def print_line(name, signal, destination):
    signal_name = "low"
    if signal == 1:
        signal_name = "high"
    print(f"{name} -{signal_name}-> {destination}")


class Module:
    def __init__(self):
        pass


class Flipflop(Module):
    def __init__(self, name, output_modules):
        self.name = name
        self.output_modules = output_modules
        self.signal_to_send = None
        self.on = False

    def receive(self, signal, _):
        if signal == 0:
            if not self.on:
                self.on = True
                self.signal_to_send = 1
            else:
                self.on = False
                self.signal_to_send = 0

    def process(self):
        if self.signal_to_send != None:
            for module_key in self.output_modules:
                print_line(self.name, self.signal_to_send, module_key)
                signals_sent[self.signal_to_send] += 1
                if module_key in modules.keys():
                    module = modules[module_key]
                    process_queue.append(module_key)
                    module.receive(self.signal_to_send, self.name)

        self.signal_to_send = None


class Conjunction(Module):
    def __init__(self, name, output_modules):
        self.name = name
        self.output_modules = output_modules
        self.input_signals = {}
        self.signal_to_send = None

    def add_input(self, module_key):
        self.input_signals[module_key] = 0

    def receive(self, signal, sender):
        self.input_signals[sender] = signal

        if all([s == 1 for s in self.input_signals.values()]):
            self.signal_to_send = 0
        else:
            self.signal_to_send = 1

    def process(self):
        if self.signal_to_send != None:
            for module_key in self.output_modules:
                print_line(self.name, self.signal_to_send, module_key)
                signals_sent[self.signal_to_send] += 1
                if module_key in modules.keys():
                    module = modules[module_key]
                    process_queue.append(module_key)
                    module.receive(self.signal_to_send, self.name)

        self.signal_to_send = None


class Broadcaster(Module):
    def __init__(self, name, output_modules):
        self.name = name
        self.output_modules = output_modules
        self.signal_to_send = None

    def receive(self, signal, _):
        self.signal_to_send = signal

    def process(self):
        if self.signal_to_send != None:
            for module_key in self.output_modules:
                print_line(self.name, self.signal_to_send, module_key)
                signals_sent[self.signal_to_send] += 1
                if module_key in modules.keys():
                    module = modules[module_key]
                    process_queue.append(module_key)
                    module.receive(self.signal_to_send, self.name)

        self.signal_to_send = None


if __name__ == "__main__":
    sender_receiver = []

    for line in input.splitlines():
        new_module = Module()
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
        signals_sent[0] += 1
        modules["broadcaster"].receive(0, "button")
        process_queue.append("broadcaster")
        print_line("button", 0, "broadcaster")
        print("button -0-> broadcaster")

        while process_queue:
            module_key = process_queue.pop(0)
            module = modules[module_key]
            result = module.process()

        print("========================")

    result = signals_sent[0] * signals_sent[1]
    print(result)
