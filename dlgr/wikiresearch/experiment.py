"""The game 2048."""
import dallinger

config = dallinger.config.get_config()


def extra_parameters():
    config.register('research_prompt', unicode)


class WikiResearch(dallinger.experiment.Experiment):
    """Define the structure of the experiment."""

    def __init__(self, session=None):
        """Initialize the experiment."""
        super(WikiResearch, self).__init__(session)
        self.experiment_repeats = 1
        if session:
            self.setup()

    def configure(self):
        self.research_prompt = config.get(
            'research_prompt',
            u'What DARPA funded project was in relation to time sharing?'
        )

    def recruit(self):
        """Recruitment."""
        if not self.networks(full=False):
            self.recruiter().close_recruitment()

    def create_network(self):
        """Return a new network."""
        return dallinger.networks.Chain(max_size=1)
