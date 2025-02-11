import subprocess
from jinja2 import Template

last_stderr = []

def run_stdout(commandString):
	result = subprocess.run([commandString], shell=True, capture_output=True, text=True)
	last_stderr.append(result.stderr.strip())
	return result.stdout.strip()

def getLastStdErr():
	global last_stderr
	last=last_stderr
	last_stderr = []
	return last

def render_command(settings, commandTemplate, stackName):
	command = Template(commandTemplate).render(stackname=stackName)
	return command

def asList(stdout):
	return stdout.split("\n")

def getSwarmStacks(settings):
	return asList(run_stdout(render_command(settings, settings["commands"]["list_swarm_stacks"], None)))

def getSwarmStack(settings, stackName):
	return run_stdout(render_command(settings, settings["commands"]["generate_compose_swarm_stack"], stackName))

def getComposeStacks(settings):
	return asList(run_stdout(render_command(settings, settings["commands"]["list_compose_stacks"], None)))

def getComposeStack(settings, stackName):
	return run_stdout(render_command(settings, settings["commands"]["generate_compose_stack"], stackName))