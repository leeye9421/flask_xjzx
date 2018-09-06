import logging
import redis


class Config:
    """工程配置"""
    SECRET_KEY = "fjsifjsifdsfsdini"

    #数据库配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/xjzx"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    #配置redis
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    #配置session
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_USE_SIGNER = True
    PERMANENT_SESSION_LIFETIME = 86400


class DevelopmentConfig(Config):
    DEBUG = True
    # 日志
    LOG_LEVEL = logging.DEBUG

class ProductionConfig(Config):
    # 日志
    LOG_LEVEL = logging.ERROR

config = {
    "development":DevelopmentConfig,
    "production":ProductionConfig
}