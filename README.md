# General setup
- Mount the project files (e.g. XML) on the machine runnig the ELK-stack (this repo).
- Mount the project files in the docker-compose.yml for the logstash part of the configuration.
```
  logstash:
    volumes:
      - /srv/dh-e02/topelius_files/required-files/xml:/var/data/xml/topelius_xml
  ...
```
- Logstash will use the pipeline configuration files in '/logstash/pipeline' to ingest the project files (e.g. XML-files).
- The pipeline configuration files (e.g. logstash_topelius.conf) tell Logstash how to process the data before feeding it to the ElasticSearch index.

## Troubleshooting

Sometimes the the logstash process needs to be restarted to fully understand and process new configuration files. 
This could probably be fixed by running the project without Docker?
