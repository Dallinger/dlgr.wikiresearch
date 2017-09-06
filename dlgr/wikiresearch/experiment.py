"""The game 2048."""
import dallinger

config = dallinger.config.get_config()


def extra_parameters():
    config.register('n', int)


class WikiResearch(dallinger.experiment.Experiment):
    """Define the structure of the experiment."""

    def __init__(self, session=None):
        """Initialize the experiment."""
        super(WikiResearch, self).__init__(session)
        self.experiment_repeats = 1
        N = config.get("n")
        self.initial_recruitment_size = N
        if session:
            self.setup()

    def recruit(self):
        """Recruitment."""
        if not self.networks(full=False):
            self.recruiter().close_recruitment()

    def create_network(self):
        """Return a new network."""
        return dallinger.networks.Chain(max_size=1)
