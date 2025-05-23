# Abstração
# Log
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o metódo Log') 

    def log_erro(self, msg):
        return self._log(f'Error: {msg}')

    def log_sucess(self, msg):
        return self._log(f'Sucess: {msg}')

class LogFileMixin(Log):
    def _log(self, msg):
        msg_formtada = f'{msg} ({self.__class__.__name__})' 
        print('Salvando no log', msg_formtada)
        with open(LOG_FILE, 'a', encoding='utf8') as arquivo:
            arquivo.write(msg_formtada)
            arquivo.write('\n')
    
class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_erro('qualquer coisa')
    lp.log_sucess('Que legal')
    lf = LogFileMixin()
    lf.log_erro('qualquer coisa')
    lf.log_sucess('Que legal')
