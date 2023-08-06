from typing import Optional

from flask import current_app

from dh_potluck.messaging.exceptions import NoBrokersFoundException
from dh_potluck.messaging.typings import ConsumerConfig


def build_consumer_config(
    consumer_group_id: str, config_overrides: Optional[ConsumerConfig] = None
) -> ConsumerConfig:
    brokers = current_app.config['KAFKA_BROKERS_LIST']
    if not brokers:
        raise NoBrokersFoundException

    config: ConsumerConfig = {
        'bootstrap.servers': brokers,
        'group.id': consumer_group_id,
        'enable.auto.commit': False,
        'auto.offset.reset': 'earliest',
    }
    should_connect_ssl = current_app.config.get('KAFKA_USE_SSL_CONNECTION')
    if should_connect_ssl:
        config['security.protocol'] = 'SSL'
    if config_overrides:
        config.update(config_overrides)
    return config
