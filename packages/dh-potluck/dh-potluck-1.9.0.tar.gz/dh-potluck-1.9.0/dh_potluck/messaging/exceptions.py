from confluent_kafka import KafkaException


class CommitTimeoutException(KafkaException):
    pass


class NoBrokersFoundException(RuntimeError):
    def __init__(self) -> None:
        self.message = (
            'Tried to instantiate a MessageConsumer without setting the KAFKA_BROKERS_LIST env var'
        )
        super().__init__(self.message)
