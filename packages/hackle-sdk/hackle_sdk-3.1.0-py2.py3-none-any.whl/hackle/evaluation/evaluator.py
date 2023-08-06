class Evaluation(object):
    def __init__(self, variation_id, variation_key, reason, config=None):
        self.variation_id = variation_id
        self.variation_key = variation_key
        self.reason = reason
        self.config = config

    def __eq__(self, o):
        if isinstance(o, self.__class__):
            return self.__dict__ == o.__dict__
        else:
            return False

    def __str__(self):
        return 'Evaluation(variation_id={}, variation_key={}, reason={}, config={})'.format(self.variation_id,
                                                                                            self.variation_key,
                                                                                            self.reason,
                                                                                            self.config)

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def with_variation(workspace, variation, reason):
        parameter_configuration_id = variation.parameter_configuration_id
        if parameter_configuration_id is None:
            return Evaluation(variation_id=variation.id, variation_key=variation.key, reason=reason, config=None)

        parameter_configuration = workspace.get_parameter_configuration_or_none(parameter_configuration_id)
        if parameter_configuration is None:
            raise Exception('ParameterConfiguration[{}]'.format(parameter_configuration_id))

        return Evaluation(variation_id=variation.id, variation_key=variation.key, reason=reason,
                          config=parameter_configuration)

    @staticmethod
    def of(workspace, experiment, variation_key, reason):
        variation = experiment.get_variation_by_key_or_none(variation_key)
        if variation is None:
            return Evaluation(variation_id=None, variation_key=variation_key, reason=reason, config=None)
        else:
            return Evaluation.with_variation(workspace, variation, reason)


class Evaluator(object):

    def __init__(self, evaluation_flow_factory):
        self.evaluation_flow_factory = evaluation_flow_factory

    def evaluate(self, workspace, experiment, user, default_variation_key):
        evaluation_flow = self.evaluation_flow_factory.get_evaluation_flow(experiment.type)
        return evaluation_flow.evaluate(workspace, experiment, user, default_variation_key)
