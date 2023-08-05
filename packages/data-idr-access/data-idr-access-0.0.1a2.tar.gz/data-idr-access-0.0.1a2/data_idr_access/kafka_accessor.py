import kafka3 as kafka
from data_idr_access.accessor import Accessor


class KafkaAccessor(Accessor):
    def __init__(self, config_json):
        super().__init__(config_json)
        self.conn = {
            "producer": kafka.KafkaProducer(**config_json['producer']) if config_json.get('producer') else None,
            "consumer": kafka.KafkaConsumer(**config_json['consumer']) if config_json.get('consumer') else None,
            "client": kafka.KafkaClient(**config_json['client']) if config_json.get('client') else None
        }

    def reconnect(self):
        self.disconnect()
        self.conn = {
            "producer": kafka.KafkaProducer(**self.config['producer']) if self.config.get('producer') else None,
            "consumer": kafka.KafkaConsumer(**self.config['consumer']) if self.config.get('producer') else None,
            "client": kafka.KafkaClient(**self.config['client']) if self.config.get('client') else None
        }

    def disconnect(self):
        if self.conn:
            if self.conn.get('producer'):
                self.conn['producer'].close()
            if self.conn.get('consumer'):
                self.conn['consumer'].close()
            if self.conn.get('client'):
                self.conn['client'].close()

    def create_topic(self, topic):
        return self.conn['client'].add_topic(topic)

    def get_partition(self, topic):
        if not self.conn['producer']:
            return None
        return self.conn['producer'].partitions_for(topic)

    def produce(self, topic, value, key, partition, flush=False):
        if not self.conn['producer']:
            return False
        future = self.conn['producer'].send(
            topic, value=value,
            key=key, partition=partition)  # 同一个key值，会被送至同一个分区向分区1发送消息
        if flush:
            self.conn['producer'].flush()
        return future.get(timeout=10)  # 监控是否发送成功

    def consume(self, topic, commit=False):
        if not self.conn['consumer']:
            return False
        for message in self.conn['consumer']:
            yield message
            if commit:
                self.conn['consumer'].commit()

    def data_remaining(self, topic):
        if not self.conn['consumer']:
            return None
        consumer = self.conn['consumer']
        partitions = [kafka.TopicPartition(topic, p) for p in consumer.partitions_for_topic(topic)]

        # total
        toff = consumer.end_offsets(partitions)
        toff = [(key.partition, toff[key]) for key in toff.keys()]
        toff.sort()
        print("total offset: {}".format(str(toff)))

        # current
        coff = [(x.partition, consumer.committed(x)) for x in partitions]
        coff.sort()
        print("current offset: {}".format(str(coff)))

        # cal sum and left
        toff_sum = sum([x[1] for x in toff])
        cur_sum = sum([x[1] for x in coff if x[1] is not None])
        left_sum = toff_sum - cur_sum
        print("kafka left: {}".format(left_sum))

        return left_sum
