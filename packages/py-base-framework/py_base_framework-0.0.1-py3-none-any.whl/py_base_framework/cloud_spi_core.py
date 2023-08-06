from logging.config import dictConfig

from flask import Flask, request

from cloud_spi_log import log_config

dictConfig(log_config)

app = Flask(__name__)
