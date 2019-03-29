“At 06:00 on every 5th day-of-month.”

at 2019-03-31 06:00:00
then at 2019-04-01 06:00:00
then at 2019-04-06 06:00:00
then at 2019-04-11 06:00:00
then at 2019-04-16 06:00:00


CRONTAB = 00 06 */5 * * /tmp/excluir_bkp.py



import datetime
from datetime import date
import os

def Excluir_BKP():
	arquivo = "zabbix{}.bkp.gz".format(str(date.today() + datetime.timedelta(days=-5)).replace("-","_"))
    path = "/app/opt/perfcenter/backup/"
    dir = os.listdir(path)
    for file in dir:
        if file == arquivo:
            os.remove(file)
			return("Arquivo {0} Excluido".format(arquivo))
		else:
			return("Problema com Exclusão de BKP")

def main():
	Excluir_BKP()

if __name__ == "__main__":
	main()
