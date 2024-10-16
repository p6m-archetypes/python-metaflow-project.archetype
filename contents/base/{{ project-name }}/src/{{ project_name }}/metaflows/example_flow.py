import os

import logging
from metaflow import FlowSpec, step, kubernetes, trigger, Parameter
logger = logging.getLogger(__name__)


@trigger(event="{{ project_name }}_example_flow_trigger")
class {{ ProjectName }}ExampleFlow(FlowSpec):
    example_parameter = Parameter("example_parameter", default='example_default')
    @step
    def start(self):
        print('Start step')
        self.next(self.process)

    @step
    def end(self):
        print('End step')

    @kubernetes(service_account="{{ project-name }}-example-flow-config",
                image='p6m.jfrog.io/p6m-dev-docker/applications/{{ project-name }}-server:latest')
    @step
    def process(self):
        print('Process step')
        print(f'example_parameter: {self.example_parameter}')
        self.next(self.end)


if __name__ == "__main__":
    {{ ProjectName }}ExampleFlow()
