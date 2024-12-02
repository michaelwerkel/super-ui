from subprocess import Popen, PIPE

def run_stdout(commandString):
	process = Popen(["bash", "-c", commandString], stdout=PIPE)
	result = ""
	for line in process.stdout.readlines():
		result = result + str(line)
	return result

def getSwarmStacks(settings):
	return run_stdout(settings["commands"]["list_swarm_stacks"])

def getComposeStacks(settings):
	return run_stdout(settings["commands"]["list_compose_stacks"])