from abc import ABCMeta, abstractmethod

# Observer follows the design pattern of observers. Code taken from class slide.
class Observer(object):
    def __init__(self):
        __metaclass__ = ABCMeta

        @abstractmethod
        def update(self, object):
            pass

# Observable follows the design pattern for observables, code is taken from class slide but is slightly modified.
class Observable(object):
    def __init__(self):
        self.observers = []

    def update_observer(self, object):
        for i in self.observers:
               i.update(object)

    def add_observer(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)

    def remove_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def remove_all_observers(self):
        self.observers = []

