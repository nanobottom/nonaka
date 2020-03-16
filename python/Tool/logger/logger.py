from logging import config, getLogger

# ログ設定ファイルからログ設定を読み込み
config.fileConfig('logging.conf')
logger = getLogger(__name__)

logger.info('info')
logger.warning('warning')
logger.error('error')
