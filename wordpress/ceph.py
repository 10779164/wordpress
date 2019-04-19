import rados

cluster=rados.Rados(conffile='/root/test/ceph.conf')
cluster.connect()
