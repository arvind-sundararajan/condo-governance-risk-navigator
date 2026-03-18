```json
{
    "evaluation_metrics/agent_performance.py": {
        "content": "
import logging
from typing import Dict, List
import numpy as np
from n8n import Node, Workflow
from giskard import GiskardClient
from background_matting_v2 import BackgroundMattingV2

class AgentPerformanceEvaluator:
    def __init__(self, workflow: Workflow, node: Node):
        """
        Initialize the AgentPerformanceEvaluator.

        Args:
        - workflow (Workflow): The n8n workflow.
        - node (Node): The n8n node.
        """
        self.workflow = workflow
        self.node = node
        self.logger = logging.getLogger(__name__)

    def calculate_non_stationary_drift_index(self, data: List[float]) -> float:
        """
        Calculate the non-stationary drift index.

        Args:
        - data (List[float]): The input data.

        Returns:
        - float: The non-stationary drift index.
        """
        try:
            # Calculate the non-stationary drift index using Giskard
            giskard_client = GiskardClient()
            non_stationary_drift_index = giskard_client.calculate_drift_index(data)
            self.logger.info('Non-stationary drift index calculated successfully')
            return non_stationary_drift_index
        except Exception as e:
            self.logger.error(f'Error calculating non-stationary drift index: {e}')
            return None

    def stochastic_regime_switch(self, data: List[float]) -> List[float]:
        """
        Perform stochastic regime switch.

        Args:
        - data (List[float]): The input data.

        Returns:
        - List[float]: The output data after stochastic regime switch.
        """
        try:
            # Perform stochastic regime switch using BackgroundMattingV2
            background_matting_v2 = BackgroundMattingV2()
            output_data = background_matting_v2.stochastic_regime_switch(data)
            self.logger.info('Stochastic regime switch performed successfully')
            return output_data
        except Exception as e:
            self.logger.error(f'Error performing stochastic regime switch: {e}')
            return None

    def evaluate_agent_performance(self, data: List[float]) -> Dict[str, float]:
        """
        Evaluate the agent performance.

        Args:
        - data (List[float]): The input data.

        Returns:
        - Dict[str, float]: The evaluation metrics.
        """
        try:
            # Calculate the non-stationary drift index
            non_stationary_drift_index = self.calculate_non_stationary_drift_index(data)
            # Perform stochastic regime switch
            output_data = self.stochastic_regime_switch(data)
            # Evaluate the agent performance using n8n
            evaluation_metrics = self.node.evaluate_agent_performance(output_data)
            self.logger.info('Agent performance evaluated successfully')
            return evaluation_metrics
        except Exception as e:
            self.logger.error(f'Error evaluating agent performance: {e}')
            return None

if __name__ == '__main__':
    # Create a sample workflow and node
    workflow = Workflow()
    node = Node()
    # Create an instance of the AgentPerformanceEvaluator
    evaluator = AgentPerformanceEvaluator(workflow, node)
    # Generate some sample data
    data = np.random.rand(100).tolist()
    # Evaluate the agent performance
    evaluation_metrics = evaluator.evaluate_agent_performance(data)
    # Print the evaluation metrics
    print(evaluation_metrics)
",
        "commit_message": "feat: implement specialized agent_performance logic"
    }
}
```