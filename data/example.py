import boto3

cliant = boto3.cliant('route53')

response = cliant.create_hosted_zone(

 Name='test.pyarashiro.com',
 CallerReference='2018042001'
    
)

id = response['HostZone']['Id']
response = cliant.change_resource_record_sets(
    HostedZoneId='Z2HBN7K2VNLICZ',
    changeBatch={
        'changes':[
            {
                'Action': 'CREATE',
                'ResourceRecordset':{
                    'name': 'test',
                    'type': 'A',
                    'ResourceRecords': [
                        {
                            '192.168.0.1'
                        },
                    ],
                }
            }
        ]
    }

)
