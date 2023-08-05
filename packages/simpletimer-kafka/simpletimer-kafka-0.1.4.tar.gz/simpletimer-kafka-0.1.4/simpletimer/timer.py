# a simple class to record time taken for something to complete
import logging
import time
from datetime import datetime
from json import dumps

from confluent_kafka import SerializingProducer


class Stopwatch(object):
    """
    A class that can be wrapped around a function using a 'with' statement to record the time taken for the operation within to complete

    """

    def __init__(self, print_time=True):
        try:
            logging.basicConfig(
                level=logging.INFO,
                datefmt="%d/%m/%Y %I:%M:%S %p",
                format="[%(asctime)s] %(levelname)s: %(message)s",
            )
            self.print_time = print_time
            self.start = 0
            self.time_taken = 0
        except:
            logging.error("Stopwatch init error")

    def __enter__(self):
        try:
            self.start = time.perf_counter()
        except:
            logging.error("Time log error has occurred on entry")

    def __exit__(self, *args):
        try:
            self.time_taken = time.perf_counter() - self.start
            if self.print_time:
                logging.info(f"Time taken to complete operations: {self.time_taken}s")
        except:
            logging.error("Time log error has occurred on exit")


class StopwatchKafka(Stopwatch):
    """
    A subclass of the Stopwatch class that has additional functionalities for sending data to a Kafka topic via the Kafka Producer
    """

    def __init__(
        self,
        bootstrap_servers="localhost:9092",
        kafka_topic="",
        encoding="utf-8",
        print_time=True,
        kafka_keys=None,
        kafka_headers=None,
        kafka_parition=None,
        metadata=None,
    ):
        try:
            super().__init__(print_time)
            self.kafka_topic = kafka_topic
            self.kafka_keys = kafka_keys
            self.kafka_headers = kafka_headers
            self.kafka_parition = kafka_parition
            self.kafka_conf = {
                "bootstrap.servers": bootstrap_servers,
                "value.serializer": lambda x: dumps(x).encode(encoding),
            }
            self.producer = SerializingProducer(self.kafka_conf)
            if metadata is None:
                metadata = {"type": "processing_time"}
            self.metadata = metadata
        except Exception as e:
            logging.error("StopwatchKafka init error")
            logging.error(e)

    def __enter__(self):
        super().__enter__()

    def __exit__(self, *args):
        super().__exit__()
        try:
            # NOTE: edit this or make it dynamic for extra data to be sent over to topic???
            time_data = {
                "time_taken": self.time_taken,
                "timestamp": datetime.utcnow().isoformat(),
            }
            # async operation
            self.producer.produce(
                topic=self.kafka_topic,
                value=time_data,
                key=self.kafka_keys,
                headers=self.kafka_headers,
                partition=self.kafka_parition,
            )
            logging.info("Time data logging sent to Kafka Topic")
        except Exception as e:
            logging.error("Producer failed to send data to topic")
            logging.error(e)
