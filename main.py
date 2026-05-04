from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result
from nornir.core.task import Task, Result

def gather_facts(task: Task) -> Result:
    version = task.run(
        task=netmiko_send_command,
        command_string="show version"
    )
    interfaces = task.run(
        task=netmiko_send_command,
        command_string="show ip interface brief"
    )
    return Result(host=task.host)
def push_config(task: Task):
    task.run(
        task=netmiko_send_config,
        config_commands=[
            "interface Loopback100",
            "description managed by nornir",
        ]
    )
nr = InitNornir(config_file="config.yaml")
result_facts = nr.run(task=gather_facts)
result_config = nr.run(task=push_config)

print_result(result_facts)
print_result(result_config)


