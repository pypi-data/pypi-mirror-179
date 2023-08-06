_C=None
_B='kinesis'
_A=False
import logging,os,threading
from pathlib import Path
from typing import Optional
from localstack import config
from localstack.services.kinesis import kinesis_starter
from localstack.services.kinesis.kinesis_starter import check_kinesis
from localstack.utils.aws import aws_stack
from localstack.utils.files import mkdir,rm_rf
from localstack.utils.functions import run_safe
from localstack.utils.net import wait_for_port_closed
from localstack.utils.patch import patch
from localstack.utils.run import run
from localstack.utils.serving import Server
from localstack.utils.sync import retry,synchronized
from localstack_ext.bootstrap.pods.server.plugins import StateLifecyclePlugin
LOG=logging.getLogger(__name__)
RESTART_LOCK=threading.RLock()
class KinesisPersistencePlugin(StateLifecyclePlugin):
	name=_B;service=_B
	def inject_assets(A,pod_asset_directory):shutdown_kinesis();super().inject_assets(pod_asset_directory);restart_kinesis(clean_dir=_A)
	def reset_state(A):super().reset_state();reset_kinesis()
def get_kinesis_persist_path():return os.path.join(config.dirs.data,_B)
@patch(kinesis_starter.start_kinesis)
def start_kinesis(fn,port=_C,update_listener=_C,asynchronous=_C,**B):
	A=get_kinesis_persist_path();C=B.get('clean_dir',True)
	if C and Path(A).is_relative_to(config.dirs.tmp):LOG.debug('Remove path before starting server');rm_rf(A)
	mkdir(A);return fn(port,update_listener,asynchronous,os.path.abspath(A))
def wait_for_kinesis():retry(check_kinesis,sleep=0.5,retries=10)
def reset_kinesis():
	A=aws_stack.connect_to_service(_B);C=A.list_streams()['StreamNames']
	for B in C:
		try:A.delete_stream(StreamName=B,EnforceConsumerDeletion=True)
		except Exception as D:LOG.debug('error cleaning up kinesis stream %s: %s',B,D)
@synchronized(lock=RESTART_LOCK)
def shutdown_kinesis():
	import psutil as F;from localstack.services.kinesis import kinesis_starter as B;A=B._server
	if not A:return _A
	C=A.port;A._thread.auto_restart=_A;A.shutdown();A.join(timeout=10)
	try:wait_for_port_closed(C,sleep_time=0.8,retries=10)
	except Exception:LOG.warning('Kinesis server port %s (%s) unexpectedly still open; running processes: %s',C,B._server._thread,run(['ps','aux']));D=A._thread.process.pid;LOG.info('Attempting to kill Kinesis process %s',D);E=F.Process(D);run_safe(E.terminate);run_safe(E.kill);wait_for_port_closed(C,sleep_time=0.5,retries=8)
	B._server=_C;return True
@synchronized(lock=RESTART_LOCK)
def restart_kinesis(if_running=_A,clean_dir=_A):
	from localstack.services.kinesis import kinesis_starter as A;B=shutdown_kinesis()
	if if_running and not B:return A._server
	LOG.debug('Restarting Kinesis process ...');C=A.start_kinesis(clean_dir=clean_dir);wait_for_kinesis();return C