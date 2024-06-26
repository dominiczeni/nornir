A collection of [nornir](https://github.com/nornir-automation/nornir) python scripts.



Example of content for the nornir YAML config file leveraging the [nornir-csv](https://github.com/matman26/nornir_csv) inventory plugin.

```
inventory:
  plugin: CsvInventoryPlugin
  options:
runner:
  plugin: threaded
  options:
    num_workers: 20
```

Example of content for 'host.csv' file that should be present in ./inventory/ directory.  The username/password can be input with any value as the actual credentials will be gathered at runtime.

```
name,hostname,platform,port,username,password
host1,1.1.1.1,cisco_xe,22,bogus,bogus
host2,2.2.2.2,cisco_xe,22,bogus,bogus
```
