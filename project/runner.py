from subprocess import Popen, PIPE
from django.test.runner import DiscoverRunner
from django.conf import settings
from react.render_server import render_server


TEST_REACT_SERVER_HOST = getattr(settings, 'TEST_REACT_SERVER_HOST', '127.0.0.1')
TEST_REACT_SERVER_PORT = getattr(settings, 'TEST_REACT_SERVER_PORT', 9008)


class CustomTestRunner(DiscoverRunner):
    """
    Same as the default Django test runner, except it also runs our node
    server as a subprocess so we can render React components.
    """

    def setup_test_environment(self, **kwargs):
        # Start the test node server
        self.node_server = Popen(
            [
                'node',
                'react-server.js',
                '--host=%s' % TEST_REACT_SERVER_HOST,
                '--port=%s' % TEST_REACT_SERVER_PORT
            ],
            stdout=PIPE
        )
        # Wait until the server is ready before proceeding
        self.node_server.stdout.readline()
        # Point the renderer to our new test server
        settings.REACT = {
            'RENDER': True,
            'RENDER_URL': 'http://%s:%s' % (
                TEST_REACT_SERVER_HOST, TEST_REACT_SERVER_PORT
            ),
        }
        super(CustomTestRunner, self).setup_test_environment(**kwargs)

    def teardown_test_environment(self, **kwargs):
        # Kill the node server
        self.node_server.terminate()
        super(CustomTestRunner, self).teardown_test_environment(**kwargs)