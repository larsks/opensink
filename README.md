# OpenSink: All the OpenStack APIs in one place

Do you sometimes need to write scripts that interact with the
OpenStack API?  Do you always find yourself spending more time trying
to remember how to get a valid Nova client than actually writing your
scripts?

This is for you.

## Usage

Assuming that you have the standard suite of `OS_*` environment
variable available, then using `opensink` is as simple as:

    >>> import opensink.openstack
    >>> clients = opensink.openstack.OpenStack()

Need a list of servers?

    >>> clients.nova.servers.list()
    [<Server: larstest-server-23dwogjbq3ux>, <Server: cirros>]

Want to create a Cinder volume?

    >>> clients.cinder.volumes.create(1)
    <Volume: e61ffb18-7d97-4dde-ba70-b256df7b709f>

How about a list of resources in your heat stack?

    >>> [ r.to_dict()['resource_name']
    ... for r in clients.heat.resources.list(id)]
    [u'server_floating', u'secgroup_all_open', u'server_eth0', u'server']


