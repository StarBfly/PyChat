from abc import ABCMeta, abstractclassmethod, abstractproperty


class MessageProvider(metaclass=ABCMeta):
    @abstractproperty
    def message_filter_predicate(self, predicate):
        pass

    @abstractclassmethod
    def get_messages(self):
        pass
