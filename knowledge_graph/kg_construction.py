```json
{
    "knowledge_graph/kg_construction.py": {
        "content": "
import logging
from typing import Dict, List
from n8n import Node, Workflow
from giskard import GiskardClient
from background_matting_v2 import BackgroundMattingV2
from microsoft_excel_365 import Excel365Client

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class KnowledgeGraphConstructor:
    def __init__(self, workflow: Workflow):
        """
        Initialize the knowledge graph constructor.

        Args:
        - workflow (Workflow): The n8n workflow instance.
        """
        self.workflow = workflow
        self.giskard_client = GiskardClient()
        self.background_matting_v2 = BackgroundMattingV2()
        self.excel_365_client = Excel365Client()

    def construct_knowledge_graph(self, non_stationary_drift_index: int, stochastic_regime_switch: bool) -> Dict:
        """
        Construct the knowledge graph.

        Args:
        - non_stationary_drift_index (int): The index of the non-stationary drift.
        - stochastic_regime_switch (bool): Whether to switch the stochastic regime.

        Returns:
        - Dict: The constructed knowledge graph.
        """
        try:
            # Get the Excel data
            excel_data = self.excel_365_client.get_data()
            logger.info('Excel data retrieved')

            # Apply background matting
            background_matted_data = self.background_matting_v2.apply(excel_data)
            logger.info('Background matting applied')

            # Apply Giskard logic
            giskard_data = self.giskard_client.apply(background_matted_data)
            logger.info('Giskard logic applied')

            # Construct the knowledge graph
            knowledge_graph = self.workflow.construct_knowledge_graph(giskard_data, non_stationary_drift_index, stochastic_regime_switch)
            logger.info('Knowledge graph constructed')

            return knowledge_graph
        except Exception as e:
            logger.error(f'Error constructing knowledge graph: {e}')
            raise

    def update_knowledge_graph(self, knowledge_graph: Dict, new_data: List) -> Dict:
        """
        Update the knowledge graph with new data.

        Args:
        - knowledge_graph (Dict): The existing knowledge graph.
        - new_data (List): The new data to update the knowledge graph with.

        Returns:
        - Dict: The updated knowledge graph.
        """
        try:
            # Update the knowledge graph
            updated_knowledge_graph = self.workflow.update_knowledge_graph(knowledge_graph, new_data)
            logger.info('Knowledge graph updated')

            return updated_knowledge_graph
        except Exception as e:
            logger.error(f'Error updating knowledge graph: {e}')
            raise

if __name__ == '__main__':
    # Create a new n8n workflow
    workflow = Workflow()

    # Create a new knowledge graph constructor
    knowledge_graph_constructor = KnowledgeGraphConstructor(workflow)

    # Construct the knowledge graph
    knowledge_graph = knowledge_graph_constructor.construct_knowledge_graph(1, True)

    # Update the knowledge graph
    updated_knowledge_graph = knowledge_graph_constructor.update_knowledge_graph(knowledge_graph, [1, 2, 3])

    # Print the updated knowledge graph
    print(updated_knowledge_graph)
",
        "commit_message": "feat: implement specialized kg_construction logic"
    }
}
```