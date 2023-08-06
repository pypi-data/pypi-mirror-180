import pytest
from tests.common.logger import get_logger
from helix_events_sdk.event_reader import KafkaEventReader


@pytest.mark.skip(reason="only manual test runs on the local machine works with stag/prod vpn")
def test_read_events_from_topic(caplog) -> None:
    kafka_brokers = [
        "b-2.staging-kafka-cluster.7f9ja3.c7.kafka.us-east-1.amazonaws.com:9094",
        "b-1.staging-kafka-cluster.7f9ja3.c7.kafka.us-east-1.amazonaws.com:9094"
    ]
    audit_topic = "audit"
    logger = get_logger()
    with KafkaEventReader(
        topic=audit_topic,
        group_id='my-group',
        logger=logger,
        kafka_brokers=kafka_brokers,
        use_ssl=True
    ) as kafka_event_consumer:
        for i in range(5):
            audit_event = kafka_event_consumer.read_next_event()
            if audit_event:
                with open(f"audit_event_{i}.json", 'a') as file:
                    file.write(f"{audit_event}")
