from hypeman import Hypeman
from hypeman.lib import exec, cp_to_instance, cp_from_instance

client = Hypeman()
instance_id = "instance-id"

cp_to_instance(client, instance_id, "./input.txt", "/tmp/input.txt")
result = exec(client, instance_id, ["cat", "/tmp/input.txt"])
print(result.output.decode(), end="")
cp_from_instance(client, instance_id, "/tmp/input.txt", "./downloads")
