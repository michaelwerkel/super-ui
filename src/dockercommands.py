from subprocess import Popen, PIPE

def run_stdout(commandString):
	process = Popen(["bash", "-c", commandString], shell=True, stdout=PIPE)
	result = ""
	for line in process.stdout:
		result = result + line
	return result

def getSwarmStacks(settings):
	return run_stdout(settings["commands"]["list_swarm_stacks"])

def getComposeStacks(settings):
	return run_stdout(settings["commands"]["list_compose_stacks"])