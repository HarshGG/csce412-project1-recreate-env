import boto3

instance = 'CSCE412_Project1'
snapshot = 'CSCE412_Project1-1694025293'

client = boto3.client('lightsail', region_name = 'us-east-2a')

num_instances = int(input('Enter how many instances you would like: '))

instance_names = []

for i in range(num_instances):
    instance_names.append(f"CSCE412_Project1-Instance{i}")

try: 
    response1 = client.create_instances(
        instanceNames=instance_names,
        availabilityZone='us-east-2a',
        blueprintId='windows_server_2022',
        bundleId = 'nano_3_0'
    )
except Exception as ex:
    print(ex)
