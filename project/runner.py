from subprocess import Popen, PIPE
from django.test.runner import DiscoverRunner


class CustomTestRunner(DiscoverRunner):
    """
    Same as the default Django test runner, except it also runs our node
    server as a subprocess so we can render React components.
    """

    def setup_test_environment(self, **kwargs):
        # Start the node server
        self.node_server = Popen(['node', 'react-server.js'], stdout=PIPE)
        # Wait until the server is ready before proceeding
        _ = self.node_server.stdout.readline()
        super(CustomTestRunner, self).setup_test_environment(**kwargs)

    def teardown_test_environment(self, **kwargs):
        # Kill the node server
        self.node_server.terminate()
        super(CustomTestRunner, self).teardown_test_environment(**kwargs)