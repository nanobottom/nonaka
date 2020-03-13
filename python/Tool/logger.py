from logging import getLogger, StreamHandler, FileHandler,\
                    Formatter, Logger, DEBUG, INFO

"""
ログレベル：
DEBUG > INFO > WARNING > ERROR > CRITICAL
"""
def get_logger(save_name='sample.log'):
    # ロガーを取得する
    logger = getLogger(__name__)
    logger.setLevel(DEBUG) # 出力レベルを設定

    # ハンドラー1を生成する
    h1 = StreamHandler()
    h1.setLevel(DEBUG) # 出力レベルを設定

    # ハンドラー2を生成する
    h2 = FileHandler(save_name)
    h2.setLevel(INFO) # 出力レベルを設定

    # フォーマッタを生成する
    fmt = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # ハンドラーにフォーマッターを設定する
    h1.setFormatter(fmt)
    h2.setFormatter(fmt)

    # ロガーにハンドラーを設定する
    logger.addHandler(h1)
    logger.addHandler(h2)
    return logger

def kill_logger(logger):
    name = logger.name
    del Logger.manager.loggerDict[name]

    return

def kill_handler(logger, handles):
    for handle in handles:
        logger.removeHandler(handle)

    return
    

if __name__ == '__main__':
    logger = get_logger()
    # ログ出力を行う
    logger.debug('debugログを出力')
    logger.info('infoログを出力')
    logger.warn('warnログを出力')
    logger.error('errorログを出力')
