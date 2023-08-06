# helix.events.sdk

The helix.events.sdk package facilitates sending strongly typed events within the helix architecure. Currently one type of event, AuditEvent, is supported. 

### How to set up
* `make devsetup` - to build the dev setup
* `make tests` - to run all tests under `/tests/` directory


### Examples
* The following code snippet shows how to instantiate and send and audit event:

```python
# create the AuditEvent
event = AuditEvent(Source.BWELLBACKEND, Audit(patient_id="1",
                                              user_id="1",
                                              user_role="Patient",
                                              ip_address="192.168.1.1",
                                              action=AuditAction.READ,
                                              action_type=AuditActionType.VIEW,
                                              accessed_resource=ResourceType.DIAGNOSES))

kafka_brokers = [
    "kafkabroker1:9092",
    "kafkabroker1:9092"
]
with KafkaEventWriter(
    get_logger(), kafka_brokers=kafka_brokers, use_ssl=True
) as kafka_event_writer:
    kafka_event_writer.write_event(event=event)
```
The above code shows how to write an event to Kafka assuming the kafka cluster has two brokers and uses TLS.
