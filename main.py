from multiprocessing import Pool
import concurrent.futures
import logging
import time
import traceback
import datetime

class MultiDemo:

	logger = logging.getLogger('root')
	
	def main_process(self):
		print("do something")
		
	def tasks(self):
		inputs = []
		try:
            with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
                futures = [executor.submit(self.main_process) for inp in
                           inputs]
        except Exception as e:
            traceback.print_exc()
            self.logger.error("Error occurred while processing: " + str(e))